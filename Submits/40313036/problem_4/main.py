from random import randint, choice
class User:
    def __init__(self, username):
        self.username = username
        self.money = 100
        self.soldiers = []

    def add_soldier(self, name, info, quantity):
        new_soldier = Soldier(name, self.username, info[0], info[1], info[2])
        self.soldiers.append([new_soldier, quantity])

    def __lt__(self, other):
        if len(self.soldiers)*len(other.soldiers) == 0:
            return len(self.soldiers) > len(other.soldiers)
        self_choice = choice(self.soldiers)
        self_soldier = self_choice[0]
        other_choice = choice(other.soldiers)
        other_soldier = other_choice[0]
        while len(self.soldiers)*len(other.soldiers) > 0:
            counter = randint(0, 1)
            while self_soldier.health*other_soldier.health > 0:
                if counter%2 and randint(0, 100) <= self_soldier.probality*100:
                    other_soldier.health -= self_soldier.power
                elif counter%2 == 0 and randint(0, 100) <= other_soldier.probality*100:
                    self_soldier.health -= other_soldier.power
                counter += 1
            if self_soldier.health <= 0:
                if self_choice[1] == 1:
                    for id in range(len(self.soldiers)):
                        if self.soldiers[id][0].name == self_soldier.name:
                            self.soldiers = self.soldiers[:id]+self.soldiers[id+1:]
                else:
                    for id in range(len(self.soldiers)):
                        if self.soldiers[id][0].name == self_soldier.name:
                            self.soldiers[id][1] -= 1
                if len(self.soldiers) == 0: break
                self_choice = choice(self.soldiers)
                self_soldier = self_choice[0]
            if other_soldier.health <= 0:
                if other_choice[1] == 1:
                    for id in range(len(other.soldiers)):
                        if other.soldiers[id][0].name == other_soldier.name:
                            other.soldiers = other.soldiers[:id]+other.soldiers[id+1:]
                else:
                    for id in range(len(other.soldiers)):
                        if other.soldiers[id][0].name == other_soldier.name:
                            other.soldiers[id][1] -= 1
                if len(other.soldiers) == 0: break
                other_choice = choice(other.soldiers)
                other_soldier = other_choice[0]
        return len(self.soldiers) > len(other.soldiers)

class Soldier:
    def __init__(self, name, username, health, probality, power):
        self.name = name
        self.username = username
        self.health = health
        self.probality = probality
        self.power = power

users = {}
info = {
    "Infantry": [10, 3, 0.8, 1],
    "Cavalry": [25, 5, 0.6, 2],
    "Archer": [20, 2, 0.75, 1.5],
    "Heavy-Cavalry": [50, 10, 0.4, 4]
}
while True:
    inp = input(">> ").split()
    if inp[0] == "CREATE_USER":
        users[inp[1]] = User(inp[1])
        print(f"Registered {inp[1]} with initial money of {users[inp[1]].money}")
    elif inp[0] == "BUY":
        if users[inp[1]].money > info[inp[2]][0]*int(inp[3]):
            users[inp[1]].money -= info[inp[2]][0]*int(inp[3])
            users[inp[1]].add_soldier(inp[2], info[inp[2]][1:], int(inp[3]))
            print(f"{inp[1]} bought {inp[3]} {inp[2]}")
        else:
            print("No enough money")
    elif inp[0] == "ATTACK":
        print(f"{inp[1]} and {inp[2]} started a battle")
        if users[inp[1]] < users[inp[2]]:
            print(f"{inp[1]} Lost the battle")
            users[inp[1]].soldiers = []
            users[inp[1]].money -= 50
            users[inp[2]].money += 50
        else:
            print(f"{inp[2]} Lost the battle")
            users[inp[2]].soldiers = []
            users[inp[2]].money -= 50
            users[inp[1]].money += 50
        if users[inp[1]].money == 0:
            users[inp[1]] = None
            print(f"{inp[1]} is Eliminated")
        elif users[inp[2]].money == 0:
            users[inp[2]] = None
            print(f"{inp[2]} is Eliminated")
    elif inp[0] == "DAY" and inp[1] == "END":
        out = ""
        for user in users:
            users[user].money += 50
            out += f"{user} = {users[user].money}, "
        if len(out) > 2: out = out[:-2]
        print(f"End of the day, players budgets: "+out)
    elif inp[0] == "exit":
        break