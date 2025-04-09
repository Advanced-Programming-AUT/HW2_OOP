import random
war_prize = 50


class User:
    def __init__(self, username, soldiers, money):
        self.username = username
        self.soldiers = soldiers
        self.money = money

    def add_money(self, money):
        self.money += money

    def add_soldiers(self, soldier, count):
        if self.money >= soldier.cost * count:
            for i in range(count):
                self.soldiers.append(soldier)
            self.money -= soldier.cost * count
            print(f"{self.username}: You bought {count} {soldier}!")
        else:
            print(f"{self.username}: You don't have enough money!")

    def war(self, other, prize):
        self_army = self.soldiers
        other_army = other.soldiers

        while len(self_army) > 0 and len(other_army) > 0:
            if random.choice([True, False]):
                random.choice(self_army).battle(random.choice(other_army))
            else:
                random.choice(other_army).battle(random.choice(self_army))

            self_army = [soldier for soldier in self_army if soldier.health > 0]
            other_army = [soldier for soldier in other_army if soldier.health > 0]

        if len(self_army) == 0:
            print(f"{other.username}: Win the Battle")
            other.money += prize
            self.money -= prize
            print(f"{other.username}: has taken 50 coins from {self.username}!")
        elif len(other_army) == 0:
            print(f"{self.username}: Win the Battle")
            self.money += prize
            other.money -= prize
            print(f"{self.username}: has taken 50 coins from {other.username}!")


class Soldiers:
    def __init__(self, cost, power, accuracy, health):
        self.cost = cost
        self.power = power
        self.accuracy = accuracy
        self.health = health

    def battle(self, other):
        chance = random.randint(0, 100)
        if chance < self.accuracy:
            other.health -= self.power


class Infantry(Soldiers):
    def __init__(self):
        super().__init__(10, 1, 0.8, 3)

    def __str__(self):
        return "Infantry"


class Cavalry(Soldiers):
    def __init__(self):
        super().__init__(25, 2, 0.6, 5)

    def __str__(self):
        return "Cavalry"


class Archer(Soldiers):
    def __init__(self):
        super().__init__(20, 1.5, 0.75, 2)

    def __str__(self):
        return "Archer"


class HeavyCavalry(Soldiers):
    def __init__(self):
        super().__init__(50, 4, 0.4, 10)

    def __str__(self):
        return "Heavy Cavalry"


def main():
    user_list = []
    x = 3
    initial_budget = 200
    end_day_money = 50
    while len(user_list) != x:
        for user in user_list:
            if user.money == 0:
                print(f"{user.username}: Eliminated!")
                user_list.remove(user)

        cmd = input()
        cmd = cmd.split()
        if cmd[0] == "CREATE_USER":
            new_user = User(cmd[1], [], initial_budget)
            user_list.append(new_user)
            print(f"Registered {new_user.username} with initial money of {new_user.money} ")

        if cmd[0] == "BUY":
            user = ""
            for users in user_list:
                if users.username == cmd[1]:
                    user = users
            if cmd[2] == "Infantry":
                user.add_soldiers(Infantry(), int(cmd[3]))
            elif cmd[2] == "Archer":
                user.add_soldiers(Archer(), int(cmd[3]))
            elif cmd[2] == "Cavalry":
                user.add_soldiers(Cavalry(), int(cmd[3]))
            elif cmd[2] == "HeavyCavalry":
                user.add_soldiers(HeavyCavalry(), int(cmd[3]))

        if cmd[0] == "ATTACK":
            attacker = ""
            defender = ""
            for users in user_list:
                if users.username == cmd[1]:
                    attacker = users
                if users.username == cmd[2]:
                    defender = users
            print(f"{attacker.username} and {defender.username} started a battle")
            attacker.war(defender, war_prize)
        if cmd[0] == "DAY":
            for users in user_list:
                users.add_money(end_day_money)
            print("End of Day! : Players Budget : ", end="")
            for user in user_list:
                print(f"{user.username}: {user.money} ", end="")

        if len(user_list) > 1:
            x = 1


main()
