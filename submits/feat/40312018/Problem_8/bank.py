import random
import re

def generate_card_number():
    return '621986' + ''.join([str(random.randint(0, 9)) for _ in range(10)])

def generate_shaba_number():
    return 'IR' + ''.join([str(random.randint(0, 9)) for _ in range(24)])

class Account:
    def __init__(self, acc_type, balance):
        self.acc_type = acc_type
        self.balance = float(balance)
        self.card_number = generate_card_number()
        self.shaba_number = generate_shaba_number()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        fee = 0
        if self.acc_type == "ShortTerm":
            fee = 0.03 * amount
        elif self.acc_type == "LongTerm":
            fee = 0.05 * amount
        total = amount + fee
        if self.balance >= total:
            self.balance -= total
            return True, fee
        return False, fee

    def transfer_fee(self, amount):
        fee = 0
        if self.acc_type == "ShortTerm":
            fee = 0.01 * amount
        elif self.acc_type == "LongTerm":
            fee = 0.03 * amount
        return fee

    def apply_interest(self):
        interest = 0
        if self.acc_type == "ShortTerm":
            interest = self.balance * 0.00067  # 0.067%
        elif self.acc_type == "LongTerm":
            interest = self.balance * 0.00167  # 0.167%
        self.balance += interest
        return interest

class User:
    def __init__(self, name, phone, nid):
        self.name = name
        self.phone = phone
        self.nid = nid
        self.accounts = []

class BankSystem:
    def __init__(self):
        self.users = {}
        self.card_to_account = {}
        self.shaba_to_account = {}
        self.pending_shaba_transfers = []

    def validate_user_info(self, name, phone, nid):
        valid_name = re.match(r'^(?=(.*[A-Za-z]){3,})[A-Za-z0-9_]+$', name)
        valid_phone = re.match(r'^09\d{9}$', phone)
        valid_nid = re.match(r'^\d{10}$', nid)
        return valid_name and valid_phone and valid_nid

    def create_user(self, name, phone, nid):
        if not self.validate_user_info(name, phone, nid):
            return f"Invalid user info: {name}, {phone}, {nid}"
        if name in self.users:
            return "Username already exists."
        self.users[name] = User(name, phone, nid)
        return f"User {name} registered successfully!"

    def create_account(self, username, acc_type, balance):
        if username not in self.users:
            return "User not found."
        if acc_type not in ["Normal", "ShortTerm", "LongTerm"]:
            return "Invalid account type."
        account = Account(acc_type, float(balance))
        self.users[username].accounts.append(account)
        self.card_to_account[account.card_number] = account
        self.shaba_to_account[account.shaba_number] = account

        disp_type = acc_type if acc_type == "Normal" else ("Short-term" if acc_type == "ShortTerm" else "Long-term")
        return (f"{disp_type} account created for {username} with card number {account.card_number} "
                f"and SHABA number {account.shaba_number}")


def change_account_balance(self, username, card_number, amount):
    if username not in self.users:
        return "User not found."
    user = self.users[username]
    account = None
    for acc in user.accounts:
        if acc.card_number == card_number:
            account = acc
            break
    if not account:
        return "Card number not found for the given user."
    amount = float(amount)
    if amount >= 0:
        account.deposit(amount)
        return f"Deposited {amount:.2f} Tomans. New balance: {account.balance:.2f} Tomans"
    else:
        withdraw_amount = -amount
        success, fee = account.withdraw(withdraw_amount)
        if success:
            return (f"Withdrawn {withdraw_amount:.2f} Tomans with a fee of {fee:.2f} Tomans. "
                    f"New balance: {account.balance:.2f} Tomans")
        else:
            return "Insufficient balance for withdrawal."

def transfer_card_to_card(self, sender_card, receiver_card, amount):
    amount = float(amount)
    if amount > 10000000:
        return "Transfer limit exceeded for card-to-card."
    sender = self.card_to_account.get(sender_card)
    receiver = self.card_to_account.get(receiver_card)
    if not sender or not receiver:
        return "Card number not found."
    fee = sender.transfer_fee(amount)
    total_deduction = amount + fee
    if sender.balance < total_deduction:
        return "Insufficient balance for transfer."
    sender.balance -= total_deduction
    receiver.balance += amount
    return (f"Card-to-card transfer completed successfully!\n"
            f"- Transfer amount: {amount:.2f} Tomans\n"
            f"- Sender card: {sender_card}\n"
            f"- Receiver card: {receiver_card}\n"
            f"- Sender balance: {sender.balance:.2f} Tomans\n"
            f"- Receiver balance: {receiver.balance:.2f} Tomans")


def transfer_shaba(self, sender_shaba, receiver_shaba, amount):
    amount = float(amount)
    if amount > 100000000:
        return "Transfer limit exceeded for SHABA."
    sender = self.shaba_to_account.get(sender_shaba)
    receiver = self.shaba_to_account.get(receiver_shaba)
    if not sender or not receiver:
        return "SHABA number not found."
    fee = sender.transfer_fee(amount)
    total_deduction = amount + fee
    if sender.balance < total_deduction:
        return "Insufficient balance for transfer."
    self.pending_shaba_transfers.append((sender, receiver, amount, fee, sender_shaba, receiver_shaba))
    return "SHABA transfer registered and will be completed at the end of the day."


def check_balance(self, card_number):
    account = self.card_to_account.get(card_number)
    if not account:
        return "Card number not found."
    return f"Balance of account {card_number}: {account.balance:.2f} Tomans"


def end_day(self):
    logs = ["End of day:"]
    if self.pending_shaba_transfers:
        for sender, receiver, amount, fee, sender_shaba, receiver_shaba in self.pending_shaba_transfers:
            sender.balance -= (amount + fee)
            receiver.balance += amount
            logs.append(
                f"- SHABA transfer completed!\n" f"  Transfer amount: {amount:.2f} Tomans\n" f"  Sender SHABA: {sender_shaba}\n" f"  Receiver SHABA: {receiver_shaba}\n" f"  Sender balance: {sender.balance:.2f} Tomans\n" f"  Receiver balance: {receiver.balance:.2f} Tomans")
            self.pending_shaba_transfers.clear()
        else:
            logs.append("- No pending SHABA transfers.")

        for user in self.users.values():
            for account in user.accounts:
                interest = account.apply_interest()
                if interest > 0:
                    logs.append(f"- Daily interest for {user.name}'s {account.acc_type} account calculated: {interest:.2f} Tomans\n" f"  New balance: {account.balance:.2f} Tomans")
        return '\n'.join(logs)

    def account_info(self, username):
        if username not in self.users:
            return "User not found."
        user = self.users[username]
        info = [f"User {user.name}'s information:", f"- Phone number: {user.phone}", f"- National ID: {user.nid}", "- Accounts:"]

        for account in user.accounts:
            info.append(f"  - Card number: {account.card_number}")
            info.append(f"    SHABA number: {account.shaba_number}")
            info.append(f"    Account type: {account.acc_type}")
            info.append(f"    Balance: {account.balance:.2f} Tomans")
        return "\n".join(info)


def run_bank_system():
    bank = BankSystem()
    print("Welcome to the Bank Management System. Enter your request.")
    while True:
        request = input()
        if request.upper() == "EXIT":
            print("Exiting system...")
            break

        parts = request.split()
        if parts[0] == "CREATE" and parts[1] == "USER":
            if len(parts) < 5:
                print("Invalid number of arguments for CREATE USER.")
                continue
            username, phone, nid = parts[2], parts[3], parts[4]
            print(bank.create_user(username, phone, nid))
        elif parts[0] == "CREATE" and parts[1] == "ACCOUNT":
            if len(parts) < 5:
                print("Invalid number of arguments for CREATE ACCOUNT.")
                continue
            username, acc_type, balance = parts[2], parts[3], parts[4]
            print(bank.create_account(username, acc_type, balance))
        elif parts[0] == "CHANGE" and parts[1] == "ACCOUNT" and parts[2] == "BALANCE":
            if len(parts) < 5:
                print("Invalid number of arguments for CHANGE ACCOUNT BALANCE.")
                continue
            username, card_number, amount = parts[3], parts[4], parts[5]
            print(bank.change_account_balance(username, card_number, amount))
        elif parts[0] == "TRANSFER" and parts[1] == "CARD" and parts[2] == "TO" and parts[3] == "CARD":
            if len(parts) < 6:
                print("Invalid number of arguments for TRANSFER CARD TO CARD.")
                continue
            sender_card, receiver_card, amount = parts[4], parts[5], parts[6]
            print(bank.transfer_card_to_card(sender_card, receiver_card, amount))
        elif parts[0] == "TRANSFER" and parts[1] == "SHABA":
            if len(parts) < 5:
                print("Invalid number of arguments for TRANSFER SHABA.")
                continue
            sender_shaba, receiver_shaba, amount = parts[2], parts[3], parts[4]
            print(bank.transfer_shaba(sender_shaba, receiver_shaba, amount))
        elif parts[0] == "CHECK" and parts[1] == "BALANCE":
            if len(parts) < 3:
                print("Invalid number of arguments for CHECK BALANCE.")
                continue
            card_number = parts[2]
            print(bank.check_balance(card_number))
        elif parts[0] == "END" and parts[1] == "DAY":
            print(bank.end_day())
        elif parts[0] == "ACCOUNT" and parts[1] == "INFO":
            if len(parts) < 3:
                print("Invalid number of arguments for ACCOUNT INFO.")
                continue
            username = parts[2]
            print(bank.account_info(username))
        else:
            print("Invalid request.")


if __name__ == '__main__':
    run_bank_system()
