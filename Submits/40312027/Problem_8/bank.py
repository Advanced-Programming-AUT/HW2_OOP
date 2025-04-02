import re
from datetime import datetime


class User:
    def __init__(self, name, phone, national_id):
        if not re.match(r"^09\d{9}$", phone):
            raise ValueError("Invalid phone number")
        if not re.match(r"^\d{10}$", national_id):
            raise ValueError("Invalid national ID")
        if not re.match(r"^[a-zA-Z0-9_]{3,}$", name):
            raise ValueError("Invalid username")

        self.name = name
        self.phone = phone
        self.national_id = national_id
        self.accounts = []

    def create_account(self, account_type, initial_balance):
        account = Account(self, account_type, initial_balance)
        self.accounts.append(account)
        return account


class Account:
    account_counter = 1000

    def __init__(self, user, account_type, balance):
        if account_type not in ['Normal', 'ShortTerm', 'LongTerm']:
            raise ValueError("invalid type,please try again...")

        self.user = user
        self.account_type = account_type
        self.balance = balance
        self.card_number = f"621986{Account.account_counter:010d}"
        self.shaba_number = f"IR{Account.account_counter:024d}"
        self.transactions = []
        Account.account_counter += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(" amount can not be negative ")
        self.balance += amount
        self.transactions.append((datetime.now(), "Deposit", amount, self.balance))

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError(" withdrawal amount is not acceptable")

        penalty = 0
        if self.account_type == 'ShortTerm':
            penalty = amount * 0.03
        elif self.account_type == 'LongTerm':
            penalty = amount * 0.05

        self.balance -= (amount + penalty)
        self.transactions.append((datetime.now(), "Withdraw", amount, self.balance))

    def transfer(self, receiver, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError(" transfer amount is not acceptable")

        fee = 0
        if self.account_type == 'ShortTerm':
            fee = amount * 0.01
        elif self.account_type == 'LongTerm':
            fee = amount * 0.03

        self.balance -= (amount + fee)
        receiver.balance += amount
        self.transactions.append((datetime.now(), "Transfer", amount, self.balance))
        receiver.transactions.append((datetime.now(), "Received Transfer", amount, receiver.balance))

    def apply_interest(self):
        if self.account_type == 'ShortTerm':
            self.balance *= 1.00067
        elif self.account_type == 'LongTerm':
            self.balance *= 1.00167
        self.transactions.append((datetime.now(), "Interest Applied", 0, self.balance))

    def print_transactions(self):
        for t in self.transactions:
            print(f"{t[0]} - {t[1]}: {t[2]} | Balance: {t[3]}")


class BankSystem:
    def __init__(self):
        self.users = {}

    def create_user(self, name, phone, national_id):
        user = User(name, phone, national_id)
        self.users[name] = user
        return user

    def end_day(self):
        for user in self.users.values():
            for account in user.accounts:
                account.apply_interest()



bank = BankSystem()
while True:
    request = input("Enter your request: ")
    if request == "EXIT":
        break

    parts = request.split()
    try:
        if parts[0] == "CREATE_USER":
            
            bank.create_user(parts[1], parts[2], parts[3])
        elif parts[0] == "CREATE_ACCOUNT":
            user = bank.users.get(parts[1])
            if user:
                user.create_account(parts[2], float(parts[3]))
        elif parts[0] == "DEPOSIT":
            acc = next(acc for user in bank.users.values() for acc in user.accounts if acc.card_number == parts[1])
            acc.deposit(float(parts[2]))
        elif parts[0] == "WITHDRAW":
            acc = next(acc for user in bank.users.values() for acc in user.accounts if acc.card_number == parts[1])
            acc.withdraw(float(parts[2]))
        elif parts[0] == "TRANSFER":
            sender = next(acc for user in bank.users.values() for acc in user.accounts if acc.card_number == parts[1])
            receiver = next(acc for user in bank.users.values() for acc in user.accounts if acc.card_number == parts[2])
            sender.transfer(receiver, float(parts[3]))
        elif parts[0] == "CHECK_BALANCE":
            acc = next(acc for user in bank.users.values() for acc in user.accounts if acc.card_number == parts[1])
            print(f"Balance: {acc.balance}")
        elif parts[0] == "SHOW_TRANSACTIONS":
            acc = next(acc for user in bank.users.values() for acc in user.accounts if acc.card_number == parts[1])
            acc.print_transactions()
        elif parts[0] == "END_DAY":
            bank.end_day()
        else:
            print("try again please... ")
    except Exception as e:
        print(f"Error: {e}")

