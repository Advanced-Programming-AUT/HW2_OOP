from random import random, randint, choice

BASE_BUDGET = 100
END_DAY_BUDGET = 50
LOSS_AMOUNT = 50

class Troop:
    def __init__(self, power: float, chance: float, health: float) -> None:
        self.power = power
        self.chance = chance
        self.health = health

    def calc_damage(self) -> float:
        return (random() < self.chance) * self.power

    def take_damage(self, damage: float) -> bool:
        self.health -= damage
        return self.health <= 0

    def copy(self):
        return Troop(self.power, self.chance, self.health)

class User:
    def __init__(self, name: str, budget: int) -> None:
        self.name = name
        self.budget = budget
        self.troops = []

    def __str__(self) -> str:
        return f"{self.name} = {self.budget}"

    def buy(self, ttype: str, quantity: int) -> None:
        match ttype:
            case "Infantry":
                price = 10 * quantity
                troop = Troop(1, 0.8, 3)
            case "Cavalry":
                price = 25 * quantity
                troop = Troop(2, 0.6, 5)
            case "Archer":
                price = 20 * quantity
                troop = Troop(1.5, 0.75, 2)
            case "HeavyCavalry":
                price = 50 * quantity
                troop = Troop(4, 0.4, 10)
            case _:
                raise ValueError

        if self.budget <= price:
            print(f"Not enough money for {self.name}")
        else:
            print(f"{self.name} bought {quantity} {ttype}")
            self.budget -= price
            for _ in range(quantity):
                self.troops.append(troop.copy())

    def add_budget(self, add: int) -> None:
        self.budget += add

    def subtract_budget(self, sub: int) -> int:
        if self.budget > sub:
            self.budget -= sub
            return sub

        res = self.budget
        self.budget = 0
        return res

    def has_troop(self) -> bool:
        return len(self.troops) != 0

    def has_budget(self) -> bool:
        return self.budget != 0

    def attack(self) -> float:
        return choice(self.troops).calc_damage()

    def defend(self, damage: float) -> None:
        if not len(self.troops):
            return

        idx = randint(0, len(self.troops) - 1)
        if self.troops[idx].take_damage(damage):
            self.troops.pop(idx)

class Manager:
    def __init__(self):
        self.users = {}

    def add_user(self, name: str) -> None:
        if name in self.users:
            print(f"Username {name} already exists")
            return

        self.users[name] = User(name, BASE_BUDGET)
        print(f"Registered {name} with initial money of {BASE_BUDGET}")

    def day_end(self) -> None:
        for i in self.users:
            self.users[i].add_budget(END_DAY_BUDGET)
        print(f"End of the day, players budgets: {', '.join(map(str, self.users.values()))}")

    def buy(self, name: str, ttype: str, quantity: int) -> None:
        if name not in self.users:
            print(f"Username {name} doesn't exist")
            return

        self.users[name].buy(ttype, quantity)

    def attack(self, attacker: str, defender: str) -> None:
        if attacker not in self.users:
            print(f"Username {attacker} doesn't exist")
        if defender not in self.users:
            print(f"Username {defender} doesn't exist")

        print(f"{attacker} and {defender} started a battle")

        atk = self.users[attacker]
        dfn = self.users[defender]
        while atk.has_troop():
            dfn.defend(atk.attack())
            atk, dfn = dfn, atk

        add = atk.subtract_budget(LOSS_AMOUNT)
        dfn.add_budget(add)
        print(f"{atk.name} lost the battle\n{dfn.name} has taken {add} coins from {atk.name}")

        if not atk.has_budget():
            self.users.pop(atk.name)
            print(f"{atk.name} is eliminated")

manager = Manager()

while True:
    inp = input()
    if not inp:
        break

    code, data = inp.split(maxsplit=1)
    match code:
        case "CREATE_USER":
            manager.add_user(data)
        case "BUY":
            name, ttype, quantity = data.split()
            manager.buy(name, ttype, int(quantity))
        case "ATTACK":
            attacker, defender = data.split()
            manager.attack(attacker, defender)
        case "DAY":
            manager.day_end()
        case _:
            print("Invalid execution code")
