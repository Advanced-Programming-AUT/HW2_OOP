

import re
import random

# User class to manage users
class User:
    def __init__(self, name, phone_number, national_id):
        self.name = name
        self.phone_number = phone_number
        self.national_id = national_id
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

# Account class to manage bank accounts
class Account:
    def __init__(self, user_name, account_type, card_number):
        self.user_name = user_name
        self.account_type = account_type
        self.card_number = card_number
        self.shaba_number = self.generate_shaba()
        self.balance = 0

    def generate_shaba(self):
        return "IR" + "".join([str(random.randint(0, 9)) for _ in range(24)])

    def apply_interest(self):
        if self.account_type == "ShortTerm":
            self.balance += self.balance * 0.00067  # 0.067% daily interest
        elif self.account_type == "LongTerm":
            self.balance += self.balance * 0.00167  # 0.167% daily interest

# Bank class to manage the system
class Bank:
    def __init__(self):
        self.users = {}
        self.pending_shaba_transfers = []

    def create_user(self, name, phone_number, national_id):
        if not self.validate_user_info(name, phone_number, national_id):
            return "Error: Invalid user information."
        if name in self.users:
            return f"Error: User {name} already exists."
        user = User(name, phone_number, national_id)
        self.users[name] = user
        return f"User {name} registered successfully!"

    def validate_user_info(self, name, phone_number, national_id):
        if not re.match(r"^[a-zA-Z0-9\-]{3,}$", name):
            return False
        if not re.match(r"^09\d{9}$", phone_number):
            return False
        if not re.match(r"^\d{10}$", national_id):
            return False
        return True

    def create_account(self, user_name, account_type, card_number):
        if user_name not in self.users:
            return f"Error: User {user_name} does not exist."
        user = self.users[user_name]
        account = Account(user_name, account_type, card_number)
        user.add_account(account)
        return f"{account_type} account created for {user_name} with card number {card_number} and SHABA {account.shaba_number}."

    def transfer_card_to_card(self, sender_card, receiver_card, amount):
        sender_account = self.find_account_by_card(sender_card)
        receiver_account = self.find_account_by_card(receiver_card)

        if not sender_account or not receiver_account:
            return "Error: One or both card numbers are invalid."
        if sender_account.balance < amount:
            return "Error: Insufficient balance in sender's account."
        if amount > 10_000_000:
            return "Error: Card-to-card transfers cannot exceed 10,000,000 Tomans per day."

        sender_account.balance -= amount
        receiver_account.balance += amount
        return f"Card-to-card transfer completed successfully! Sender balance: {sender_account.balance} Tomans."

    def transfer_shaba(self, sender_shaba, receiver_shaba, amount):
        sender_account = self.find_account_by_shaba(sender_shaba)
        receiver_account = self.find_account_by_shaba(receiver_shaba)

        if not sender_account or not receiver_account:
            return "Error: One or both SHABA numbers are invalid."
        if sender_account.balance < amount:
            return "Error: Insufficient balance in sender's account."
        if amount > 100_000_000:
            return "Error: SHABA transfers cannot exceed 100,000,000 Tomans per day."

        self.pending_shaba_transfers.append((sender_account, receiver_account, amount))
        return "SHABA transfer registered and will be completed at the end of the day."

    def find_account_by_card(self, card_number):
        for user in self.users.values():
            for account in user.accounts:
                if account.card_number == card_number:
                    return account
        return None

    def find_account_by_shaba(self, shaba_number):
        for user in self.users.values():
            for account in user.accounts:
                if account.shaba_number == shaba_number:
                    return account
        return None

    def check_balance(self, card_number):
        account = self.find_account_by_card(card_number)
        if not account:
            return "Error: Invalid card number."
        return f"Balance of account {card_number}: {account.balance} Tomans."

    def end_day(self):
        # Complete pending SHABA transfers
        for sender_account, receiver_account, amount in self.pending_shaba_transfers:
            sender_account.balance -= amount
            receiver_account.balance += amount
            print(f"SHABA transfer completed: {amount} Tomans from {sender_account.shaba_number} to {receiver_account.shaba_number}.")
        self.pending_shaba_transfers.clear()

        # Apply daily interest
        for user in self.users.values():
            for account in user.accounts:
                account.apply_interest()




def bank_menu():
    bank = Bank()
    print("Welcome to the Bank Management System!")

    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. Create Account")
        print("3. Transfer (Card to Card)")
        print("4. Transfer (SHABA)")
        print("5. Check Balance")
        print("6. End Day")
        print("7. Account Information")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            name = input("Enter user name: ")
            phone_number = input("Enter phone number (e.g., 09123456789): ")
            national_id = input("Enter national ID (10 digits): ")
            print(bank.create_user(name, phone_number, national_id))

        elif choice == "2":
            user_name = input("Enter user name: ")
            account_type = input("Enter account type (Normal/ShortTerm/LongTerm): ")
            card_number = input("Enter card number (16 digits): ")
            print(bank.create_account(user_name, account_type, card_number))

        elif choice == "3":
            sender_card = input("Enter sender card number: ")
            receiver_card = input("Enter receiver card number: ")
            amount = int(input("Enter amount to transfer: "))
            print(bank.transfer_card_to_card(sender_card, receiver_card, amount))

        elif choice == "4":
            sender_shaba = input("Enter sender SHABA number: ")
            receiver_shaba = input("Enter receiver SHABA number: ")
            amount = int(input("Enter amount to transfer: "))
            print(bank.transfer_shaba(sender_shaba, receiver_shaba, amount))

        elif choice == "5":
            card_number = input("Enter card number: ")
            print(bank.check_balance(card_number))

        elif choice == "6":
            print("Ending the day...")
            bank.end_day()

        elif choice == "7":
            user_name = input("Enter user name: ")
            if user_name not in bank.users:
                print("User not found.")
            else:
                user = bank.users[user_name]
                print(f"\nUser {user_name}'s Information:")
                print(f"- Name: {user.name}")
                print(f"- Phone Number: {user.phone_number}")
                print(f"- National ID: {user.national_id}")
                print("Accounts:")
                for account in user.accounts:
                    print(f"  - Card Number: {account.card_number}")
                    print(f"  - SHABA Number: {account.shaba_number}")
                    print(f"  - Account Type: {account.account_type}")
                    print(f"  - Balance: {account.balance} Tomans")
                print("\n")

        elif choice == "8":
            print("Exiting the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    bank_menu()