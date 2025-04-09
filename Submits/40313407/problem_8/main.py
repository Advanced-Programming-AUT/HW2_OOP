from random import randint

class Client:
    def __init__(self, name, phone, nid):
        if not (phone.startswith("09") and len(phone) == 11):
            print("Invalid phone number")
        elif len(nid) != 10:
            print("Invalid national ID")
        self.name = name
        self.phone = phone
        self.national_id = nid
        self.wallets = []

    def find_account(self, card_id=None, shaba_id=None):
        for acc in self.wallets:
            if card_id and acc.card == card_id:
                return acc
            if shaba_id and acc.shaba == shaba_id:
                return acc
        return None

    def __str__(self):
        details = f"Client: {self.name}\nPhone: {self.phone}\nNational ID: {self.national_id}\nAccounts:"
        for acc in self.wallets:
            details += f"\n- Card: {acc.card}, SHABA: {acc.shaba}, Type: {acc.kind}, Balance: {acc.balance} Tomans"
        return details


class BankAccount:
    def __init__(self, card, shaba, kind, amount):
        self.card = card
        self.shaba = shaba
        self.kind = kind
        self.balance = amount
        self.pending = 0

    def __str__(self):
        return f'Balance for {self.card}: {self.balance} Tomans'

    def close_day(self):
        if self.kind == 'Short-term':
            self.balance *= 1.067
        elif self.kind == 'Long-term':
            self.balance *= 1.167
        self.balance += self.pending
        self.pending = 0

    def transact(self, val):
        if self.balance + val >= 0:
            self.balance += val
            return True
        return False


central_bank = BankAccount('BANK_CORE', 'BANK_CORE', 'SYSTEM', 0)
client_db = {}
acc_index = {}

while True:
    cmd = input().split()
    if cmd[0] == 'REGISTER':
        client_db[cmd[1]] = Client(cmd[1], cmd[2], cmd[3])
        print(f"{cmd[1]} has been registered.")
    elif cmd[0] == 'NEW_ACCOUNT':
        if cmd[1] in client_db:
            card_num = str(randint(10**16, 10**17 - 1))
            shaba_num = 'IR' + str(randint(10**24, 10**25 - 1))
            acc = BankAccount(card_num, shaba_num, cmd[2], int(cmd[3]))
            client_db[cmd[1]].wallets.append(acc)
            acc_index[card_num] = cmd[1]
            acc_index[shaba_num] = cmd[1]
            print(f"{cmd[2]} account created for {cmd[1]} with Card: {card_num}, SHABA: {shaba_num}")
        else:
            print("Client not found.")
    elif cmd[0] == 'INFO':
        if cmd[1] in client_db:
            print(client_db[cmd[1]])
        else:
            print("Client not found.")
    elif cmd[0] == 'CARD_TRANSFER':
        from_card, to_card, amt = cmd[1], cmd[2], int(cmd[3])
        if from_card in acc_index and to_card in acc_index:
            sender = client_db[acc_index[from_card]].find_account(card_id=from_card)
            receiver = client_db[acc_index[to_card]].find_account(card_id=to_card)
            if sender.transact(-amt):
                if sender.kind == 'Short-term':
                    receiver.transact(amt * 0.99)
                    central_bank.transact(amt * 0.01)
                elif sender.kind == 'Long-term':
                    receiver.transact(amt * 0.97)
                    central_bank.transact(amt * 0.03)
                else:
                    receiver.transact(amt)
                print("Card-to-card transaction successful.")
                print(sender)
                print(receiver)
            else:
                print("Insufficient balance.")
        else:
            print("Invalid card(s).")
    elif cmd[0] == 'SHABA_TRANSFER':
        from_shaba, to_shaba, amt = cmd[1], cmd[2], int(cmd[3])
        if from_shaba in acc_index and to_shaba in acc_index:
            sender = client_db[acc_index[from_shaba]].find_account(shaba_id=from_shaba)
            receiver = client_db[acc_index[to_shaba]].find_account(shaba_id=to_shaba)
            if sender.transact(-amt):
                if sender.kind == 'Short-term':
                    receiver.pending += amt * 0.99
                    central_bank.transact(amt * 0.01)
                elif sender.kind == 'Long-term':
                    receiver.pending += amt * 0.97
                    central_bank.transact(amt * 0.03)
                else:
                    receiver.pending += amt
                print("SHABA transfer successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid SHABA(s).")
    elif cmd[0] == 'ADJUST_BALANCE':
        username, card_id, amount = cmd[1], cmd[2], int(cmd[3])
        if card_id in acc_index:
            account = client_db[acc_index[card_id]].find_account(card_id=card_id)
            if account.transact(amount):
                print("Balance updated.")
                print(account)
            else:
                print("Transaction failed due to insufficient funds.")
        else:
            print("Account not found.")
    elif cmd[0] == 'BALANCE_CHECK':
        if cmd[1] in acc_index:
            acc = client_db[acc_index[cmd[1]]].find_account(card_id=cmd[1])
            print(acc)
        else:
            print("Account not found.")
    elif cmd[0] == 'DAY_END':
        for person in client_db.values():
            for acc in person.wallets:
                acc.close_day()

