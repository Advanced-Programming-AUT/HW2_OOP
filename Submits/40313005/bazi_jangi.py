from abc import ABC
import random

class User:
    def __init__(self,name, money ):
        self.name = name
        self.money = money
        self.cards = []

class Card(ABC):
    def __init__(self, price,damage,accuracy,hp ):
        self.price = price
        self.damage = damage
        self.accuracy = accuracy
        self.hp = hp

    def attack(self):
        return (self.damage * random.choices([1, 0], weights=[self.accuracy, 1-self.accuracy])[0])

    def alive(self):
        return (self.hp == 0)

class Infantry(Card):
    def __init__(self):
        super().__init__(10, 1, 0.8, 3)

class Cavalry(Card):
    def __init__(self):
        super().__init__(25, 2, 0.6, 5)

class Archer(Card):
    def __init__(self):
        super().__init__(20, 1.5, 0.75, 2)

class Cavalry_Heavy(Card):
    def __init__(self):
        super().__init__(50, 4, 0.4, 10)


users=[]

while(True):
    command = input().split()
    match command[0]:
        case "CREATE_USER":
            new_user = User(command[1],100)
            users.append(new_user)
            print(f"New user regestered! {new_user.name} - {new_user.money}")
        case "BUY":
            for user in users:
                if user.name == command[1]:
                    match command[2]:
                        case "Infantry":
                            for i in range(int(command[3])):
                                new_card = Infantry()
                                if user.money < new_card.price:
                                    print("Not enught money!")
                                else:
                                    user.money -= new_card.price
                                    user.cards.append(new_card)
                                    print("1 card bought!")
                        case "Cavalry":
                            for i in range(int(command[3])):
                                new_card = Cavalry()
                                if user.money < new_card.price:
                                    print("Not enught money!")
                                else:
                                    user.money -= new_card.price
                                    user.cards.append(new_card)
                                    print("1 card bought!")
                        case "Archer":
                            for i in range(int(command[3])):
                                new_card = Archer()
                                if user.money < new_card.price:
                                    print("Not enught money!")
                                else:
                                    user.money -= new_card.price
                                    user.cards.append(new_card)
                                    print("1 card bought!")
                        case "Cavalry_Heavy":
                            for i in range(int(command[3])):
                                new_card = Cavalry_Heavy()
                                if user.money < new_card.price:
                                    print("Not enught money!")
                                else:
                                    user.money -= new_card.price
                                    user.cards.append(new_card)
                                    print("1 card bought!")
        case "ATTACK":
            attacker =None
            definder =None
            flag = -1
            for user in users:
                if user.name == command[1]:
                    attacker = user
                elif user.name == command[2]:
                    definder = user
            
            while len(attacker.cards) != 0 and len(definder.cards)!= 0:
                attacker_card = attacker.cards[random.randint(0,len(attacker.cards)-1)]
                definder_card = definder.cards[random.randint(0,len(definder.cards)-1)]
                if flag == -1:
                    definder_card.hp -= attacker_card.attack()
                    if not definder_card.alive():
                        definder.cards.remove(definder_card)
                    flag *= -1
                else:
                    attacker_card.hp -= definder_card.attack()
                    if not attacker_card.alive():
                        attacker.cards.remove(attacker_card)
                    flag *= -1


            if len(attacker.cards) != 0:
                attacker.money += 50 ;  definder.money -= 50
                print(f"{attacker.name} won!  - {definder.name} lost 50 coins.")
                if definder.money <= 0:
                    print(f"{definder.name} eliminated!")
                    users.remove(definder)
            else: 
                attacker.money -= 50 ;  definder.money += 50
                print(f"{definder.name} won!  - {attacker.name} lost 50 coins.")
                if attacker.money <= 0:
                    print(f"{attacker.name} eliminated!")
                    users.remove(attacker)

        
        case "DAY":
            print("It's new day!")
            for user in users:
                user.money += 50
                print(f"{user.name} : {user.money}")