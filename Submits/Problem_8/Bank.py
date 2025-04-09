import random
import re
from abc import ABC, abstractmethod


class Client:
    users = {} #name : client
    users_card_access = {} #card_number : card
    users_shaba_access = {} #shaba : card
    def __init__(self, name, phone_number, national_code):
        self.__name = name
        self.__phone_number = phone_number
        self.__national_code = national_code
        self.__accounts = []
        Client.users[name] = self
        print(f"User {self.name} registered successfully!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @staticmethod
    def name_search(name):
        for client in Client.users.values():
            if name == client.__name:
                return True
        return False

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def national_code(self):
        return self.__national_code

    @national_code.setter
    def national_code(self, national_code):
        self.__national_code = national_code

    def add_account(self, account):
        self.__accounts.append(account)

    @staticmethod
    def card_shaba_handler(card, card_number, shaba):
        Client.users_card_access[card_number] = card
        Client.users_shaba_access[shaba] = card

    def user_info(self):
        print(f"User {self.name}'s information: ")
        print(f"- Name: {self.name}\n- Phone number: {self.phone_number}\n"
              f"- National ID: {self.national_code}\nAccounts:")
        for account in self.accounts:
            print(f"- Card number: {account.card_number}\n- Shaba number: {account.shaba}\n"
                  f"- Account type: {account.account_type}\n- Balance: {account.balance} Rials")
class Account(ABC):
    def __init__(self, name):
        self.__name = name
        self.__card_number = f"60379988{random.randint(pow(10, 7), pow(10, 8) - 1)}9"


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def card_number(self):
        return self.__card_number

    @abstractmethod
    def transfer(self, other, amount):
        pass

    @abstractmethod
    def change_balance(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class Normal(Account):
    def __init__(self, name, balance):
        super().__init__(name)
        self.__shaba = f"IR010101{random.randint(pow(10, 10), pow(10, 19) - 1):0=18}"
        print(f"Normal account created for {name} with card number {self.card_number} and "
              f"shaba {self.__shaba}")
        self.account_type = "Normal"
        self.__balance = balance
        Client.users[name].add_account(self)
        Client.card_shaba_handler(self, self.card_number, self.shaba)

    @property
    def shaba(self):
        return self.__shaba

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def transfer(self, other, amount):
        pass

    def change_balance(self, amount):
        self.__balance += amount
        self.check_balance()

    def withdraw(self, amount):
        pass

    def check_balance(self):
        print(f"Balance of account {self.card_number}: {self.balance} Tomans")


class LongTerm(Account):
    def __init__(self, name, balance):
        super().__init__(name)
        self.__shaba = f"IR010102{random.randint(pow(10, 10), pow(10, 19) - 1):0=18}"
        print(f"Long-term account created for {name} with card number {self.card_number} and "
              f"shaba {self.__shaba}")
        self.account_type = "Long-term"
        self.__balance = balance
        Client.users[name].add_account(self)
        Client.card_shaba_handler(self, self.__card_number, self.__shaba)

    @property
    def shaba(self):
        return self.__shaba

    def transfer(self, other, amount):
        pass

    def change_balance(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        pass

    def check_balance(self):
        pass


class ShortTerm(Account):
    def __init__(self, name, balance):
        super().__init__(name)
        self.__shaba = f"IR010103{random.randint(pow(10, 10), pow(10, 19) - 1):0=18}"
        print(f"Short-term account created for {name} with card number {self.card_number} and "
              f"shaba {self.__shaba}")
        self.account_type = "Short-term"
        self.__balance = balance
        Client.users[name].add_account(self)
        Client.card_shaba_handler(self, self.__card_number, self.__shaba)

    @property
    def shaba(self):
        return self.__shaba

    def transfer(self, other, amount):
        pass

    def change_balance(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def check_balance(self):
        pass


def validator(value, value_type):
    match value_type:
        case 'name':
            name_pattern = r'^[a-zA-Z0-9_]'
            if not (re.match(name_pattern, value) and len(value) > 3):
                print('Invalid Name')
                return None
            return value
        case 'phone':
            number_pattern = r'^[0][9]+[0-9]{9}'
            if not re.match(number_pattern, value):
                print('Invalid Phone Number')
                return None
            return int(value)
        case 'code':
            code_pattern = r'^[0-9]{10}'
            if not re.match(code_pattern, value):
                print('Invalid National Code')
                return None
            return int(value)


def main():
    print("welcome to bank management system")
    main_user = Client("aliali", '09123456789', '1234567890')
    main_card = Normal('aliali', 100)
    while True:
        print("choose one\n1. Create user\n2. Create account\n3. Change account balance\n4. Transfer card to card\n"
              "5. Transfer shaba\n6. Check balance\n7. End day\n8. Account info\n9. Exit")
        command = input(">> ")
        match command:
            case '1':
                name = validator(input("Enter your name: "), 'name')
                phone_number = validator(input("Enter your phone number: "), 'phone')
                national_code = validator(input("Enter your national code: "), 'code')
                if all([name, phone_number, national_code]):
                    Client(name, phone_number, national_code)
            case '2':
                for client in Client.users.values():
                    print(client.name)
                name = input("choose one of the names: ")
                if Client.name_search(name):
                    account_type = input("Enter your account type: (normal, short-term, long-term)")
                    try:
                        balance = int(input("Enter initial balance: "))
                        match account_type:
                            case 'normal':
                                normal_account = Normal(name, balance)
                            case 'short-term':
                                short_account = ShortTerm(name, balance)
                            case 'long-term':
                                long_account = LongTerm(name, balance)
                            case '_':
                                print("type is not valid")
                    except ValueError:
                        print("Invalid Balance")
                else:
                    print("Invalid Name")
            case '3':
                user_name = input("Enter your name: ")
                card_number = input("Enter your card number: ")
                amount = int(input("Enter transaction amount:(can be positive or negative) "))
                card = Client.users_card_access.get(card_number, None)
                if not card:
                    print("card does not exist")
                else :
                    card.change_balance(amount)





if __name__ == '__main__':
    main()
