from user import BankUserClass
from account import BankAccountClass

class BankManagementSystemClass:
    def __init__(self):
        self.users_dictionary_attribute = {}
        self.pending_shaba_transfers_list_attribute = []

    def create_user_method(self, user_name_input, phone_number_input, national_id_input):
        new_user_object = BankUserClass(user_name_input, phone_number_input, national_id_input)
        if not new_user_object.validate_user_information_method():
            return False

        self.users_dictionary_attribute[user_name_input] = new_user_object
        return True

    def create_account_method(self, user_name_input, account_type_input, card_number_input):
        if user_name_input not in self.users_dictionary_attribute:
            return False

        user_object = self.users_dictionary_attribute[user_name_input]
        new_account_object = BankAccountClass(user_object, account_type_input, card_number_input)
        user_object.add_account_method(new_account_object)
        return True

    def transfer_card_to_card_method(self, sender_card_input, receiver_card_input, amount_input):
        sender_account = None
        receiver_account = None

        for user_item in self.users_dictionary_attribute.values():
            for account_item in user_item.accounts_list_attribute:
                if account_item.card_number_attribute == sender_card_input:
                    sender_account = account_item
                if account_item.card_number_attribute == receiver_card_input:
                    receiver_account = account_item

        if not sender_account or not receiver_account:
            return False

        if sender_account.user_attribute.transferred_amount_card_today_attribute + amount_input > sender_account.user_attribute.daily_transfer_limit_card_attribute:
            return False

        transferred_amount = sender_account.transfer_method(amount_input)
        if transferred_amount > 0:
            receiver_account.deposit_method(transferred_amount)
            sender_account.user_attribute.transferred_amount_card_today_attribute += amount_input
            return True
        return False

    def transfer_shaba_method(self, sender_shaba_input, receiver_shaba_input, amount_input):
        sender_account = None
        receiver_account = None

        for user_item in self.users_dictionary_attribute.values():
            for account_item in user_item.accounts_list_attribute:
                if account_item.shaba_number_attribute == sender_shaba_input:
                    sender_account = account_item
                if account_item.shaba_number_attribute == receiver_shaba_input:
                    receiver_account = account_item

        if not sender_account or not receiver_account:
            return False

        if sender_account.user_attribute.transferred_amount_shaba_today_attribute + amount_input > sender_account.user_attribute.daily_transfer_limit_shaba_attribute:
            return False

        self.pending_shaba_transfers_list_attribute.append({
            'sender_account': sender_account,
            'receiver_account': receiver_account,
            'amount': amount_input
        })
        sender_account.user_attribute.transferred_amount_shaba_today_attribute += amount_input
        return True

    def process_end_of_day_method(self):
        result_string = ""
        for transfer_item in self.pending_shaba_transfers_list_attribute:
            transferred_amount = transfer_item['sender_account'].transfer_method(transfer_item['amount'])
            if transferred_amount > 0:
                transfer_item['receiver_account'].deposit_method(transferred_amount)
                result_string += "SHABA transfer completed!\n"
                result_string += "- Transfer amount: " + str(transfer_item['amount']) + " Tomans\n"
                result_string += "- Sender SHABA: " + transfer_item['sender_account'].shaba_number_attribute + "\n"
                result_string += "- Receiver SHABA: " + transfer_item['receiver_account'].shaba_number_attribute + "\n"

        self.pending_shaba_transfers_list_attribute = []

        for user_item in self.users_dictionary_attribute.values():
            for account_item in user_item.accounts_list_attribute:
                interest_amount = account_item.calculate_daily_interest_method()
                if interest_amount > 0:
                    result_string += "- Daily interest for " + user_item.user_name_attribute + "'s " + account_item.account_type_attribute + " account calculated: " + str(
                        interest_amount) + " Tomans\n"

        for user_item in self.users_dictionary_attribute.values():
            user_item.transferred_amount_card_today_attribute = 0
            user_item.transferred_amount_shaba_today_attribute = 0

        return result_string

    def check_balance_method(self, card_number_input):
        for user_item in self.users_dictionary_attribute.values():
            for account_item in user_item.accounts_list_attribute:
                if account_item.card_number_attribute == card_number_input:
                    return account_item.get_balance_method()
        return None

    def get_account_info_method(self, user_name_input):
        if user_name_input not in self.users_dictionary_attribute:
            return None
        return self.users_dictionary_attribute[user_name_input].get_user_info_method()