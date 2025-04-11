import random
class Player:
    def __init__(self, username, budget=100):
        self.username = username
        self.budget = budget
        self.soldiers = {"Infantry" : {"quantity" : 0, "health" : 3},
                         "Cavalry" : {"quantity" : 0, "health" : 5},
                         "Archer" : {"quantity" : 0, "health" : 2},
                         "Heavy Cavalry" : {"quantity" : 0, "health" : 10}}
        self.exist_soldiers = []
    def __str__(self):
        return f"Registered {self.username} with initial money of 100"
    def buy_soldier(self, soldier_type, quantity):
        quantity = int(quantity)
        soldier_price = {"Infantry" : 10, "Cavalry" : 25, "Archer" : 20, "Heavy Cavalry" : 50}
        if self.budget >= (soldier_price[soldier_type] * quantity):
            self.budget -= soldier_price[soldier_type] * quantity
            self.soldiers[soldier_type]["quantity"] += quantity
            print(f"{self.username} bought {quantity} {soldier_type}")
        else:
            print("Not enough money")
    def day_end(self):
        self.budget += 50
        return f"{self.username} : {self.budget}"
    def random_soldiers(self):
        for soldier in self.soldiers:
            if self.soldiers[soldier]["quantity"] > 0:
                self.exist_soldiers.append(soldier)
        soldier =random.choice(self.exist_soldiers)
        return  soldier

class Fight:
    def __init__(self, attacker:Player, defender:Player):
        self.attacker = attacker
        self.defender = defender
        self.soldiers_data = {"Infantry" : {"health" : 3, "power" : 1, "luck" : 0.8},
                     "Cavalry" : {"health" : 5, "power" : 2, "luck" : 0.6},
                     "Archer" : {"health" : 2, "power" : 1.5, "luck" : 0.75},
                     "Heavy Cavalry" : {"health" : 10, "power" : 4, "luck" : 0.4}}
        self.loser = None
    def __str__(self):
        result = f"{self.loser} lost the battle"
        if self.defender.budget < 0:
            result += f"\n{self.defender.username} is Eliminated"
        elif self.attacker.budget < 0:
            result += f"\n{self.attacker.username} is Eliminated"
        return result
    def battle(self):
        print(f"{self.attacker.username} and {self.defender.username} started a battle")
        while  self.attacker.exist_soldiers and self.defender.exist_soldiers:
            attacker_soldier = self.attacker.random_soldiers()
            defender_soldier = self.defender.random_soldiers()
            attacker_damage = random.uniform(0, self.soldiers_data[attacker_soldier]["luck"]) * self.soldiers_data[attacker_soldier]["power"]
            self.defender.soldiers[defender_soldier]["health"] -= attacker_damage
            if self.defender.soldiers[defender_soldier]["health"] <= 0:
                self.defender.soldiers[defender_soldier]["quantity"] -=1
            defender_soldier = self.defender.random_soldiers()
            attacker_soldier = self.attacker.random_soldiers()
            defender_damage = random.uniform(0, self.soldiers_data[defender_soldier]["luck"]) * self.defender.soldiers[defender_soldier]["quantity"]
            self.attacker.soldiers[attacker_soldier]["health"] -= defender_damage
            if self.attacker.soldiers[attacker_soldier]["health"] <= 0:
                    self.attacker.soldiers[attacker_soldier]["quantity"] -= 1

        if self.attacker.soldiers:
            self.loser = self.defender.username
            self.attacker.budget += 50
            self.defender.budget -= 50
        else:
            self.loser = self.attacker.username
            self.attacker.budget -= 50
            self.defender.budget += 50

def main():
    players = {}
    n = int(input())
    for _ in range(n):
        command = list(input().split())
        if command[0] == "CREATE_USER":
            players[command[1]] = Player(command[1])
            print(Player(command[1]))
        elif command[0] == "BUY":
            players[command[1]].buy_soldier(command[2], command[3])
        elif command[0] == "ATTACK":
            fight = Fight(players[command[1]], players[command[2]])
            fight.battle()
            print(fight)
        elif command[0] == "DAY" and command[1] == "END":
            print("End of the day, players budgets: ", end="")
            for name in players:
                print(players[name].day_end(), end=" ")
            print()
if __name__ == "__main__":
    main()

