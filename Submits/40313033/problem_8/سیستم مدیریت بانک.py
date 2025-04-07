import re
import random


class User:
    def __init__(self, name, phone, national_id):
        if not re.match(r"^09\d{9}$", phone):
            raise ValueError("Invalid phone number!")
        if not re.match(r"^\d{10}$", national_id):
            raise ValueError("Invalid national ID!")
        if not re.match(r"^[A-Za-z0-9_]{3,}$", name) or len(re.findall(r"[A-Za-z]", name)) < 3:
            raise ValueError(
                "Invalid username! Must contain at least 3 letters.")

        self.name = name
        self.phone = phone
        self.national_id = national_id
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)


class Account:
    def __init__(self, owner, account_type, card_number, initial_balance):
        self.owner = owner
        self.account_type = account_type
        self.card_number = card_number
        self.shaba_number = f"IR{random.randint(10**23, 10**24-1)}"
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


class Bank:
    def __init__(self):
        self.users = {}
        self.accounts = {}
        self.pending_shaba_transfers = []

    def create_user(self, name, phone, national_id):
        if name in self.users:
            print("User already exists!")
            return
        try:
            user = User(name, phone, national_id)
            self.users[name] = user
            print(f"User {name} registered successfully!")
        except ValueError as e:
            print(e)

    def create_account(self, name, account_type, card_number, initial_balance):
        if name not in self.users:
            print("User does not exist!")
            return
        if card_number in self.accounts:
            print("Card number already exists!")
            return
        user = self.users[name]
        account = Account(user, account_type, card_number, initial_balance)
        user.add_account(account)
        self.accounts[card_number] = account
        print(f"{account_type} account created for {name} with:")
        print(f"- Card Number: {card_number}")
        print(f"- SHABA Number: {account.shaba_number}")
        print(f"- Initial Balance: {initial_balance} Tomans")

    def transfer_card_to_card(self, sender_card, receiver_card, amount):
        if sender_card not in self.accounts or receiver_card not in self.accounts:
            print("Invalid card number(s)!")
            return
        sender = self.accounts[sender_card]
        receiver = self.accounts[receiver_card]

        fee = 0
        if sender.account_type == "ShortTerm":
            fee = 0.01
        elif sender.account_type == "LongTerm":
            fee = 0.03

        if sender.withdraw(amount + int(amount * fee)):
            receiver.deposit(amount)
            print(f"Card-to-card transfer completed successfully!")
        else:
            print("Insufficient balance!")

    def transfer_shaba(self, sender_shaba, receiver_shaba, amount):
        sender_account = next((acc for acc in self.accounts.values(
        ) if acc.shaba_number == sender_shaba), None)
        receiver_account = next((acc for acc in self.accounts.values(
        ) if acc.shaba_number == receiver_shaba), None)

        if not sender_account or not receiver_account:
            print("Invalid SHABA number(s)!")
            return

        if sender_account.balance < amount:
            print("Insufficient balance for SHABA transfer!")
            return

        self.pending_shaba_transfers.append(
            (sender_account, receiver_account, amount))
        print("SHABA transfer scheduled. It will be processed at the end of the day.")

    def check_balance(self, card_number):
        if card_number not in self.accounts:
            print("Invalid card number!")
            return
        print(
            f"Balance of account {card_number}: {self.accounts[card_number].balance} Tomans")

    def account_info(self, name):
        if name not in self.users:
            print("User does not exist!")
            return
        user = self.users[name]
        print(f"User Information:")
        print(f"- Name: {user.name}")
        print(f"- Phone number: {user.phone}")
        print(f"- National id: {user.national_id}")
        print("Accounts")
        print("--------------------")
        for acc in user.accounts:
            print(f"- Card Number: {acc.card_number}")
            print(f"- SHABA Number: {acc.shaba_number}")
            print(f"- Type: {acc.account_type}")
            print(f"- Balance: {acc.balance} Tomans")
            print("--------------------")

    def end_day(self):
        print("Processing end of day operations...")

        for sender, receiver, amount in self.pending_shaba_transfers:
            if sender.withdraw(amount):
                receiver.deposit(amount)
                print(
                    f"SHABA transfer from {sender.shaba_number} to {receiver.shaba_number} completed: {amount} Tomans")
            else:
                print(
                    f"SHABA transfer from {sender.shaba_number} to {receiver.shaba_number} failed due to insufficient balance!")

        self.pending_shaba_transfers.clear()

        for account in self.accounts.values():
            if account.account_type == "ShortTerm":
                interest = int(account.balance * 0.00067)
                account.balance += interest
                print(
                    f"- Interest added to {account.card_number}: {interest} Tomans")
            elif account.account_type == "LongTerm":
                interest = int(account.balance * 0.00167)
                account.balance += interest
                print(
                    f"- Interest added to {account.card_number}: {interest} Tomans")


bank = Bank()

print("Enter commands (type 'exit' to stop):")
while True:
    try:
        command = input("> ").strip()
        if command.lower() == "exit":
            break
        parts = command.split()
        action = parts[0]

        if action == "CREATE_USER":
            bank.create_user(parts[1], parts[2], parts[3])
        elif action == "CREATE_ACCOUNT":
            bank.create_account(parts[1], parts[2], parts[3], int(parts[4]))
        elif action == "TRANSFER_CARD_TO_CARD":
            bank.transfer_card_to_card(parts[1], parts[2], int(parts[3]))
        elif action == "TRANSFER_SHABA":
            bank.transfer_shaba(parts[1], parts[2], int(parts[3]))
        elif action == "CHECK_BALANCE":
            bank.check_balance(parts[1])
        elif action == "ACCOUNT_INFO":
            bank.account_info(parts[1])
        elif action == "END_DAY":
            bank.end_day()
        else:
            print("Invalid command!")
    except (IndexError, ValueError):
        print("Invalid input format!")
