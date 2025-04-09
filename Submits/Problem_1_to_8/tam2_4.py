import random
users_dict = {}
class Soldier:
    def __init__(self, soldier_type, price, power, hit_chance, health):
        self.soldier_type = soldier_type
        self.price = price
        self.power = power
        self.hit_chance = hit_chance
        self.health = health
    def __str__(self):
        return self.soldier_type


class User:
    def __init__(self, user_name):
        self.user_name = user_name
        users_dict[user_name] = self
        self.money = 100
        self.bought_soldiers = []
        print(f'Registered {self.user_name} with initial money of {self.money}')
    def __str__(self):
        return self.user_name
    def check_money(self):
        if self.money <= 0:
            users_dict.pop(self.user_name)
            print(self.user_name, 'is Eliminated')
    def buying_soldier(self, soldier_type, quantity):
        soldiers = {'Infantry': Soldier('Infantry',10, 1, 0.8, 3),
                    'Cavalry': Soldier('Cavalry', 25, 2, 0.6, 5),
                    'Archer': Soldier( 'Archer',20, 1.5, 0.75, 2),
                    'Heavy Cavalry': Soldier('Heavy Cavalry', 50, 4, 0.4, 10)}
        if soldier_type in soldiers:
            if self.money > quantity * soldiers[soldier_type].price :
                self.money -= quantity * soldiers[soldier_type].price
                for i in range(quantity):
                    self.bought_soldiers.append(soldiers[soldier_type])
                print(f'{self.user_name} bought {quantity} {soldier_type}')
            else:
                print(f'{self.user_name} does not have enough money')
        else:
            print(f'{soldier_type} is not available')
    def attack(self, defender_username):
        if len(self.bought_soldiers) == 0:
            return f'{self.user_name} does not have any soldiers'
        else:
            attacker = random.choice(self.bought_soldiers)
        if len(defender_username.bought_soldiers) == 0:
            return f'{self.user_name} does not have any soldiers'
        else:
            defender = random.choice(defender_username.bought_soldiers)
        if random.random() <= attacker.hit_chance:
            defender.health -= attacker.power
            if defender.health <= 0 :
                defender_username.bought_soldiers.remove(defender)

def battle(attacker, defender):
    print(attacker, 'and', defender, 'started a battle')
    counter = 0
    while len(attacker.bought_soldiers) != 0 and len(defender.bought_soldiers) != 0:
        if counter % 2 == 0:
            attacker.attack(defender)
        else:
            defender.attack(attacker)
        counter += 1
    if len(attacker.bought_soldiers) != 0:
        print(defender, 'lost the battle')
        defender.money -= 50
        attacker.money += 50
        print(attacker, 'has taken 50 coin from', defender)
        defender.check_money()
    else:
        print(attacker, 'lost the battle')
        defender.money += 50
        attacker.money -= 50
        print(defender, 'has taken 50 coin from', attacker)
        attacker.check_money()
def day_end():
    print('End of the day, players budgets: ', end='')
    for user in users_dict.values():
        user.money += 50
        print(user, ':', user.money, end=' ')
    print()
    for user in users_dict.values():
        user.check_money()


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        command = input()
        if 'CREATE_USER' in command:
            command_list = command.split()
            User(command_list[1])
        elif 'BUY' in command:
            command_list = command.split()
            if command_list[1] in users_dict:
                user_name = command_list[1]
                soldier_type = command_list[2]
                quantity = int(command_list[3])
                users_dict[user_name].buying_soldier(soldier_type, quantity)
            else:
                print('Username not available')
        elif 'ATTACK' in command:
            command_list = command.split()
            if command_list[1] in users_dict and command_list[2] in users_dict:
                attacker = users_dict[command_list[1]]
                defender = users_dict[command_list[2]]
                battle(attacker, defender)
            else:
                print('Username not available')
        elif 'DAY END' in command:
            day_end()




