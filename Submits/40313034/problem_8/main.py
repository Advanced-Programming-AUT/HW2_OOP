import sys, os
import re
from random import randint

original_stdout = sys.stdout

os.remove('output.txt')

file1 = open('input.txt', 'r')
file2 = open('output.txt', 'a')

sys.stdout = file2

# ---------- Main Code ----------

class User:
    def __init__(self, username, phone_number, national_id):
        if User.check_phone_number(phone_number) and User.check_national_id(national_id) and User.check_username(username):
            self.username = username
            self.phone_number = phone_number
            self.national_id = national_id
            self.valid = True
            self.accounts = list()
            print(f'User {self.username} registered successfully!')
        else:
            self.valid = False


    @staticmethod
    def check_phone_number(phone_number):
        if not re.match('^09[0-9]{9}$', phone_number):
            print('Phone Number is incorrect!')
            return 0
        return 1

    @staticmethod
    def check_national_id(national_id):
        if not re.match('^[0-9]{10}$', national_id):
            print('National ID is incorrect!')
            return 0
        return 1

    @staticmethod
    def check_username(username):
        if not re.match('^[a-zA-Z0-9_]{3,}$', username):
            print('Username is incorrect!')
            return 0
        return 1

    def add_account(self, account):
        self.accounts.append(account)

    def info(self):
        print(f'User {self.username}\'s information:')
        print(f'- Name: {self.username}')
        print(f'- Phone Number: {self.phone_number}')
        print(f'- National ID: {self.national_id}')
        print(f'- Accounts:')
        for account in self.accounts:
            account.info()
        print()

class Account:
    Profit = {'Normal': 1.0,
              'ShortTerm': 1.067,
              'LongTerm': 1.167}
    DepositFine = {'Normal': 1.0,
                   'ShortTerm': 0.97,
                   'LongTerm': 0.95}
    WithdrawFine = {'Normal': 1.0,
                    'ShortTerm': 1.01,
                    'LongTerm': 1.03}

    def __init__(self, user, account_type, inital_balance, card_number):
        # account type is one of ['Normal', 'ShortTerm', 'LongTerm']
        if account_type not in ['Normal', 'ShortTerm', 'LongTerm']:
            print('Account Type is incorrect!')
            self.valid = False
            return

        self.user = user
        self.account_type = account_type
        self.card_number = card_number
        self.balance = inital_balance
        self.valid = True
        self.shaba_number = 'IR00000000' + self.card_number
        self.max_card = 0
        self.max_shaba = 0

        self.user.add_account(self)

        print(f'{self.account_type} account created for {self.user.username} with card number {self.card_number} and SHABA number {self.shaba_number}.')

    @property
    def username(self):
        return self.user.username

    def transfer(self, other, amount):
        self.balance -= amount
        other.balance += amount

    def info(self):
        print(f'  - Card Number: {self.card_number}')
        print(f'  - SHABA Number: {self.shaba_number}')
        print(f'  - Account Type: {self.account_type}')
        print(f'  - Balance: {self.balance}')
        print()

class Bank:
    def __init__(self):
        self.users, self.card_numbers, self.shaba_numbers = dict(), dict(), dict()
        self.queue = list()

    def create_user(self, username, phone_number, national_id):
        if username in self.users:
            print(f'Username {username} was taken.')
            return

        user = User(username, phone_number, national_id)
        if user.valid:
            self.users[username] = user

    def card_number_maker(self):
        while 1:
            number = ""
            for i in range(16):
                number += str(randint(0, 9))

            if number not in self.card_numbers:
                return number

    def create_account(self, username, account_type, inital_balance):
        if username not in self.users:
            print(f'Username {username} not found!')
            return

        card_number = self.card_number_maker()
        account = Account(self.users[username], account_type, inital_balance, card_number)
        if account.valid:
            self.card_numbers[card_number] = account
            self.shaba_numbers[account.shaba_number] = account

    def transfer_card_to_card(self, sender_card_number, receiver_card_number, amount):
        if sender_card_number not in self.card_numbers:
            print(f'Sender Card Number {sender_card_number} not found!')
            return
        if receiver_card_number not in self.card_numbers:
            print(f'Receiver Card Number {receiver_card_number} not found!')
            return
        if self.card_numbers[sender_card_number].max_card + amount > 10000000:
            print('You have reached the maximum card to card amount limit')
            return
        if self.card_numbers[sender_card_number].balance - amount < 0:
            print('Not enough money!')
            return

        self.card_numbers[sender_card_number].max_card += amount
        self.card_numbers[sender_card_number].transfer(self.card_numbers[receiver_card_number], amount)
        print('Card-to-Card transfer completed successfully!')
        print('- Transfer amount:', amount, 'Tomans')
        print('- Sender card:', sender_card_number)
        print('- Receiver card:', receiver_card_number)
        print('- Sender balance:', self.card_numbers[sender_card_number].balance, 'Tomans')
        print('- Receiver balance:', self.card_numbers[receiver_card_number].balance, 'Tomans')
        print()

    def init_transfer_shaba(self, sender_shaba_number, receiver_shaba_number, amount):
        if sender_shaba_number not in self.shaba_numbers:
            print(f'Sender SHABA Number {sender_shaba_number} not found!')
            return
        if receiver_shaba_number not in self.shaba_numbers:
            print(f'Receiver SHABA Number {receiver_shaba_number} not found!')
            return
        if self.shaba_numbers[sender_shaba_number].max_shaba + amount > 100000000:
            print('You have reached the maximum SHABA to SHABA amount limit')
            return
        if self.shaba_numbers[sender_shaba_number].balance - amount < 0:
            print('Not enough money!')
            return

        print('SHABA transfer registered and will be competed at the end of the day.')
        self.shaba_numbers[sender_shaba_number].max_shaba += amount
        self.queue.append((sender_shaba_number, receiver_shaba_number, amount))

    def transfer_shaba(self, sender_shaba_number, receiver_shaba_number, amount):
        self.shaba_numbers[sender_shaba_number].transfer(self.shaba_numbers[receiver_shaba_number], amount)
        print('- SHABA transfer completed!')
        print('  - Transfer amount:', amount, 'Tomans')
        print('  - Sender SHABA:', sender_shaba_number)
        print('  - Receiver SHABA:', receiver_shaba_number)
        print('  - Sender balance:', self.shaba_numbers[sender_shaba_number].balance, 'Tomans')
        print('  - Receiver balance:', self.shaba_numbers[receiver_shaba_number].balance, 'Tomans')
        print()

    def check_balance(self, card_number):
        if card_number not in self.card_numbers:
            print(f'Card Number {card_number} not found!')
            return

        print(f'Balance of account {card_number}: {self.card_numbers[card_number].balance} Tomans.')

    def end_day(self):
        print('End of Day:')
        for transfer in self.queue:
            self.transfer_shaba(transfer[0], transfer[1], transfer[2])

        for account in self.card_numbers.values():
            account.max_card, account.max_shaba = 0, 0
            if account.account_type != 'Normal':
                interest = account.balance * (1 - Account.Profit[account.account_type])
                account.balance *= Account.Profit[account.account_type]
                print(f'- Daily interest for {account.username}\'s {account.account_type} account calculated: {interest}')
                print(f'  - New balance for {account.username}\'s {account.account_type} account: {account.balance}')

    def change_account_balance(self, username, card_number, amount):
        if amount >= 0:
            amount *= Account.DepositFine[self.card_numbers[card_number].account_type]
            self.card_numbers[card_number].balance += amount
            print(f'{amount} tomans has been deposited into {card_number}.')

        else:
            amount *= Account.WithdrawFine[self.card_numbers[card_number].account_type]
            if self.card_numbers[card_number].balance - amount < 0:
                print('Not enough money!')
                return

            self.card_numbers[card_number].balance -= amount
            print(f'{amount} tomans has ben withdrawed from {card_number}.')

        self.check_balance(card_number)

    def account_info(self, username):
        if username not in self.users:
            print(f'Username {username} not found!')
            return

        self.users[username].info()

if __name__ == '__main__':
    bank = Bank()
    while 1:
        command = file1.readline().strip()
        command = [line.strip() for line in list(command.split(' ')) if line.strip()]

        if len(command) == 0:
            break

        if command[0] == 'CREATE_USER':
            bank.create_user(command[1], command[2], command[3])
        elif command[0] == 'CREATE_ACCOUNT':
            bank.create_account(command[1], command[2], command[3])
        elif command[0] == 'TRANSFER_CARD_TO_CARD':
            bank.transfer_card_to_card(command[1], command[2], int(command[3]))
        elif command[0] == 'TRANSFER_SHABA':
            bank.init_transfer_shaba(command[1], command[2], int(command[3]))
        elif command[0] == 'CHECK_BALANCE':
            bank.check_balance(command[1])
        elif command[0] == 'END_DAY':
            bank.end_day()
        elif command[0] == 'CHANGE_ACCOUNT_BALANCE':
            bank.change_account_balance(command[1], command[2], int(command[3]))
        else:
            bank.account_info(command[1])

# ---------- End of Main Code ----------

sys.stdout = original_stdout

file1.close()
file2.close()
