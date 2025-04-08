import random


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.army = []

    def buy_soldiers(self, soldier_type, quantity):
        if soldier_type not in Soldier.soldier_types:
            print(f" try again. it is not acceptable : {soldier_type}")
            return

        cost, health, power, hit_chance = Soldier.soldier_types[soldier_type]
        total_cost = cost * quantity
        if self.money >= total_cost:
            self.money -= total_cost
            for _ in range(quantity):
                self.army.append(Soldier(soldier_type, health, power, hit_chance))
            print(f"{self.name} bought {quantity} {soldier_type}")
        else:
            print(f"{self.name} has not enough amount... to buy  {quantity} {soldier_type}")

    def is_defeated(self):
        return len(self.army) == 0

    def upgrade_soldiers(self):
        if self.money >= 20:
            self.money -= 20
            for soldier in self.army:
                soldier.health += 5
                soldier.power += 1
            print(f"{self.name} upgraded all  of the soldiers")
        else:
            print(f"{self.name} has not enough amount to upgrade soldiers")

    def show_status(self):
        print(f"{self.name} -> Money: {self.money}, Army Size: {len(self.army)}")


class Soldier:
    soldier_types = {
        "Infantry": (3, 10, 1, 0.8),
        "Cavalry": (5, 25, 2, 0.6),
        "Archer": (2, 20, 1.5, 0.75),
        "HeavyCavalry": (10, 50, 4, 0.4)
    }

    def __init__(self, soldier_type, health, power, hit_chance):
        self.type = soldier_type
        self.health = health
        self.power = power
        self.hit_chance = hit_chance

    def attack(self, enemy):
        if random.random() < self.hit_chance:
            enemy.health -= self.power
            return True
        return False


class WarGame:
    def __init__(self):
        self.players = {}

    def create_user(self, name):
        if name not in self.players:
            self.players[name] = Player(name)
            print(f"Registered {name} with initial money of 100")
        else:
            print(f"User {name} already exists")

    def buy(self, name, soldier_type, quantity):
        if name in self.players:
            self.players[name].buy_soldiers(soldier_type, quantity)

    def attack(self, attacker_name, defender_name):
        if attacker_name in self.players and defender_name in self.players:
            attacker = self.players[attacker_name]
            defender = self.players[defender_name]
            print(f"{attacker_name} and {defender_name} started a battle")

            while attacker.army and defender.army:
                attacking_soldier = random.choice(attacker.army)
                defending_soldier = random.choice(defender.army)

                if attacking_soldier.attack(defending_soldier):
                    if defending_soldier.health <= 0:
                        defender.army.remove(defending_soldier)

                attacker, defender = defender, attacker

            if not defender.army:
                print(f"{defender_name} lost the battle")
                attacker.money += defender.money // 2
                defender.money //= 2
                if defender.money == 0:
                    del self.players[defender_name]
                    print(f"{defender_name} is eliminated")

    def upgrade(self, name):
        if name in self.players:
            self.players[name].upgrade_soldiers()

    def show_status(self, name):
        if name in self.players:
            self.players[name].show_status()

    def day_end(self):
        for player in self.players.values():
            player.money += 50
        print("End of the day, players' budgets:", ", ".join([f"{p.name} = {p.money}" for p in self.players.values()]))


game = WarGame()
while True:
    request = input().strip()
    if request == "EXIT":
        break
    parts = request.split()
    if parts[0] == "CREATE_USER":
        game.create_user(parts[1])
    elif parts[0] == "BUY":
        if len(parts) < 4:
            print ("ERROR : Invalid BUY request. Format should be : BUY <name> <soldier_type> <quantity>")
        else:
             game.buy(parts[1], parts[2], int(parts[3]))
    elif parts[0] == "ATTACK":
        game.attack(parts[1], parts[2])
    elif parts[0] == "UPGRADE":
        game.upgrade(parts[1])
    elif parts[0] == "STATUS":
        game.show_status(parts[1])
    elif request == "DAY END":
        game.day_end()