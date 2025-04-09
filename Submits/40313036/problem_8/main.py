from random import randint
import regex as re
class User:
    def __init__(self, username, phone_number, national_ID):
        if len(phone_number) != 11 or phone_number[:2] != '09':
            print("wrong phone number")
        elif len(national_ID) != 10:
            print("Wrong national id")
        self.username = username
        self.phone_number = phone_number
        self.national_ID = national_ID
        self.accounts = []

    def get_account(self, cart_number = None, shaba_number = None):
        if cart_number != None:
            for account in self.accounts:
                if account.cart_number == cart_number:
                    return account
        if shaba_number != None:
            for account in self.accounts:
                if account.shaba_number == shaba_number:
                    return account
        return None

    def __str__(self):
        output = f'''User {self.username}\'s information:
- Name: {self.username}
- Phone number: {self.phone_number}
- National ID: {self.national_ID}
- Accounts:'''
        for account in self.accounts:
            output += f'''
- Cart number: {account.cart_number}
- SHABA number: {account.shaba_number}
- Account type: {account.account_type}
- Balance: {account.balance} Tomans\n'''
        return output

class Account:
    def __init__(self, cart_number, shaba_number, account_type, initial_balance):
        self.cart_number = cart_number
        self.shaba_number = shaba_number
        self.account_type = account_type
        self.balance = initial_balance
        self.queue = 0

    def __str__(self):
        return f'Balance of account {self.cart_number}: {self.balance} Tomans'

    def end_day(self):
        if self.account_type == 'Short-term':
            self.balance *= 1.067
        elif self.account_type == 'Long-term':
            self.balance *= 1.167
        self.balance += self.queue

    def pay(self, amount):
        if self.balance+amount >= 0:
            self.balance += amount
            return True
        else:
            return False

bank = Account('bank', 'bank', 'bank', 0)
users = {}
accounts = {}
while True:
    inp = input().split()
    if inp[0] == 'CREATE_USER':
        users[inp[1]] = User(inp[1], inp[2], inp[3])
        print(f'User {inp[1]} registered successfully!')
    elif inp[0] == 'CREATE_ACCOUNT':
        if inp[1] in users:
            cart_number = str(randint(10**16, 10**17-1))
            shaba_number = 'IR'+str(randint(10**24, 10**25-1))
            users[inp[1]].accounts += [Account(cart_number, shaba_number, inp[2], int(inp[3]))]
            accounts[cart_number] = inp[1]
            accounts[shaba_number] = inp[1]
            print(f'{inp[2]} account created for {inp[1]} woth card number {cart_number} and SHABA {shaba_number}')
        else:
            print("User not found!")
    elif inp[0] == 'ACCOUNT_INFO':
            if inp[1] in users:
                print(users[inp[1]])
            else:
                print("User not found!")
    elif inp[0] == 'TRANSFER_CARD_TO_CARD':
        if inp[1] in accounts and inp[2] in accounts:
            account1 = users[accounts[inp[1]]].get_account(cart_number = inp[1])
            account2 = users[accounts[inp[2]]].get_account(cart_number = inp[2])
            amount = int(inp[3])
            if account1.pay(-amount):
                if account1.account_type == 'Short-term':
                    account2.pay(amount*0.99)
                    bank.pay(amount*0.01)
                elif account1.account_type == 'Long-term':
                    account2.pay(amount*0.97)
                    bank.pay(amount*0.03)
                else:
                    account2.pay(amount)
                print(f'''Card-to-card trasfer completed successfully!
- Transfer amount: {amount} Tomans
- Sender card: {account1.cart_number}
- Receiver card: {account2.cart_number}
- Sender balance: {account1.balance}
- Receiver balance {account2.balance}''')
            else:
                print("not enough money!")
        else:
            print('Account not found!')
    elif inp[0] == 'TRANSFER_SHABA':
        if inp[1] in accounts and inp[2] in accounts:
            account1 = users[accounts[inp[1]]].get_account(shaba_number = inp[1])
            account2 = users[accounts[inp[2]]].get_account(shaba_number = inp[2])
            amount = int(inp[3])
            if account1.pay(-amount):
                if account1.account_type == 'Short-term':
                    account2.queue += amount*0.99
                    bank.pay(amount*0.01)
                elif account1.account_type == 'Long-term':
                    account2.queue += amount*0.97
                    bank.pay(amount*0.03)
                else:
                    account2.queue += amount
                print(f'''SHABA trasfer completed successfully!
- Transfer amount: {amount} Tomans
- Sender SHABA: {account1.shaba_number}
- Receiver SHABA: {account2.shaba_number}
- Sender balance: {account1.balance}
- Receiver balance {account2.balance+account2.queue}''')
            else:
                print("not enough money!")
        else:
            print('Account not found!')
    elif inp[0] == 'CHANGE_ACCOUNT_BALANCE':
        if inp[2] in accounts:
            account = users[accounts[inp[1]]].get_account(cart_number = inp[2])
            if account.pay(int(inp[3])):
                print('payment done!')
                print(account)
            else:
                print('not enough money!')
        else:
            print("Account not found!")
    elif inp[0] == 'CHECK_BALANCE':
        if inp[1] in accounts:
            account = users[accounts[inp[1]]].get_account(cart_number = inp[1])
            print(account)
        else:
            print("Account not found!")
    elif inp[0] == 'END_DAY':
        for user in users:
            for account in users[user].accounts:
                account.end_day()