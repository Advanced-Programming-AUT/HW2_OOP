import random
from abc import ABC, abstractclassmethod

class Attack(ABC):
    @abstractclassmethod
    def attack(self, other):
        pass

class Infantry(Attack):
    def __init__(self, name):
        self.health = 3
        self.name = name
        self.chance = [1, 1, 1, 1, 0] #0.8
        self.power = 1
        self.price = 10
    def attack(self, other):
        chance_for_hit = self.chance[random.randint(0, len(self.chance) - 1)]
        if chance_for_hit:
            other.health -= self.power
            print(f"attack from {self.name}")
            print(f"{other.name} hited")

class Cavalry(Attack):
    def __init__(self, name):
        self.health = 5
        self.name = name
        self.chance = [1, 1, 1, 0, 0] # 0.6
        self.power = 2
        self.price = 25
    def attack(self, other):
        chance_for_hit = self.chance[random.randint(0, len(self.chance) - 1)]
        if chance_for_hit:
            other.health -= self.power
            print(f"attack from {self.name}")
            print(f"{other.name} hited")
            
class Archer(Attack):
    def __init__(self, name):
        self.health = 2
        self.name = name
        self.chance = [1, 1, 1, 0] # 0.75
        self.power = 1.5
        self.price = 20
    def attack(self, other):
        chance_for_hit = self.chance[random.randint(0, len(self.chance) - 1)]
        if chance_for_hit:
            other.health -= self.power
            print(f"attack from {self.name}")
            print(f"{other.name} hited")

class HeavyCavalry(Attack):
    def __init__(self, name):
        self.health = 10
        self.name = name
        self.chance = [1, 1, 0, 0, 0] # 0.4
        self.power = 4
        self.price = 50
    def attack(self, other):
        chance_for_hit = self.chance[random.randint(0, len(self.chance) - 1)]
        if chance_for_hit:
            other.health -= self.power
            print(f"attack from {self.name}")
            print(f"{other.name} hited")
list_all_gamers = []      
list_all_gamer = []
class Gamer:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin
        list_all_gamer.append(self)
        list_all_gamers.append(self)
        self.soldeirs = []
        print(f"Registered {self.name} with intialize money of {self.coin}\n")
    def setter(self):
        if self.coin < 0:
            self.coin = 0
    def attack(self, other):
        count = 0 
        print(f"{self.name} and {other.name} started the battle\n")
        while len(other.soldeirs) != 0 and len(self.soldeirs) != 0:
            if count % 2 == 0:
                solder_attack = self.soldeirs[random.randint(0, len(self.soldeirs) - 1)]
                solder_defnece = other.soldeirs[random.randint(0, len(other.soldeirs) - 1)]
                solder_attack.attack(solder_defnece)
                if solder_defnece.health <= 0:
                    other.soldeirs.remove(solder_defnece)
            if count % 2 == 1:
                solder_attack = other.soldeirs[random.randint(0, len(other.soldeirs) - 1)]
                solder_defnece = self.soldeirs[random.randint(0, len(self.soldeirs) - 1)]
                solder_attack.attack(solder_defnece)
                if solder_defnece.health <= 0:
                    self.soldeirs.remove(solder_defnece)
            count += 1
        if len(other.soldeirs) == 0:
            print(f"\n{other.name} lose the battle\n")
            self.coin += 50
            other.coin -= 50
            print(f"{self.name} has taken 50 coins from {other.name}\n")
            if other.coin <= 0:
                list_all_gamer.remove(other)
                print(f"{other.name} is Eliminated\n")
        else:
            print(f"\n{self.name} lose the battle\n")
            other.coin += 50
            self.coin -= 50
            print(f"{other.name} has taken 50 coins from {self.name}\n")
            if self.coin <= 0:
                list_all_gamer.remove(self)
                print(f"{self.name} is Eliminated\n")
                
    def buy_soldeir(self, type_of_soldeir, count):
        if type_of_soldeir not in ["Infantry", "Cavalry", "Archer", "Heavy_Cavalry"]:
            print("Please Enter Type Of Soldier Correctly\n")
        else:
            if type_of_soldeir == "Infantry":
                if 10 * int(count) >= self.coin:
                    print("Not Enough Money\n")
                else:
                    name_of_soldeir = input("Enter your soldeir's name: ")
                    for _ in range(count):
                        self.soldeirs.append(Infantry(name_of_soldeir))
                    self.coin -= 10 * count
                    print(f"{self.name} bought {count} {type_of_soldeir}\n")
            if type_of_soldeir == "Cavalry":
                if 25 * int(count) >= self.coin:
                    print("Not Enough Money\n")
                else:
                    name_of_soldeir = input("Enter your soldeir's name: ")
                    for _ in range(count):
                        self.soldeirs.append(Cavalry(name_of_soldeir))
                    self.coin -= 25 * count
                    print(f"{self.name} bought {count} {type_of_soldeir}\n")
            if type_of_soldeir == "Archer":
                if 20 * int(count) >= self.coin:
                    print("Not Enough Money\n")
                else:
                    name_of_soldeir = input("Enter your soldeir's name: ")
                    for _ in range(int(count)):
                        self.soldeirs.append(Archer(name_of_soldeir))
                    self.coin -= 20 * count
                    print(f"{self.name} bought {count} {type_of_soldeir}\n")
            if type_of_soldeir == "Heavy_Cavalry":
                if 50 * int(count) >= self.coin:
                    print("Not Enough Money\n")
                else:
                    name_of_soldeir = input("Enter your soldeir's name: ")
                    for _ in range(int(count)):
                        self.soldeirs.append(HeavyCavalry(name_of_soldeir))
                    self.coin -= 50 * count
                    print(f"{self.name} bought {count} {type_of_soldeir}\n")
order = [""]
while order[0] != "Exit":
    order = input().split()
    if order[0] == "CREATE_USER":
        gamer = Gamer(order[1], 100)
        
    if order[0] == "BUY":
        count = 1
        for gamer in list_all_gamer:
            if gamer.name == order[1]:
                gamer = gamer
                count = 0
                break
        if count:
            print("This Name was not signed up!\n")
        else:
            if order[2] not in ["Infantry", "Cavalry", "Archer", "Heavy_Cavalry"]:
                print("This Type Not Exist\n")
            else:
                gamer.buy_soldeir(order[2], int(order[3]))
                
    if order[0] == "ATTACK":
        name_of_defencer = order[2]
        name_of_attacker = order[1]
        count1 = 1
        count2 = 1
        for gamer_attacker in list_all_gamer:
            if gamer_attacker.name == name_of_attacker:
                attacker = gamer_attacker
                count2 = 0
                break
        if count2:
            print("The attacker not exist!\n")
         
        for gamer_defencer in list_all_gamer:
            if gamer_defencer.name == name_of_defencer:
                defencer = gamer_defencer
                count1 = 0
                break
        if count1:
            print("The defencer not exist!\n")
        if count1 == 0 and count2 == 0:
            attacker.attack(defencer)
        
    if order[0] == "DAY" and order[1] == "END":
        print("End of The Day:")
        for gamer in list_all_gamer:
            gamer.coin += 50
        print("The Daily Profit assigned for gamers\n")
        if len(list_all_gamer) == 1:
            print(f"{list_all_gamer[0].name} victory finally !!!\n")
        print("Player's Budgets:")
        for gamer in list_all_gamers:
            gamer.setter()
            print(f"- {gamer.name} : {gamer.coin}")
        
        