import random

soldier_types = {"Infantry": {"health": 3, "power": 1, "accuracy": 0.8, "cost": 10}, "Cavalry": {"health": 5, "power": 2, "accuracy": 0.6, "cost": 25}, "Archer": {"health": 2, "power": 1.5, "accuracy": 0.75, "cost": 20}, "HeavyCavalry": {"health": 10, "power": 4, "accuracy": 0.4, "cost": 50}}


class Soldier:
    def __init__(self, soldier_type):
        s = soldier_types[soldier_type]
        self.health = s["health"]
        self.power = s["power"]
        self.accuracy = s["accuracy"]
        self.type = soldier_type

    def is_alive(self):
        return self.health > 0


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.soldiers = []

    def buy_soldiers(self, soldier_type, quantity):
        cost = soldier_types[soldier_type]["cost"] * quantity
        if self.money - cost <= 0:
            return False
        for _ in range(quantity):
            self.soldiers.append(Soldier(soldier_type))
        self.money -= cost
        return True

    def get_alive_soldiers(self):
        return [s for s in self.soldiers if s.is_alive()]

    def is_eliminated(self):
        return self.money <= 0 and len(self.get_alive_soldiers()) == 0


class Game:
    def __init__(self):
        self.players = {}

    def create_user(self, name):
        if name in self.players:
            return f"{name} already exists."
        self.players[name] = Player(name)
        return f"Registered {name} with initial money of 100"

    def buy(self, name, soldier_type, quantity):
        if name not in self.players:
            return f"{name} does not exist."
        s = self.players[name].buy_soldiers(soldier_type, quantity)
        if s:
            return f"{name} bought {quantity} {soldier_type}"
        else:
            return f"{name} could not buy {quantity} {soldier_type}"

    def attack(self, attacker_name, defender_name):
        if attacker_name not in self.players or defender_name not in self.players:
            return "One of the players does not exist."
        attacker = self.players[attacker_name]
        defender = self.players[defender_name]

        if len(attacker.get_alive_soldiers()) == 0 or len(defender.get_alive_soldiers()) == 0:
            return "One of the players is not able to fight."

        bat = [f"{attacker.name} and {defender.name} started a battle"]

        turn = 0
        while attacker.get_alive_soldiers() and defender.get_alive_soldiers():
            if turn % 2 == 0:
                atk, def_ = attacker, defender
            else:
                atk, def_ = defender, attacker

            atk_soldier = random.choice(atk.get_alive_soldiers())
            def_soldier = random.choice(def_.get_alive_soldiers())

            if random.random() <= atk_soldier.accuracy:
                def_soldier.health -= atk_soldier.power
                if def_soldier.health < 0:
                    def_soldier.health = 0

            turn += 1

        if len(attacker.get_alive_soldiers()) > 0:
            winner, loser = attacker, defender
        else:
            winner, loser = defender, attacker

        winner.money += 50
        loser.money -= 50
        bat.append(f"{loser.name} lost the battle")
        bat.append(f"{winner.name} has taken 50 coin from {loser.name}")
        if loser.is_eliminated():
            bat.append(f"{loser.name} is Eliminated")
        return "\n".join(log)

    def day_end(self):
        for player in self.players.values():
            if not player.is_eliminated():
                player.money += 50
        result = "End of the day, players budgets: " + ", ".join(
            [f"{p.name} = {p.money}" for p in self.players.values()])
        return result


def main():
    game = Game()
    while True:
        line = input()


        if line.startswith("CREATE USER"):
            _, _, username = line.split()
            print(game.create_user(username))

        elif line.startswith("BUY"):
            _, username, soldier_type, quantity = line.split()
            print(game.buy(username, soldier_type, int(quantity)))

        elif line.startswith("ATTACK"):
            _, attacker, defender = line.split()
            print(game.attack(attacker, defender))

        elif line.strip() == "DAY END":
            print(game.day_end())


if __name__ == "__main__":
    main()
