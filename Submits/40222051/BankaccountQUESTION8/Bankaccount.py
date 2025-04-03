import re
class CreatNumber:
    def __init__(self, name, phone_number, national_id, first_amount):
        self.name = name
        self.phone_number = phone_number
        self.national_id = national_id
        self.first_amount = first_amount


class CreatAccount:
    user_accounts_dict = {}  # dictionary for storing accounts by card number
    users_dict = {}  # dictionary to storing user info
    pending_shaba_transfers = []  # list to queue SHABA transfers for end-of-day processing

    # starting points for shaba and card number generation
    BASE_CARD_NUMBER = 6219860000000000
    BASE_SHABA_NUMBER = "IR123456789012345678900000"
    card_counter = 0  # Counter for incrementing card numbers
    shaba_counter = 0  # Counter for incrementing SHABA numbers

    # regex patterns for validation
    CARD_PATTERN = re.compile(r'^\d{16}$')  # 16-digit card number
    SHABA_PATTERN = re.compile(r'^IR\d{24}$')  # IR followed by 24 digits

    def __init__(self, name, account_type, initial_amount):
        self.name = name
        self.account_type = account_type.lower()

        # generation and validation for card number
        self.card_number = str(CreatAccount.BASE_CARD_NUMBER + CreatAccount.card_counter)
        if not CreatAccount.CARD_PATTERN.match(self.card_number):
            raise ValueError(f"Generated card number invalid: {self.card_number}")
        CreatAccount.card_counter += 1

        # generation and validation for SHABA number
        shaba_suffix = str(CreatAccount.shaba_counter).zfill(10)  # Pad to 10 digits
        self.shaba_number = CreatAccount.BASE_SHABA_NUMBER[:-len(shaba_suffix)] + shaba_suffix
        if not CreatAccount.SHABA_PATTERN.match(self.shaba_number):
            raise ValueError(f"Generated SHABA number invalid: {self.shaba_number}")
        CreatAccount.shaba_counter += 1

        # createing user info using existing phone and national id from users_dict
        self.user_info = CreatNumber(name, CreatAccount.users_dict[name].phone_number,
                                     CreatAccount.users_dict[name].national_id, initial_amount)
        self.balance = initial_amount
        CreatAccount.user_accounts_dict[self.card_number] = self  # storing account by card number
        CreatAccount.users_dict[name] = self  # updating users_dict with account object

    def add_profit(self):
        # calculating daily interest for short-term accounts
        if self.account_type == 'shortterm':
            interest = self.balance * 0.00067
            self.balance += interest
            return (f"- Daily interest for {self.name}'s short-term account calculated: {interest:.1f} Tomans\n"
                    f"- New balance for {self.name}'s short-term account: {self.balance:.1f} Tomans")
        return ""  # no interest for normal accounts

    def transform_credit(self, data):
        parts = data.split()
        command = parts[0]

        if command == 'TRANSFER_CARD_TO_CARD':
            sender_card, receiver_card, amount = parts[1], parts[2], float(parts[3])
            # checking if both sender and receiver cards exist
            if sender_card not in self.user_accounts_dict or receiver_card not in self.user_accounts_dict:
                return "Card not found."
            sender = self.user_accounts_dict[sender_card]
            receiver = self.user_accounts_dict[receiver_card]
            if sender.balance >= amount:# checking if the sender has enough balance
                sender.balance -= amount
                receiver.balance += amount
                return (f"Card-to-card transfer completed successfully!\n"
                        f"- Transfer amount: {amount} Tomans\n"
                        f"- Sender card: {sender_card}\n"
                        f"- Receiver card: {receiver_card}\n"
                        f"- Sender balance: {sender.balance} Tomans\n"
                        f"- Receiver balance: {receiver.balance} Tomans")
            return "Insufficient balance."

        elif command == 'TRANSFER_SHABA':
            sender_shaba, receiver_shaba, amount = parts[1], parts[2], float(parts[3])
            # queue SHABA transfer for end-of-day processing
            CreatAccount.pending_shaba_transfers.append((sender_shaba, receiver_shaba, amount))
            return "SHABA transfer registered and will be completed at the end of the day."

        return "Invalid command."

    def check_balance(self):
        # returning current balance for the account
        return f"Balance of account {self.card_number}: {self.balance} Tomans"

    def display_info(self):
        # displaying detailed account information
        return (f"User {self.name}'s information:\n"
                f"- Name: {self.name}\n"
                f"- Phone number: {self.user_info.phone_number}\n"
                f"- National ID: {self.user_info.national_id}\n"
                f"- Card number: {self.card_number}\n"
                f"- SHABA number: {self.shaba_number}\n"
                f"- Account type: {'Short-term' if self.account_type == 'shortterm' else 'Normal'}\n"
                f"- Balance: {self.balance} Tomans")


def process_command(command):
    parts = command.split()
    if not parts:
        return "Please enter a command."

    action = parts[0]

    if action == 'CREATE_USER':
        if len(parts) != 4:
            return "Format: CREATE_USER <name> <phone> <national_id>"
        name, phone, national_id = parts[1], parts[2], parts[3]
        if name in CreatAccount.users_dict:
            return "User already exists."
        # registering user with initial amount of 0
        CreatAccount.users_dict[name] = CreatNumber(name, phone, national_id, 0)
        return f"User {name} registered successfully!"

    if action == 'CREATE_ACCOUNT':
        if len(parts) != 4:  # expects only name, account_type, and initial_amount
            return "Format: CREATE_ACCOUNT <name> <account_type> <initial_amount>"
        name, account_type, initial_amount = parts[1], parts[2], float(parts[3])
        if name not in CreatAccount.users_dict:
            return "User must be created first with CREATE_USER."
        try:
            account = CreatAccount(name, account_type, initial_amount)
            account_type_str = "Normal" if account_type.lower() == "normal" else "Short-term"
            return (f"{account_type_str} account created for {name}:\n"
                    f"- Card number: {account.card_number}\n"
                    f"- SHABA number: {account.shaba_number}\n"
                    f"- Initial balance: {initial_amount} Tomans")
        except ValueError as e:
            return str(e)

    elif action == 'CHECK_BALANCE':
        if len(parts) != 2:
            return "Format: CHECK_BALANCE <card_number>"
        card_number = parts[1]
        if card_number in CreatAccount.user_accounts_dict:
            return CreatAccount.user_accounts_dict[card_number].check_balance()
        return "Card not found."

    elif action in ['TRANSFER_CARD_TO_CARD', 'TRANSFER_SHABA']:
        if len(parts) != 4:
            return "Format: <command> <sender> <receiver> <amount>"
        account = list(CreatAccount.user_accounts_dict.values())[0] if CreatAccount.user_accounts_dict else None
        if not account:
            return "No accounts exist."
        return account.transform_credit(command)

    elif action == 'END_DAY':
        output = "End of day:\n"
        # processing all pending SHABA transfers
        for sender_shaba, receiver_shaba, amount in CreatAccount.pending_shaba_transfers[:]:
            sender_card = next(
                (card for card, acc in CreatAccount.user_accounts_dict.items() if acc.shaba_number == sender_shaba),
                None)
            receiver_card = next(
                (card for card, acc in CreatAccount.user_accounts_dict.items() if acc.shaba_number == receiver_shaba),
                None)
            if sender_card and receiver_card:
                sender = CreatAccount.user_accounts_dict[sender_card]
                receiver = CreatAccount.user_accounts_dict[receiver_card]
                if sender.balance >= amount:
                    sender.balance -= amount
                    receiver.balance += amount
                    output += (f"- SHABA transfer completed!\n"
                               f"- Transfer amount: {amount} Tomans\n"
                               f"- Sender SHABA: {sender_shaba}\n"
                               f"- Receiver SHABA: {receiver_shaba}\n"
                               f"- Sender balance: {sender.balance} Tomans\n"
                               f"- Receiver balance: {receiver.balance} Tomans\n")
        CreatAccount.pending_shaba_transfers.clear()
        # applying interest to short-term accounts
        for account in CreatAccount.user_accounts_dict.values():
            if account.account_type == 'shortterm':
                output += account.add_profit()
        return output.strip()

    elif action == 'ACCOUNT_INFO':
        if len(parts) != 2:
            return "Format: ACCOUNT_INFO <name>"
        name = parts[1]
        if name in CreatAccount.users_dict and isinstance(CreatAccount.users_dict[name], CreatAccount):
            return CreatAccount.users_dict[name].display_info()
        return "Account not found for this user."

    elif action == 'exit':
        return "EXIT"

    return "Unknown command. Try: CREATE_USER, CREATE_ACCOUNT, CHECK_BALANCE, TRANSFER_CARD_TO_CARD, TRANSFER_SHABA, END_DAY, ACCOUNT_INFO"



print(
    "Welcome! Enter commands (e.g., 'CREATE_USER Ali 09123456789 1234567890' or 'CREATE_ACCOUNT Ali Normal 150000') or 'exit' to quit.")
while True:
    command = input("> ").strip()
    if command == 'exit':
        print("Goodbye!")
        break
    response = process_command(command)
    print(response)