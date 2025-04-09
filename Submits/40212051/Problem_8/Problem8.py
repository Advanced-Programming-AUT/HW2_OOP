import re

class User(object):
    def __init__(self, name, phone_number, national_id):

        if not re.match(r"^09\d{9}$", phone_number):
            raise ValueError("Invalid phone number")
        if not re.match(r"^\d{10}$", national_id):
            raise ValueError("Invalid national ID")
        if not re.match(r"^[A-Za-z0-9_]{3,}$", name):
            raise ValueError("Invalid username")

        self.name = name
        self.phone_number = phone_number
        self.national_id = national_id
        self.accounts = []

    def get_info(self):
        return (f"User: {self.name}"
                f"Phone: {self.phone_number}"
                f"National ID: {self.national_id}"
                f"Accounts: {[str(acc) for acc in self.accounts]}")

    def add_account(self, account):
        self.accounts.append(account)

class BankAccount(object):
    interest_rates = {"Normal": 0, "Short-Term": 0.067, "Long-Term": 0.167}

    def __init__(self, user, account_type, card_number, SHABA_number):
        if account_type not in self.interest_rates:
            raise ValueError("Invalid account type")

        self.user = user
        self.account_type = account_type
        self.card_number = card_number
        self.SHABA_number = SHABA_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        penalty = 0
        if self.account_type == "Short-Term":
            penalty = amount * 0.03
        elif self.account_type == "Long-Term":
            penalty = amount * 0.05

        total_deduction = amount + penalty
        if self.balance >= total_deduction:
            self.balance -= total_deduction
            return True
        return False

    def transfer(self, receiver_account, amount, method):
        fee = 0
        if method == "Card":
            if amount > 10**8:
                return False
        elif method == "SHABA":
            if amount > 10**8:
                return False
            fee = amount * (0.01 if self.account_type == "Short-Term" else 0.03)

        total_deduction = amount + fee
        if self.balance >= total_deduction:
            self.balance -= total_deduction
            receiver_account.balance += amount
            return True
        return False

    def calculate_interest(self):
        daily_interest = self.balance * (self.interest_rates[self.account_type] / 100)
        self.balance += daily_interest

    def __str__(self):
        return f"{self.account_type} Account , Card: {self.card_number}, Balance: {self.balance}"


class BankSystem(object):

    def __init__(self):
        self.users = {}

    def create_user(self, name, phone_number, national_id):

        if name in self.users:
            print("User already exists!")
            return
        self.users[name] = User(name, phone_number, national_id)
        print(f"User {name} registered successfully!")

    def create_account(self, name, account_type, card_number, SHABA_number):

        if name not in self.users:
            print("User not found!")
            return
        account = BankAccount(self.users[name], account_type, card_number, SHABA_number)
        self.users[name].add_account(account)
        print(f"{account_type} account created for {name} with card {card_number} and SHABA {SHABA_number}")

    def transfer_money(self, sender_card, receiver_card, amount, method="Card"):

        sender_account = receiver_account = None

        for user in self.users.values():
            for account in user.accounts:
                if account.card_number == sender_card:
                    sender_account = account
                if account.card_number == receiver_card:
                    receiver_account = account

        if not sender_account or not receiver_account:
            print("Invalid accounts")
            return

        if sender_account.transfer(receiver_account, amount, method):
            print("Transfer successful!")
        else:
            print("Transfer failed!")

    def check_balance(self, card_number):

        for user in self.users.values():
            for account in user.accounts:
                if account.card_number == card_number:
                    print(f"Balance for {card_number}: {account.balance}")
                    return
        print("Account not found!")

    def end_day(self):

        print("End of day processing...")
        for user in self.users.values():
            for account in user.accounts:
                account.calculate_interest()
        print("Daily interest calculated!")

    def account_info(self, name):

        if name in self.users:
            print(self.users[name].get_info())
        else:
            print("User not found!")


bank = BankSystem()
bank.create_user("Ali", "09123456789", "1234567890")
bank.create_user("Reza", "09198765432", "0987654321")
bank.create_account("Ali", "Normal", "6219861234567890", "IR123456789012345678901234")
bank.create_account("Reza", "ShortTerm", "6219869876543210", "IR987654321098765432109876")
bank.transfer_money("6219861234567890", "6219869876543210", 500000, "Card")
bank.check_balance("6219861234567890")
bank.check_balance("6219869876543210")
bank.end_day()
bank.account_info("Ali")
bank.account_info("Reza")


