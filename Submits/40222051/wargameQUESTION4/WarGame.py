import random

class Player:
    soldier_dict = {
        'Infantry': {'cost': 10, 'power': 1, 'chance': 0.8, 'health': 3},
        'Cavalry': {'cost': 25, 'power': 2, 'chance': 0.6, 'health': 5},
        'Archer': {'cost': 20, 'power': 1.5, 'chance': 0.75, 'health': 2},
        'Heavy Cavalry': {'cost': 50, 'power': 4, 'chance': 0.4, 'health': 10}
    }

    def __init__(self, name):
        self.name = name
        self.amount = 100  # Starting budget
        self.soldiers = {}

    def buy_soldier(self, soldier, amount):
        cost = Player.soldier_dict[soldier]['cost'] * amount
        if cost <= self.amount:
            self.amount -= cost
            if soldier in self.soldiers:
                self.soldiers[soldier]['amount'] += amount
            else:
                self.soldiers[soldier] = {'amount': amount, **Player.soldier_dict[soldier]}
            print(f"{self.name} bought {amount} {soldier}(s). Remaining budget: ${self.amount}")
        else:
            print('Not enough money')

    def end_day(self):
        self.amount += 50
        print(f"End of day, {self.name}'s budget increased by $50 to ${self.amount}")

    def is_eliminated(self):
        return len(self.soldiers) == 0 or all(s['amount'] <= 0 for s in self.soldiers.values())

class War:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def attack(self):
        if self.attacker.is_eliminated() or self.defender.is_eliminated():
            return False  # Battle ends if either player is eliminated

        attacker_soldiers = list(self.attacker.soldiers.keys())
        defender_soldiers = list(self.defender.soldiers.keys())

        if not attacker_soldiers or not defender_soldiers:
            return False

        random_attacker_soldier = random.choice(attacker_soldiers)
        random_defender_soldier = random.choice(defender_soldiers)

        # Attacker's attack
        if random.random() < self.attacker.soldiers[random_attacker_soldier]['chance']:
            power = self.attacker.soldiers[random_attacker_soldier]['power']
            self.defender.soldiers[random_defender_soldier]['health'] -= power
            print(f"{self.attacker.name}'s {random_attacker_soldier} hits {self.defender.name}'s {random_defender_soldier} for {power} damage")
            if self.defender.soldiers[random_defender_soldier]['health'] <= 0:
                self.defender.soldiers[random_defender_soldier]['amount'] -= 1
                print(f"{self.defender.name}'s {random_defender_soldier} is defeated!")
                if self.defender.soldiers[random_defender_soldier]['amount'] > 0:
                    self.defender.soldiers[random_defender_soldier]['health'] = Player.soldier_dict[random_defender_soldier]['health']
                else:
                    del self.defender.soldiers[random_defender_soldier]

        # Defender's counter-attack
        if random.random() < self.defender.soldiers[random_defender_soldier]['chance']:
            power = self.defender.soldiers[random_defender_soldier]['power']
            self.attacker.soldiers[random_attacker_soldier]['health'] -= power
            print(f"{self.defender.name}'s {random_defender_soldier} hits {self.attacker.name}'s {random_attacker_soldier} for {power} damage")
            if self.attacker.soldiers[random_attacker_soldier]['health'] <= 0:
                self.attacker.soldiers[random_attacker_soldier]['amount'] -= 1
                print(f"{self.attacker.name}'s {random_attacker_soldier} is defeated!")
                if self.attacker.soldiers[random_attacker_soldier]['amount'] > 0:
                    self.attacker.soldiers[random_attacker_soldier]['health'] = Player.soldier_dict[random_attacker_soldier]['health']
                else:
                    del self.attacker.soldiers[random_attacker_soldier]

        return True  # Battle continues


def process():
    print("Welcome to the War Game!")
    player1_name = input("Enter first player's name: ")
    player2_name = input("Enter second player's name: ")

    player1 = Player(player1_name)
    player2 = Player(player2_name)
    war = War(player1, player2)

    while True:
        print("\nWar Game Menu")
        print("1. Buy Soldiers (Player 1)")
        print("2. Buy Soldiers (Player 2)")
        print("3. Start Battle")
        print("4. End Day (Gain $50)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1" or choice == "2":
            player = player1 if choice == "1" else player2
            print("Available soldiers:")
            for i, soldier in enumerate(Player.soldier_dict.keys(), 1):
                print(f"{i}. {soldier} - Cost: ${Player.soldier_dict[soldier]['cost']}")
            soldier_choice = int(input("Select soldier number: ")) - 1
            soldier_name = list(Player.soldier_dict.keys())[soldier_choice]
            amount = int(input(f"How many {soldier_name}s to buy? "))
            player.buy_soldier(soldier_name, amount)

        elif choice == "3":
            if not player1.soldiers or not player2.soldiers:
                print("Both players need soldiers to fight!")
                continue
            print("Battle begins!")
            while war.attack():
                if player1.is_eliminated():
                    print(f"{player1.name} is Eliminated")
                    print(
                        f"End of the day, players budgets: {player2.name} ${player2.amount}$. {player1.name} ${player1.amount}$")
                    return
                elif player2.is_eliminated():
                    print(f"{player2.name} is Eliminated")
                    print(
                        f"End of the day, players budgets: {player1.name} ${player1.amount}$. {player2.name} ${player2.amount}$")
                    return

        elif choice == "4":
            player1.end_day()
            player2.end_day()

        elif choice == "5":
            print("Exiting game...")
            break

        else:
            print("Invalid choice! Please try again.")


process()




