import sys, os
from random import random, randrange

original_stdout = sys.stdout

os.remove('output.txt')

file1 = open('input.txt', 'r')
file2 = open('output.txt', 'a')

sys.stdout = file2

# ---------- Main Code ----------

class Soldier:
    Soldiers = {'Infantry': (10, 1, 0.8, 3),
                'Cavalry': (25, 2, 0.6, 5),
                'Archer': (20, 1.5, 0.75, 2),
                'Heavy Cavalry': (10, 4, 0.4, 10)}

    def __init__(self, name):
        self.name, self.price, self.power, self.chance, self.health = tuple([name]) + Soldier.Soldiers[name]

    def decrease_health(self, damage):
        self.health -= damage

    def copy(self):
        soldier = Soldier(self.name)
        soldier.name, soldier.price, soldier.power, soldier.chance, soldier.health = self.name, self.price, self.power, self.chance, self.health
        return soldier

class User:
    initial_money = 100
    initial_winner_money = 49

    def __init__(self, username):
        self.__username = username
        self.__money = User.initial_money
        self.__soldiers = []

    @property
    def username(self):
        return self.__username

    @property
    def soldiers(self):
        return self.__soldiers

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    def increase_money(self, money):
        self.__money += money

    def decrease_money(self, money):
        self.__money -= money

    def __str__(self):
        return self.__username

    def buy(self, name, quantity):
        if self.__money >= Soldier.Soldiers[name][0] * quantity:
            self.__soldiers += [Soldier(name)] * quantity
            self.__money -= Soldier.Soldiers[name][0] * quantity
            print(f'{self.__username} bought {quantity}x {name}.')
        else:
            print(f'{self.__username} has not enough money to buy {quantity}x {name}.')

    def remove(self, name):
        for soldier in self.__soldiers:
            if soldier.name == name:
                self.__soldiers.remove(soldier)
                return

        print(f'{self.__username} has not a {name}.')

    def attack(self, other):
        attacker_soldiers = [soldier.copy() for soldier in self.__soldiers]
        defender_soldiers = [soldier.copy() for soldier in other.soldiers]

        turn = 0
        while len(attacker_soldiers) and len(defender_soldiers):
            i = randrange(len(attacker_soldiers))
            j = randrange(len(defender_soldiers))

            if turn == 0 and random() < attacker_soldiers[i].chance:
                defender_soldiers[j].decrease_health(attacker_soldiers[i].power)
                if defender_soldiers[j].health <= 0:
                    defender_soldiers.pop(j)
            if turn == 1 and random() < defender_soldiers[j].chance:
                attacker_soldiers[i].decrease_health(defender_soldiers[j].power)
                if attacker_soldiers[i].health <= 0:
                    attacker_soldiers.pop(i)

            turn = 1 - turn

        if len(attacker_soldiers):
            print(f'{other.username} lost the battle.')
            self.increase_money(User.initial_winner_money)
            other.decrease_money(User.initial_winner_money)
            print(f'{self.__username} has taken {User.initial_winner_money} coin from {other.username}.')
        if len(defender_soldiers):
            print(f'{self.__username} lost the battle.')
            other.increase_money(User.initial_winner_money)
            self.decrease_money(User.initial_winner_money)
            print(f'{other.username} has taken {User.initial_winner_money} coin from {self.__username}.')

class Game:
    initial_increase_money = 50

    def __init__(self):
        self.__users = dict()

    def create_user(self, username):
        if username in self.__users:
            print(f'{username} has already been taken.')
        else:
            self.__users[username] = User(username)
            print(f'Registered {username} with initial money of {User.initial_money}')

    def buy(self, username, name, quantity):
        if username not in self.__users:
            print(f'{username} has not found.')
        else:
            self.__users[username].buy(name, quantity)

    def day_end(self):
        print('End of the day, players budgets:', end = ' ')
        for user in self.__users.values():
            user.increase_money(Game.initial_increase_money)
            print(f'{user} = {user.money},', end = ' ')
        print()

    def remove_user(self, username):
        if username not in self.__users:
            print(f'{username} has not found.')
        else:
            print(f'{username} is Eliminated.')
            del self.__users[username]

    def attack(self, attacker, defender):
        if attacker not in self.__users:
            print(f'{attacker} has not found.')
        if defender not in self.__users:
            print(f'{defender} has not found.')
        if attacker in self.__users and defender in self.__users:
            print(f'{attacker} and {defender} started a battle.')
            self.__users[attacker].attack(self.__users[defender])

            if self.__users[attacker].money <= 0:
                self.remove_user(attacker)
            if self.__users[defender].money <= 0:
                self.remove_user(defender)

def combine(*args):
    ans = ''
    for string in args:
        ans += str(string) + ' '
    return ans.strip()

if __name__ == '__main__':
    game = Game()
    while 1:
        command = file1.readline().strip()
        command = [line.strip() for line in list(command.split(' ')) if line.strip()]

        if len(command) == 0:
            break

        if command[0] == 'CREATE_USER':
            game.create_user(command[1])
        elif command[0] == 'ATTACK':
            game.attack(command[1], command[2])
        elif command[0] == 'BUY':
            game.buy(command[1], combine(*command[2:len(command) - 1]), int(command[-1]))
        else:
            game.day_end()

# ---------- End of Main Code ----------

sys.stdout = original_stdout

file1.close()
file2.close()