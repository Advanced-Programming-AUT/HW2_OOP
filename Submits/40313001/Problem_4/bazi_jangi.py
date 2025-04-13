import random

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.soldiers = []

    def buy_soldier(self, soldier_type, quantity):
        cost, health, power, hit_chance = Soldier.TYPES[soldier_type]
        total_cost = cost * quantity
        if self.money >= total_cost:
            self.money -= total_cost
            for _ in range(quantity):
                self.soldiers.append(Soldier(soldier_type))
            print(f"{self.name} bought {quantity} {soldier_type}")
        else:
            print(f"{self.name} does not have enough money to buy {quantity} {soldier_type}")

    def attack(self, opponent):
        print(f"{self.name} and {opponent.name} started a battle")
        while self.soldiers and opponent.soldiers:
            attacker_soldier = random.choice(self.soldiers)
            defender_soldier = random.choice(opponent.soldiers)
            attacker_soldier.attack(defender_soldier)
            if defender_soldier.health <= 0:
                opponent.soldiers.remove(defender_soldier)

        if not opponent.soldiers:
            print(f"{opponent.name} Lost the battle")
            winnings = min(opponent.money, 50)
            self.money += winnings
            opponent.money -= winnings
            print(f"{self.name} has taken {winnings} coins from {opponent.name}")
            if opponent.money == 0:
                print(f"{opponent.name} is Eliminated")

    def end_day(self):
        self.money += 50


class Soldier:
    TYPES = {
        "Infantry": (3, 10, 1, 0.8),
        "Cavalry": (6, 25, 2, 0.6),
        "Archer": (5, 20, 1.5, 0.75),
        "Heavy Cavalry": (10, 50, 4, 0.4)
    }

    def __init__(self, soldier_type):
        self.type = soldier_type
        self.health, self.power, self.hit_chance = self.TYPES[soldier_type][1:]

    def attack(self, enemy):
        enemy.health -= self.power


#test case
players = {}
commands = [
    "CREATE_USER Alice",
    "CREATE_USER Bob",
    "BUY Alice Infantry 5",
    "BUY Bob Cavalry 2",
    "ATTACK Alice Bob",
    "DAY END",
    "BUY Bob Archer 3",
    "ATTACK Bob Alice",
    "DAY END"
]

for command in commands:
    parts = command.split()
    if parts[0] == "CREATE_USER":
        name = parts[1]
        players[name] = Player(name)
        print(f"Registered {name} with initial money of 100")
    elif parts[0] == "BUY":
        name, soldier_type, quantity = parts[1], parts[2], int(parts[3])
        if name in players:
            players[name].buy_soldier(soldier_type, quantity)
    elif parts[0] == "ATTACK":
        attacker, defender = parts[1], parts[2]
        if attacker in players and defender in players:
            players[attacker].attack(players[defender])
    elif command == "DAY END":
        for player in players.values():
            player.end_day()
        print("End of the day, players budgets:", ", ".join(f"{p.name} = {p.money}" for p in players.values()))
