import re

class Account:
    def __init___(self , type , balance):
        self.type = type
        self.balance = balance
        self.card_number = ...
        self.shaba_number = ...
        ...
    

    def sood(self):
        if self.type == 'short':
            return self.balance * 0.00067
        elif self.type == 'long':
            return self.balance * 0.00167
        else:
            return 0
        
    def bardasht(self , amount):
        if self.type == 'short':
            jarime = amount *0.03
        elif self.type == 'long':
            jarime = amount * 0.05
        else:
            jarime = 0
        t = amount+ jarime

        if self.balance >= t:
            self.balance -= t
            return 1
        return 0
    
    def seporde (self ,  amount):
        self.balance += amount
    
    def j_tranfer(self , amount):
        if self.type == "short":
            return amount * 0.01
        elif self.type == "long":
            return amount * 0.03
        else: return 0



class User:
    def __init__(self , username , phone_number , nID):
        self.username = username
        self.phone_number =phone_number
        self.nID = nID
        self.accounts = []

    def create_acc (self , type , balance):
        acc = Account(type , balance)
        self.accounts.append(acc)
        print(f'hesab ijad shod \n type: {acc.type}, card: {acc.card_number} , shaba={acc.shaba_number}')



class ForControl:
    def __init__(self):
        self.users = dict()
    def checkUsername(self , username):
        a = re.match(r"[a-zA-Z0-9_]{3,}" , username)
        return a
    def checkphone(self , phone_number):
        a = re.match(r"09\d{9}" , phone_number)
        return a
    def checknID(self , nID):
        a = re.match(r"\d{10}" , nID)
        return a
    def creatingUser(self , username , phone_number , nID):
        if username in self.users:
            print('your account already exists dude!') ; return
        if not self.checkUsername(username):
            print('invalid!') ; return
        if not self.checkphone(phone_number):
            print('invalid!') ; return
        if not self.checknID(nID):
            print('invalid!') ; return
        self.users[username] = User(username , phone_number , nID)
        print('done')



    def create_acc(self , username , type , balance):
        if username not in self.users:
            print('register first') ; return
        self.users[username].create_acc(type , balance)
    def update_balance(self , username , card_number , amount):
        if username not in self.users:
            print('!!') ; return
        