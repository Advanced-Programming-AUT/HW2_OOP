import re
import random
pattern_user_name = r"^\w*[a-zA-Z]{3,}\w*$"
pattern_phon_number = r"^09\d{9}$"
pattern_National_ID = r"^\d{10}$"

list_of_user_account = []
list_of_all_bank_account = []
list_of_transfer_shaba_endday = []
class UserAccount:
    def __init__(self, user_name, phon_number, National_ID):
        self.user_name = user_name
        self.phon_number = phon_number
        self.National_ID = National_ID
        print(f"User {self.user_name} registered successfully!")
        list_of_user_account.append(self)
        
class BankAccount:
    def __init__(self, user_name, card_number):
        self.user_name = user_name
        self.card_number = str(card_number)
        self.balance = 0
        self.type_account = "Normal"
        number_random = random.randint(100000000000000000000000, 999999999999999999999999)
        self.shaba_number = f"IR{number_random}"
        list_of_all_bank_account.append(self)
        print(f"Normal account created by {self.user_name} with card number {self.card_number} SHABA number {self.shaba_number}")
    def withdraw(self, amount_money):
        if self.balance >= int(amount_money):
            self.balance -= int(amount_money)
            print(f"An amount {amount_money} Tomans has been withdraw from {self.card_number}")
        else:
            print(f"An account {self.card_number} hasn't enough money!")
    def desposit(self, amount_money):
        self.balance += int(amount_money)
        print(f"An amount {amount_money} Tomans has been desposit from {self.card_number}")
    def transfer_card_to_card(self, reciever_account, amount_money):
        if int(amount_money) <= self.balance and int(amount_money) <= 10000000:
            self.balance -= int(amount_money)
            reciever_account.balance += int(amount_money)
            print("Card_to_card transfer completed successfully!")
            print(f"- Transfer amount: {amount_money} Tomans\n- Sender card: {self.card_number}")
            print(f"- Reciever card: {reciever_account.card_number}")
            print(f"- Sender balance: {self.balance} Tomans\n- Reciever balance: {reciever_account.balance} Tomans")
        else:
            print("Account has not enough money or amount-money more than allowed limit")
    def transfer_shaba(self, reciever_account, amount_money):
        if int(amount_money) <= self.balance and int(amount_money) <= 100000000:
            list_of_transfer_shaba_endday.append([self, reciever_account, amount_money])
            print("SHABA transfer registered and will be completed at the end of day.")
        else:
            print("Account has not enough money or amount-money more than allowed limit")
    def transfer_shaba_endday(self, reciever_account, amount_money):
        self.balance -= int(amount_money)
        reciever_account.balance += int(amount_money)
        print("- SHABA transfer completed!")
        print(f" - Transfer amount: {amount_money} Tomans\n - Sender SHABA: {self.shaba_number}")
        print(f"- Reciever SHABA: {reciever_account.shaba_number}")
        print(f"- Sender balance: {self.balance} Tomans\n- Reciever balance: {reciever_account.balance} Tomans")
        
class ShortTerm(BankAccount):
    def __init__(self, user_name, card_number):
        self.user_name = user_name
        self.card_number = str(card_number)
        self.balance = 0
        self.type_account = "Short-term"
        number_random = random.randint(100000000000000000000000, 999999999999999999999999)
        self.shaba_number = f"IR{number_random}"
        list_of_all_bank_account.append(self)
        print(f"Short-term account created by {self.user_name} with card number {self.card_number} SHABA number {self.shaba_number}")
    def withdraw(self, amount_money):
        if self.balance >= int(amount_money):
            self.balance -= int(amount_money)
            self.balance -= int(amount_money) * 0.03 # مبلغ جریمه
            print(f"An amount {amount_money} Tomans has been withdraw from {self.card_number}")
        else:
            print(f"An account {self.card_number} hasn't enough money!")
    def daily_profit(self):
        self.balance *= 1.00067
        print(f"- Daily interest for {self.user_name}'s short-term account calculated: {self.balance * 0.00067} Tomans")
        print(f" - New balance for {self.user_name}'s short-term account: {self.balance} Tomans")
    def transfer_card_to_card(self, reciever_account, amount_money):
        if int(amount_money) <= self.balance and int(amount_money) <= 10000000:
            self.balance -= int(amount_money)
            reciever_account.balance += int(amount_money)
            self.balance -= int(amount_money) * 0.01
            print("Card_to_card transfer completed successfully!")
            print(f"- Transfer amount: {amount_money} Tomans\n- Sender card: {self.card_number}")
            print(f"- Reciever card: {reciever_account.card_number}")
            print(f"- Sender balance: {self.balance} Tomans\n- Reciever balance: {reciever_account.balance} Tomans")
        else:
            print("Account has not enough money or amount-money more than allowed limit")
    def transfer_shaba_endday(self, reciever_account, amount_money):
        self.balance -= int(amount_money)
        self.balance -= int(amount_money) * 0.01
        reciever_account.balance += int(amount_money)
        print("- SHABA transfer completed!")
        print(f" - Transfer amount: {amount_money} Tomans\n - Sender SHABA: {self.shaba_number}")
        print(f" - Reciever SHABA: {reciever_account.shaba_number}")
        print(f" - Sender balance: {self.balance} Tomans\n - Reciever balance: {reciever_account.balance} Tomans")
        
class LongTerm(BankAccount):
    def __init__(self, user_name, card_number):
        self.user_name = user_name
        self.card_number = str(card_number)
        self.balance = 0
        self.type_account = "Long-term"
        number_random = random.randint(100000000000000000000000, 999999999999999999999999)
        self.shaba_number = f"IR{number_random}"
        list_of_all_bank_account.append(self)
        print(f"Long-term account created by {self.user_name} with card number {self.card_number} SHABA number {self.shaba_number}")
    def withdraw(self, amount_money):
        if self.balance >= int(amount_money):
            self.balance -= int(amount_money)
            self.balance -= int(amount_money) * 0.05 # مبلغ جریمه
            print(f"An amount {amount_money} Tomans has been withdraw from {self.card_number}")
        else:
            print(f"An account {self.card_number} hasn't enough money!")
    def daily_profit(self):
        self.balance *= 1.00167
        print(f"- Daily interest for {self.user_name}'s long-term account calculated: {self.balance * 0.00167} Tomans")
        print(f" - New balance for {self.user_name}'s long-term account: {self.balance} Tomans")
    def transfer_card_to_card(self, reciever_account, amount_money):
        if int(amount_money) <= self.balance and int(amount_money) <= 100000000:
            self.balance -= int(amount_money)
            reciever_account.balance += int(amount_money)
            self.balance -= int(amount_money) * 0.03
            print("Card_to_card transfer completed successfully!")
            print(f"- Transfer amount: {amount_money} Tomans\n- Sender card: {self.card_number}")
            print(f"- Reciever card: {reciever_account.card_number}")
            print(f"- Sender balance: {self.balance} Tomans\n- Reciever balance: {reciever_account.balance} Tomans")
        else:
            print("Account has not enough money or amount-money more than allowed limit")
    def transfer_shaba_endday(self, reciever_account, amount_money):
        self.balance -= int(amount_money)
        self.balance -= int(amount_money) * 0.03
        reciever_account.balance += int(amount_money)
        print("- SHABA transfer completed!")
        print(f" - Transfer amount: {amount_money} Tomans\n - Sender SHABA: {self.shaba_number}")
        print(f" - Reciever SHABA: {reciever_account.shaba_number}")
        print(f" - Sender balance: {self.balance} Tomans\n - Reciever balance: {reciever_account.balance} Tomans")
        
order_count = int(input())

for _ in range(order_count):
    order_list = input().split()
    if order_list[0] == "CREATE_USER":
        correctly_format = 1
        if not re.match(pattern_user_name, order_list[1]):
            print("The format of user_name is not correct")
            correctly_format = 0
        if not re.match(pattern_phon_number, order_list[2]):
            print("The format of phon_number is not correct")
            correctly_format = 0
        if not re.match(pattern_National_ID, order_list[3]):
            print("The format of National_ID is not correct")
            correctly_format = 0
        if correctly_format:
            user_account = UserAccount(order_list[1], order_list[2], order_list[3])
       
    if order_list[0] == "CREATE_ACCOUNT":
        if order_list[2] == "Normal":
            bank_account = BankAccount(order_list[1], order_list[3])
        if order_list[2] == "Short-term":
            bank_account =ShortTerm(order_list[1], order_list[3])
        if order_list[2] == "Long-term":
            bank_account = LongTerm(order_list[1], order_list[3])
            
    if order_list[0] == "DESPOSIT":
        for account in list_of_all_bank_account:
            if account.card_number == order_list[1]:
                account_desposit = account
                break
        account_desposit.desposit(order_list[2]) 
        
    if order_list[0] == "TRANSFER_CARD_TO_CARD":
        for account in list_of_all_bank_account:
            if account.card_number == order_list[1]:
                account_sender = account
                break
        for account in list_of_all_bank_account:
            if account.card_number == order_list[2]:
                account_reciever = account
                break
        account_sender.transfer_card_to_card(account_reciever, order_list[3])
        
    if order_list[0] == "TRANSFER_SHABA":
        for account in list_of_all_bank_account:
            if account.shaba_number == order_list[1]:
                account_sender = account
                break
        for account in list_of_all_bank_account:
            if account.shaba_number == order_list[2]:
                account_reciever = account
                break
        account_sender.transfer_shaba(account_reciever, order_list[3])
            
    if order_list[0] == "END_DAY":
        print("End of day:")
        for transfer_endday in list_of_transfer_shaba_endday:
            transfer_endday[0].transfer_shaba_endday(transfer_endday[1], transfer_endday[2])
        for account in list_of_all_bank_account:
            if account.type_account != "Normal":
                account.daily_profit()
                
    if order_list[0] == "CHECK_BALANCE":
        for account in list_of_all_bank_account:
            if account.card_number == order_list[1]:
                account_check_balance = account
                break
        print(f"Balance of account {account_check_balance.card_number}: {account_check_balance.balance} Tomans")
                
    if order_list[0] == "ACCOUNT_INFO":
        for user in list_of_user_account:
            if user.user_name == order_list[1]:
                user_check_info = user
                break
        print(f"User {user_check_info.user_name}'s information:")
        print(f"- Name: {user_check_info.user_name}")
        print(f"- Phon_number: {user_check_info.phon_number}")
        print(f"- National ID: {user_check_info.National_ID}")
        print("Accounts:")
        for account in list_of_all_bank_account:
            if account.user_name == user.user_name:
                print(f" - Card number: {account.card_number}")
                print(f" - SHABA number: {account.shaba_number}")
                print(f" - Account type: {account.type_account}")
                print(f" - Balance: {account.balance}\n")
                