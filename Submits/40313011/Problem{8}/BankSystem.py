import re
import random

users = []
accounts = []
day_shaba_transfers = []


class User:
    def __init__(self, name, phone_number, code, accounts):
        self.name = name
        self.phone_number = phone_number
        self.code = code
        self.accounts = accounts


class Account:
    def __init__(self, owner, card_number, account_number, balance, account_type):
        self.owner = owner
        self.card_number = card_number
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def profit(self):
        profit = 0
        if self.account_type == 'ShortTerm':
            profit = self.balance * 0.067
        if self.account_type == 'LongTerm':
            profit = self.balance * 0.167
        if self.account_type == 'Normal':
            profit = 0

        self.balance += profit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

        if self.account_type == "ShortTerm":
            self.balance -= amount * 0.03
        if self.account_type == "LongTerm":
            self.balance -= amount * 0.05

    def card_transfer(self, other, amount):
        self.balance -= amount
        other.balance += amount

        if self.account_type == "ShortTerm":
            other.balance -= amount * 0.01
        if self.account_type == "LongTerm":
            other.balance -= amount * 0.03

    def shaba_transfer(self, other, amount):
        self.balance -= amount
        other.balance += amount

        if self.account_type == "ShortTerm":
            other.balance -= amount * 0.01
        if self.account_type == "LongTerm":
            other.balance -= amount * 0.03

    def show_details(self):
        print("  Account Details: ")
        print(f"-> Cart Number: {self.card_number}")
        print(f"-> Shaba Number: {self.account_number}")
        print(f"-> Balance: {self.balance} Tomans")


command = ""
while command != "quit":
    command = input()
    command = command.split(' ')

    if command[0] == "CREATE_USER":
        name = command[1]
        name_pattern = r'^[a-zA-Z]{3,}$'
        if not re.match(name_pattern, name):
            print("Invalid name")

        phone_number = command[2]
        phone_pattern = r'^09\d{9}$'
        if not re.match(phone_pattern, phone_number):
            print("Invalid phone number")

        code = command[3]
        code_pattern = r'^\d{10}'
        if not re.match(code_pattern, code):
            print("Invalid code")

        new_user = User(name, phone_number, code, [])
        users.append(new_user)

        print(f"-> User {new_user.name} created")

    if command[0] == "CREATE_ACCOUNT":
        name = command[1]
        find_name = False
        for user in users:
            if name == user.name:
                find_name = True
        if not find_name:
            print("Invalid user")

        user = User("", "", "", [])
        for user_ in users:
            if user_.name == name:
                user = user_

        account_type = command[2]
        initial_balance = int(command[3])

        card_number = f"604321{random.randint(1000000000, 9999999999)}"
        account_number = f"IR12000000{random.randint(1000000000, 9999999999)}"

        new_account = Account(user.name, card_number, account_number, initial_balance, account_type)

        user.accounts.append(new_account)
        accounts.append(new_account)
        new_account.show_details()

    if command[0] == "TRANSFER_CARD_TO_CARD":
        origin_number = command[1]
        destination_number = command[2]
        amount = int(command[3])

        origin = Account("", "", "", 0, "")
        desination = Account("", "", "", 0, "")

        for account in accounts:
            if account.card_number == origin:
                origin = account
            if account.card_number == desination:
                desination = account

        origin.card_transfer(desination, amount)

    if command[0] == "TRANSFER_SHABA":
        origin_number = command[1]
        destination_number = command[2]
        amount = int(command[3])

        origin = Account("", "", "", 0, "")
        destination = Account("", "", "", 0, "")

        for account in accounts:
            if account.account_number == origin:
                origin = account
            if account.account_number == destination:
                destination = account

        day_shaba_transfers.append(lambda: origin.shaba_transfer(destination, amount))

    if command[0] == "CHECK_BALANCE":
        card_number = command[1]

        account = Account("", "", "", 0, "")
        for acc in accounts:
            if acc.card_number == card_number:
                account = acc

        print("Account balance: " + str(account.balance))

    if command[0] == "DEPOSIT":
        card_number = command[1]

        account = Account("", "", "", 0, "")
        for acc in accounts:
            if acc.card_number == card_number:
                account = acc

        amount = int(command[2])

        account.deposit(amount)

    if command[0] == "WITHDRAWN":
        card_number = command[1]

        account = Account("", "", "", 0, "")
        for acc in accounts:
            if acc.card_number == card_number:
                account = acc

        amount = int(command[2])

        account.withdraw(amount)

    if command[0] == "ACCOUNT_INFO":
        name = command[1]
        user = User("", "", "", [])
        for user_ in users:
            if user_.name == name:
                user = user_

        user_accounts = []
        for account in accounts:
            if account.owner == user.name:
                user_accounts.append(account)

        print(f"User {user.name}'s Information:")
        print(f"Name: {user.name}")
        print(f"Phone number: {user.phone_number}")
        print(f"National ID: {user.code}")
        print("Accounts: ")
        for account in user_accounts:
            print(account.show_details())

    if command[0] == "END_DAY":
        for account in accounts:
            account.profit()
        for shaba_transfer in day_shaba_transfers:
            shaba_transfer()




