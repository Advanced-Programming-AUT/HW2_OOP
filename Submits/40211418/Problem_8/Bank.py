import re
import random
phone_pattern = r'^09\d{9}$'
name_pattern = r'^[A-Za-z_]{3,}$'
id_pattern = r'^\d{10}$'


class User:
    def __init__(self, name, phone, ID):
        if re.match(name_pattern, name): self.__name = name
        if re.match(phone_pattern, phone) : self.phone = phone
        if re.match(id_pattern, ID) : self.__id = ID
        self.__accounts = []

    @property
    def name(self):
        return self.__name
    
    @property
    def accounts(self):
        return self.__accounts
    
    @property
    def id(self):
        return self.__id
    

class Account:
    
    def __init__(self, user, balance,account_type):
        self.user = user
        self.__balance = int(balance)
        self.type = account_type
        self.card_id = ''.join(str(random.randint(0,9)) for _ in range(16))
        self.shaba = 'IR' + (''.join(str(random.randint(0,9)) for _ in range(24)))

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, val):
        self.__balance = val
    

class Bank:
    __users = []
    __accounts = []
    shaba_queue = []

    @classmethod
    def sign_up(cls, name, phone, ID):
        cls.__users.append(User(name, phone, ID))
        return f'user {name} registered successfully'

    @classmethod
    def creat_account(cls, user_name, account_type, balance):
        for user in cls.__users:
            if user.name == user_name:
                ac = Account(user, balance, account_type)
                user.accounts.append(ac)
                cls.__accounts.append(ac)
                return f'{ac.type} account created for {user_name} with card number: {ac.card_id} and shaba {ac.shaba}'

    @classmethod
    def transfer_card(cls, sender_id, reciver_id, amount):
        amount = int(amount)
        for ac in cls.__accounts:
            if ac.card_id == sender_id:
                sender = ac
            elif ac.card_id == reciver_id:
                reciver = ac
        if not(sender or reciver):
            return 'card not exist'

        match sender.type:
            case 'Normal':
                fee = 0
            case 'ShortTerm':
                fee = int(amount * 0.01)
            case 'LongTerm':
                fee = int(amount * 0.03)
        final_amount = fee + amount
        if sender.balance >= final_amount:
            sender.balance -= final_amount
            reciver.balance += amount

            return f'Card-to-card transfer completed successfully!\n'\
                    f'- Transfer amount: {amount} Tomans\n'\
                    f'- Sender card: {sender.card_id}\n'\
                    f'- Receiver card: {reciver.card_id}\n'\
                    f'- Sender balance: {sender.balance} Tomans\n'\
                    f'- Receiver balance: {reciver.balance} Tomans'
        else:
            return 'Not enough balance'
        
    @classmethod
    def transfer_shaba(cls, sender_id, reciver_id, amount):
        amount = int(amount)
        for ac in cls.__accounts:
            if ac.shaba == sender_id:
                sender = ac
            elif ac.shaba == reciver_id:
                reciver = ac
        if not(sender or reciver):
            return 'card not exist'

        match sender.type:
            case 'Normal':
                fee = 0
            case 'shortTerm':
                fee = int(amount * 0.01)
            case 'longTerm':
                fee = int(amount * 0.03)
        final_amount = fee + amount
        if sender.balance >= final_amount:
            sender.balance -= final_amount
            reciver.balance += amount

            return f'Saba-to-shaba transfer completed successfully!\n'\
                    f'- Transfer amount: {amount} Tomans\n'\
                    f'- Sender shaba: {sender.shaba}\n'\
                    f'- Receiver shaba: {reciver.shaba}\n'\
                    f'- Sender balance: {sender.balance} Tomans\n'\
                    f'- Receiver balance: {reciver.balance} Tomans'
        else:
            return 'Not enough balance'

    @classmethod
    def add_balance(cls, user_name, card_id, amount):
        amount = int(amount)
        for user in cls.__users:
            if user.name == user_name:
                for ac in user.accounts:
                    if ac.card_id == card_id:
                        ac.balance += amount
                        return f'{amount} Tomans added to balance successfully\n'\
                                f'current balance: {ac.balance}'
        return 'error happend'
            
    @classmethod
    def withdraw(cls, user_name, card_id, amount):
        amount = int(amount)
        for user in cls.__users:
            if user.name == user_name:
                for ac in user.accounts:
                    if ac.card_id == card_id:
                        if ac.type == 'Normal':
                            fee = 0
                        elif ac.type == 'ShortTerm':
                            fee = int(amount * 0.03)
                        elif ac.type == 'Longterm':
                            fee = int(amount * 0.05)
                        final_amount = amount + fee
                        ac.balance -= final_amount
                        return f'Withdraw {amount} Tomans successfully\n'\
                                f'current balance: {ac.balance}'
                    
        return 'error happend'
    
    @classmethod
    def get_info(cls, user_name):
        out = 'account info:\n'
        for user in cls.__users:
            if user.name == user_name:
                out += f'Name: {user.name}\n'\
                        f'Phone number: {user.phone}\n'\
                        f'National ID: {user.id}\n'\
                        f'Accounts: '
                for ac in user.accounts:
                    out += f'card number: {ac.card_id}\n'\
                            f'SHABA number: {ac.shaba}\n'\
                            f'Account type: {ac.type}\n'\
                            f'Balance: {ac.balance}'
                return out.strip()
        return 'error happend'
    
    @classmethod
    def get_balance(cls, card_id):
        for ac in cls.__accounts:
            if ac.card_id == card_id:
                return f'balance of account {ac.card_id}: {ac.balance}'
        return 'error happend'
    
    @classmethod
    def end_day(cls):
        out = 'End of the day\n'
        for details in cls.shaba_queue:
            out += cls.transfer_shaba(*details) + '\n'
        for user in cls.__users:
            for ac in user.accounts:
                if ac.type == 'ShortTerm':
                    profit = int(ac.balance * 0.00067)
                    ac.balance += profit
                    out += f'Daily interest for {user.name}\'s short-term account calculated: {profit} Tomans'
                elif ac.type == 'LongTerm':
                    profit = int(ac.balance * 0.00167 / 100)
                    ac.balance += profit
                    out += f'Daily interest for {user.name}\'s long-term account calculated: {profit} Tomans'
        return out
        

def main():
    while True:
        com = input().split()
        match com[0]:
            case 'CREATE_USER':
                print(Bank.sign_up(*com[1:]))
            case 'CREATE_ACCOUNT':
                print(Bank.creat_account(*com[1:]))
            case 'TRANSFER_CARD_TO_CARD':
                print(Bank.transfer_card(*com[1:]))
            case 'TRANSFER_SHABA':
                Bank.shaba_queue.append(com[1:])
                print('SHABA transfer registered and will be completed at the end of the day.')
            case 'CHECK_BALANCE':
                print(Bank.get_balance(com[1]))
            case 'ACCOUNT_INFO':
                print(Bank.get_info(com[1]))
            case 'END_DAY':
                print(Bank.end_day())
        
if __name__ == '__main__':
    main()