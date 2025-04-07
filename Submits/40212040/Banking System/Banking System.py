import re
all_clients=[]
class Client:
    def __init__(self,name,number,idn,initial_balance=0):
        self._name=name
        self._number=number
        self._idn=idn
        self.balance=initial_balance
        self.account_list=[]
        all_clients.append(self)
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self,number):
        pattern=r'^09[0123456789]{9}$'
        if bool(re.match(pattern,number)) == True:
            self._number=number
        else:
            print('the given number is not valid')
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        flag=0
        pattern=r'^[a-zA-Z0-9_]+$'
        if bool(re.match(pattern,name))==True:
            counter=0
            for t in name:
                if t.isalpha():
                    counter+=1
            if counter >= 3:
                self._name=name
                flag = 1
        if flag == 0:
            print('invalid id number')

incomplete_shaba_transfers=[]
all_accounts=[]
class Account:
    def __init__(self,clt:Client,state,account_num,card_number,initial_money):
        self.client=clt
        self.state=state
        self.num=account_num
        self.card_number=card_number
        self.cash=initial_money
        self.profit=0
        cl.account_list.append(self)
        all_accounts.append(self)

    def end_day_profit(self):
        if self.state == 'longterm':
           self.cash += 0.167 * int(self.cash)
        elif self.state =='shortterm':
            self.cash += 0.067 * int(self.cash)
#the shaba_transfer was not completed before end of day had reached,so daily profit is not calculated upon it
        for it in incomplete_shaba_transfers:
            if it[0] == self:
                if self.cash >= int(it[2]):
                    self.cash -= int(it[2])
                    it[1].cash += int(it[2])
                if self.state == 'longterm':
                    self.cash -= 0.03 * int(it[2])
                if self.state == 'shortterm':
                    self.cash -= 0.01 * int(it[2])
                print(f'completed shaba transfer of {self.num} to {it[1].num}')

    def transfer_card_to_card(self,other,amount):
        if self.cash >= amount:
            self.cash -= amount
            other.cash += amount
            print(f'transferred {amount} Toomans from card {self.client.name} to {other.client.name}')
            if self.state == 'longterm':
                self.cash -= 0.03 * amount
            if self.state == 'shortterm':
                self.cash -= 0.01 * amount
        else:
            print(f"Not enough money in {self.client.name}'s account {self.num}")
    def transfer_shaba(self,other,amount):
        if self.cash < amount:
            print(f"Not enough money in {self.client.name}'s account {self.num}")
        else:
            print(f'registered the transfer of {amount} Toomans from account {self.client.name} to {other.client.name},the process may be completed at the end of the day')
            incomplete_shaba_transfers.append((self,other,amount))

    def withdraw(self,amount):
        if self.cash >= amount :
            self.cash -= amount
            if self.state == 'longterm':
                self.cash -= 0.05 * amount
            if self.state == 'shortterm':
                self.cash -= 0.03 * amount
            self.client.balance += amount
            print(f'withdrew {amount} from account {self.num}')
    def add_cash(self,amount):
        self.cash += amount
        self.client.balance-=amount #assuming that the added money is being paid from client's personal money outside accounts
def card_transfer(amount,sender_card,recipient_card):
    sender_account:Account
    recipient_account:Account
    c1, c2 =0,0 # checking two card numbers' validity
    for item in all_accounts:
        if item.card_number == sender_card:
            sender_account=item
            c1=1
        elif item.card_number == recipient_card:
            recipient_account=item
            c2=1
    if c1 == 1 and c2 == 1:
        sender_account.transfer_card_to_card(recipient_account,amount)
    else:
        print(f'invalid sender/recipient card number')

def shaba_transfer(amount,sender_account_num,recipient_account_num):
    sender_account: Account
    recipient_account: Account
    c1, c2 = 0, 0  # checking two card numbers' validity
    for item in all_accounts:
        if item.num == sender_account_num:
            sender_account = item
            c1 = 1
        elif item.num == recipient_account_num:
            recipient_account = item
            c2 = 1
    if c1 == 1 and c2 == 1:
        sender_account.transfer_shaba(recipient_account,amount)
    else:
        print(f'invalid sender/recipient account number {c1} , {c2}')

x=input()
commands=[]
while(True):
    if not x:
        break
    commands.append(x)
    x=input()

for item in commands:
    y=item.split(' ')
    match(y[0]):
        case 'CREATE_USER':
            Client(y[1],y[2],y[3])
            print('user created')
        case 'CREATE_ACCOUNT':
            fl=0
            for item in all_clients:
                if item.name == y[1]:
                    cl=item
                    fl=1
                    break
            if fl == 1:
                Account(cl,y[2],y[3],y[4],int(y[5]))
            else:
                print(f'no client named {y[1]} found')
        case 'TRANSFER_CARD_TO_CARD':
            card_transfer(int(y[3]),y[1],y[2])
        case 'TRANSFER_SHABA':
            shaba_transfer(int(y[3]),y[1],y[2])
        case 'WITHDRAW_MONEY':
            # input is supposed to be like: WITHDRAW_MONEY <card_number> <amount>
            for item in all_accounts:
                if item.card_number == y[1]:
                    item.withdraw(int(y[2]))
        case 'CHECK_BALANCE':
            for item in all_accounts:
                if item.card_number == y[1]:
                    print(f'balance of this account :{item.num} is {item.cash}')
                    break
        case 'ACCOUNT_INFO':
            for item in all_clients:
                if item.name == y[1]:
                    print(f'name = {item._name}')
                    print(f'phone number = {item._number}')
                    print(f'national id = {item._idn}')
            for t in all_accounts:
                if t.client.name == y[1]:
                    print(f'deposit type = {t.state}')
                    print(f'account number = {t.num}')
                    print(f'card number = {t.card_number}')
        case 'END_DAY':
            print('end of day:', end=' ')
            for items in all_accounts:
                items.end_day_profit()