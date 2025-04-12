import random


class Soldier:
    def __init__(self, soldier_type, cost, power, health, hit_chance):
        self.type = soldier_type
        self.cost = cost
        self.power = power
        self.health = health
        self.hit_chance = hit_chance

    def attack(self, target):
        if random.random() <= self.hit_chance:
            target.health -= self.power
            print(f"{self.type} successfully hit {target.type}!")
            if target.health <= 0:
                print(f"{target.type} has been eliminated!")
        else:
            print(f"{self.type} missed the attack.")


class User:
    def __init__(self, username):
        self.username = username
        self.money = 100
        self.soldiers = []

    def buy_soldier(self, soldier_type, quantity):
        for _ in range(quantity):
            if self.money >= soldier_type.cost:
                self.soldiers.append(Soldier(soldier_type.type, soldier_type.cost, soldier_type.power, soldier_type.health, soldier_type.hit_chance))
                self.money -= soldier_type.cost
                print(f"{self.username} bought a {soldier_type.type}.")
            else:
                print(f"{self.username} does not have enough money to buy a {soldier_type.type}.")

    def __str__(self):
        return f"{self.username}: Money={self.money}, Soldiers={len(self.soldiers)}"


class Game:
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        if username in self.users:
            print(f"User {username} already exists.")
        else:
            self.users[username] = User(username)
            print(f"Registered {username} with initial money of 100.")

    def battle(self, attacker_name, defender_name):
        if attacker_name not in self.users or defender_name not in self.users:
            print("One or both users do not exist.")
            return

        attacker = self.users[attacker_name]
        defender = self.users[defender_name]

        print(f"Battle started between {attacker_name} and {defender_name}!")

        while attacker.soldiers and defender.soldiers:
            attacking_soldier = random.choice(attacker.soldiers)
            defending_soldier = random.choice(defender.soldiers)

            attacking_soldier.attack(defending_soldier)
            if defending_soldier.health <= 0:
                defender.soldiers.remove(defending_soldier)

            attacker, defender = defender, attacker  # Switch turns

        if defender.soldiers:
            print(f"{defender_name} won the battle and claimed all money from {attacker_name}.")
            defender.money += attacker.money
            attacker.money = 0
        else:
            print(f"{attacker_name} won the battle and claimed all money from {defender_name}.")
            attacker.money += defender.money
            defender.money = 0

        self.check_eliminations()

    def end_day(self):
        for user in self.users.values():
            user.money += 50
        print("End of the day. Updated users' budgets:")
        for user in self.users.values():
            print(f"{user.username}: Money = {user.money}")

        self.check_eliminations()

    def check_eliminations(self):
        eliminated_users = [username for username, user in self.users.items() if user.money == 0]
        for username in eliminated_users:
            del self.users[username]
            print(f"User {username} has been eliminated!")

    def check_winner(self):
        if len(self.users) == 1:
            winner = list(self.users.values())[0]
            print(f"The winner of the game is {winner.username}!")
            return True
        return False


def game_menu():
    game = Game()
    print("Welcome to the War Game!")
    print("Choose an option to proceed:")

    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. Buy Soldiers")
        print("3. Attack Another User")
        print("4. End Day")
        print("5. Show Users")
        print("6. Exit Game")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            username = input("Enter username to create: ")
            game.create_user(username)

        elif choice == "2":
            username = input("Enter username: ")
            soldier_type = input("Enter soldier type (Infantry/Cavalry/Archer/Heavy Cavalry): ")
            quantity = int(input("Enter quantity: "))

            # Match soldier type with existing definitions
            soldier = None
            if soldier_type == "Infantry":
                soldier = infantry
            elif soldier_type == "Cavalry":
                soldier = cavalry
            elif soldier_type == "Archer":
                soldier = archer
            elif soldier_type == "Heavy Cavalry":
                soldier = heavy_cavalry

            if soldier:
                game.users[username].buy_soldier(soldier, quantity)
            else:
                print("Invalid soldier type. Please try again.")

        elif choice == "3":
            attacker = input("Enter attacker's username: ")
            defender = input("Enter defender's username: ")
            game.battle(attacker, defender)

        elif choice == "4":
            game.end_day()

        elif choice == "5":
            print("Current Users:")
            for user in game.users.values():
                print(user)

        elif choice == "6":
            print("Exiting the game. Thank you for playing!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Start the game
if __name__ == "__main__":
    # Define soldier types
    infantry = Soldier("Infantry", 10, 1, 3, 0.8)
    cavalry = Soldier("Cavalry", 25, 2, 5, 0.6)
    archer = Soldier("Archer", 20, 1.5, 2, 0.75)
    heavy_cavalry = Soldier("Heavy Cavalry", 50, 4, 10, 0.4)

    game_menu()
