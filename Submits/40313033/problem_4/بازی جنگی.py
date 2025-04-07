import random


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.soldiers = []

    def add_soldier(self, soldier_type, quantity):
        soldier_types = {
            "Infantry": {"health": 10, "attack_power": 1, "hit_chance": 0.8, "cost": 3},
            "Cavalry": {"health": 25, "attack_power": 2, "hit_chance": 0.6, "cost": 5},
            "Archer": {"health": 20, "attack_power": 0.75, "hit_chance": 0.5, "cost": 2},
            "Heavy_Cavalry": {"health": 50, "attack_power": 4, "hit_chance": 0.4, "cost": 10}
        }

        if soldier_type not in soldier_types:
            print(f"Invalid soldier type")
            return

        cost = soldier_types[soldier_type]["cost"] * quantity
        if self.money < cost:
            print(
                f"{self.name} does not have enough money to buy {quantity} {soldier_type}.")
            return

        for _ in range(quantity):
            self.soldiers.append(soldier_types[soldier_type].copy())

        self.money -= cost
        print(f"{self.name} bought {quantity} {soldier_type}(s).")

    def attack(self, opponent):
        if not self.soldiers and not opponent.soldiers:
            print(
                f"Both {self.name} and {opponent.name} have no soldiers. No battle occurs.")
            return

        if not self.soldiers:
            print(
                f"{self.name} has no soldiers and automatically loses to {opponent.name}!")
            self.money = 0
            return

        if not opponent.soldiers:
            print(
                f"{opponent.name} has no soldiers and automatically loses to {self.name}!")
            self.money += min(opponent.money, 50)
            opponent.money = 0
            return

        print(f"{self.name} and {opponent.name} started a battle!")

        while self.soldiers and opponent.soldiers:
            attacker = random.choice(self.soldiers)
            defender = random.choice(opponent.soldiers)

            if random.random() < attacker["hit_chance"]:
                defender["health"] -= attacker["attack_power"]
                if defender["health"] <= 0:
                    opponent.soldiers.remove(defender)

        if not opponent.soldiers:
            print(f"{opponent.name} lost the battle!")
            winnings = min(opponent.money, 50)
            self.money += winnings
            opponent.money -= winnings
            print(f"{self.name} has taken {winnings} coins from {opponent.name}.")

    def increase_money(self):
        self.money += 50


players = {}


def process_command(command):
    parts = command.split()
    if not parts:
        return

    action = parts[0]

    if action == "CREATE_USER":
        username = parts[1]
        if username in players:
            print(f"User {username} already exists.")
        else:
            players[username] = Player(username)
            print(f"Registered {username} with initial money of 100.")

    elif action == "BUY":
        username, soldier_type, quantity = parts[1], parts[2], int(parts[3])
        if username in players:
            players[username].add_soldier(soldier_type, quantity)
        else:
            print(f"User {username} does not exist.")

    elif action == "ATTACK":
        attacker, defender = parts[1], parts[2]
        if attacker in players and defender in players:
            players[attacker].attack(players[defender])
            if players[defender].money == 0:
                print(f"{defender} is Eliminated")
                del players[defender]
        else:
            print("One or both users do not exist.")

    elif action == "DAY":
        if parts[1] == "END":
            for player in players.values():
                player.increase_money()
            print("End of the day, players budgets: ", ", ".join(
                f"{p.name} = {p.money}" for p in players.values()))


def main():
    print("Welcome to the Game!")
    print("Enter commands to play. Type 'exit' to quit.")

    while True:
        command = input("Enter command: ").strip()
        if command.lower() == "exit":
            break
        process_command(command)


if __name__ == "__main__":
    main()
