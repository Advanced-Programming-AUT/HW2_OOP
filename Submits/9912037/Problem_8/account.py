import random

class BankAccountClass:
    def __init__(self, user_object_input, account_type_input, card_number_input):
        self.user_attribute = user_object_input
        self.account_type_attribute = account_type_input
        self.card_number_attribute = card_number_input
        self.shaba_number_attribute = self.generate_shaba_number_method()
        self.balance_attribute = 1000000
        self.daily_interest_rate_attribute = 0
        self.set_interest_rate_method()

    def generate_shaba_number_method(self):
        shaba_prefix = "IR"
        random_numbers = ""
        id =  self.user_attribute.national_id_attribute
        return shaba_prefix + str(id)*2 + str(id)[0:4]
        # for i in range(22):
        #     random_numbers += str(random.randint(0, 9))
        # return shaba_prefix + random_numbers

    def set_interest_rate_method(self):
        if self.account_type_attribute == "ShortTerm":
            self.daily_interest_rate_attribute = 0.00016607
        elif self.account_type_attribute == "LongTerm":
            self.daily_interest_rate_attribute = 0.00044007
        else:
            self.daily_interest_rate_attribute = 0

    def deposit_method(self, amount_input):
        self.balance_attribute += amount_input

    def withdraw_method(self, amount_input):
        penalty_amount = 0
        if self.account_type_attribute == "ShortTerm":
            penalty_amount = amount_input * 0.03
        elif self.account_type_attribute == "LongTerm":
            penalty_amount = amount_input * 0.05

        total_amount = amount_input + penalty_amount
        if self.balance_attribute >= total_amount:
            self.balance_attribute -= total_amount
            return True
        return False

    def transfer_method(self, amount_input):
        penalty_amount = 0
        if self.account_type_attribute == "ShortTerm":
            penalty_amount = amount_input * 0.01
        elif self.account_type_attribute == "LongTerm":
            penalty_amount = amount_input * 0.03

        total_amount = amount_input + penalty_amount
        if self.balance_attribute >= total_amount:
            self.balance_attribute -= total_amount
            return amount_input
        return 0

    def calculate_daily_interest_method(self):
        interest_amount = self.balance_attribute * self.daily_interest_rate_attribute
        self.balance_attribute += interest_amount
        return interest_amount

    def get_balance_method(self):
        return self.balance_attribute