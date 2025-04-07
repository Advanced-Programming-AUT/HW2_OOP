import re

class BankUserClass:
    def __init__(self, user_name_input, phone_number_input, national_id_input):
        self.user_name_attribute = user_name_input
        self.phone_number_attribute = phone_number_input
        self.national_id_attribute = national_id_input
        self.accounts_list_attribute = []
        self.daily_transfer_limit_card_attribute = 10000000
        self.daily_transfer_limit_shaba_attribute = 100000000
        self.transferred_amount_card_today_attribute = 0
        self.transferred_amount_shaba_today_attribute = 0

    def validate_user_information_method(self):
        name_pattern = re.compile(r'^[a-zA-Z0-9_]{3,}$')
        phone_pattern = re.compile(r'^09\d{9}$')
        national_id_pattern = re.compile(r'^\d{10}$')

        name_valid = False
        if name_pattern.match(self.user_name_attribute):
            name_valid = True

        phone_valid = False
        if phone_pattern.match(self.phone_number_attribute):
            phone_valid = True

        national_id_valid = False
        if national_id_pattern.match(self.national_id_attribute):
            national_id_valid = True

        return name_valid and phone_valid and national_id_valid

    def add_account_method(self, account_object):
        self.accounts_list_attribute.append(account_object)

    def get_user_info_method(self):
        info_string = ""
        info_string += "Name: " + self.user_name_attribute + "\n"
        info_string += "Phone number: " + self.phone_number_attribute + "\n"
        info_string += "National ID: " + self.national_id_attribute + "\n"
        info_string += "Accounts:\n"
        for account_item in self.accounts_list_attribute:
            info_string += "  - Card number: " + account_item.card_number_attribute + "\n"
            info_string += "    SHABA number: " + account_item.shaba_number_attribute + "\n"
            info_string += "    Account type: " + account_item.account_type_attribute + "\n"
            info_string += "    Balance: " + str(account_item.balance_attribute) + " Tomans\n"
        return info_string