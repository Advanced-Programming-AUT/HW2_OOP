from abc import ABC
import re
import random


class User:
    def __init__(self,name,phone,code,balance):
        self.name=name
        self.phone=phone
        self.code = code 
        self.balance = balance
        self.accounts = []

class Account(ABC):
    def __init__(self,intrest,withdrawal_penalty,transfer_penalty,card_number):
        self.intrest= intrest
        self.withdrawal_penalty = withdrawal_penalty
        self.transfer_penalty = transfer_penalty
        self.card_number=str(card_number)
        self.shaba_number="IR"+str(random.randint(10**24,10**25-1))
        self.balance = 100_000
        self.CTC_limit = 0
        self.SHABA_limit = 0
    
    def CTC(self,account,amount ):
        if self.CTC_limit+amount < 10_000_000 and self.balance >= amount:
            self.balance -= amount 
            account.balance += amount 
            self.CTC_limit += amount
            return True
        else:
            return False
    def SHABA(self,account,amount):
        if self.SHABA_limit+amount < 100_000_000 and self.balance >= amount:
            self.balance -= amount 
            account.balance += amount 
            self.SHABA_limit += amount
            return True
        else:
            return False

    def intrest_cal(self):
        self.balance += self.balance * self.intrest



class Normal(Account):
    def __init__(self,card_number):
        super().__init__(0, 0, 0,card_number)
class ShortTerm(Account):
    def __init__(self,card_number):
        super().__init__(0.067, 3, 1,card_number)
class LongTerm(Account):
    def __init__(self,card_number):
        super().__init__(0.167, 5, 3,card_number)



national_id_pattern = r'^\d{10}$'
username_pattern = r'^(?=(.*[a-zA-Z]){3})[\w]+$'
phone_pattern = r'^09\d{9}$'
users = []
shaba_tnxs=[]

while True:
    command = input().split()
    match command[0]:
        case "CREATE_USER":
            if not re.match(national_id_pattern, command[3]):
                print("Invalid national id!")
                break
            if not re.match(username_pattern, command[1]):
                print("Invalid username!")
                break
            if not re.match(phone_pattern, command[2]):
                print("Invalid phone number!")
                break
            new_user = User(command[1],command[2],command[3],0)
            users.append(new_user)
            print(f"New user Created!  *{new_user.name}*{new_user.code}*")
        case "CREATE_ACCOUNT":
            for user in users:
                if user.name == command[1]:
                    match command[2]:
                        case "Normal":
                            new_account = Normal(command[3])
                        case "ShortTerm":
                            new_account = ShortTerm(command[3])
                        case "LongTerm":
                            new_account = LongTerm(command[3])
                    user.accounts.append(new_account)
                    print(f"New Account({new_account.__class__.__name__}) Created!  *{user.name}*{new_account.card_number}*{new_account.shaba_number}*")
        case "TRANSFER_CARD_TO_CARD":
            for user in users:
                for account in user.accounts:
                    if account.card_number == command[1]:
                        sender = account
                    if account.card_number == command[2]:
                        reciver = account

            status = sender.CTC(reciver,int(command[3]))
            if status:
                print(f"transaction complited! *sender:{sender.card_number}*reciver:{reciver.card_number}*amount:{command[3]}")
            else:
                print("Not enoght money!")

        case "TRANSFER_SHABA":
            for user in users:
                for account in user.accounts:
                    if account.shaba_number == command[1]:
                        sender = account
                    if account.shaba_number == command[2]:
                        reciver = account

            status = sender.SHABA(reciver,int(command[3]))
            if status:
                shaba_tnxs.append([sender,reciver,int(command[3]),0])
                print(f"transaction is pending! *sender:{sender.shaba_number}*reciver:{reciver.shaba_number}*amount:{command[3]}")
            else:
                print("Not enoght money!")

        case "CHECK_BALANCE":
            for user in users:
                for account in user.accounts:
                    if account.card_number == command[1]:
                        print(f"*{command[1]}* Balance:{account.balance}")
        
        case "ACCOUNT_INFO":
            for user in users:
                if user.name == command[1]:
                    print(f"User {user.name}'s information:\n\
                        - Name: {user.name}\n\
                        - Phone number: {user.phone}\n\
                        - National ID: {user.code}\n\
                - Accounts:")
                    for account in user.accounts:
                        print(f"\t\t\t- Card number: {account.card_number}\n\
                        - SHABA number: {account.shaba_number}\n\
                        - Account type: {account.__class__.__name__}\n\
                        - Balance: {account.balance} Tomans")
                        
        case "END_DAY":
            print("end of day!")
            for user in users:
                for account in user.accounts:
                    account.intrest_cal()
            for tnx in shaba_tnxs:
                tnx[3]=1