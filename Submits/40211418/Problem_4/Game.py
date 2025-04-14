from random import random, choice


class Infantry:
    def __init__(self):
        self.name = 'Infantry'
        self.price = 10
        self.power = 1
        self.chance_of_hit = 0.8
        self.health = 3


class Cavalry:
    def __init__(self):
        self.name = 'Cavalry'
        self.price = 25
        self.power = 2
        self.chance_of_hit = 0.6
        self.health = 5


class Archer:
    def __init__(self):
        self.name = 'Archer'
        self.price = 20
        self.power = 1.5
        self.chance_of_hit = 0.75
        self.health = 2


class HeavyCavalry:
    def __init__(self):
        self.name = 'Heavy_Cavalry'
        self.price = 50
        self.power = 4
        self.chance_of_hit = 0.4
        self.health = 10


class User:
    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.army = {}

    def update(self, army):
        self.army = {}
        if army:
            for soldier in army:
                self.army[type(soldier)] = self.army.get(type(soldier), 0) + 1
            self.balance += 50
        else:
            self.balance -= 50
            if self.balance <= 0:
                print(f'{self.name} eliminated')


class Game:
    _users = []
    _soldiers = [Infantry(), Cavalry(), Archer(), HeavyCavalry()]

    @classmethod
    def add_user(cls, name):
        cls._users.append(User(name))
        print(f'User {name} created with initial balance 100')

    @classmethod
    def buy_soldier(cls, user_name, soldier_type, quantity):
        for soldier in cls._soldiers:
            if soldier.name == soldier_type:
                break
        else:
            print(f'Soldier type {soldier_type} not found')
            return

        for user in cls._users:
            if user.name == user_name:
                if user.balance >= soldier.price * quantity:
                    user.army[type(soldier)] = user.army.get(type(soldier), 0) + quantity
                    user.balance -= soldier.price * quantity
                    print(f'{quantity} {soldier_type} bought for {user.name}, user balance: {user.balance}')
                else:
                    print(f'User {user.name} balance is not enough')
                
    @classmethod
    def attack(cls, attacker_name, defender_name):
        attacker = None
        defender = None

        for user in cls._users:
            if user.name == attacker_name:
                attacker = user
            elif user.name == defender_name:
                defender = user

        if not attacker or not defender:
            print('One or both users not found')
            return

        attacker_army = [
            soldier() for soldier, quantity in attacker.army.items() for _ in range(quantity)
        ]
        defender_army = [
            soldier() for soldier, quantity in defender.army.items() for _ in range(quantity)
        ]

        print(f'{attacker_name} and {defender_name} started a battle')

        while attacker_army and defender_army:
            attacker_soldier = choice(attacker_army)
            defender_soldier = choice(defender_army)

            if random() <= attacker_soldier.chance_of_hit:
                defender_soldier.health -= attacker_soldier.power

            if random() <= defender_soldier.chance_of_hit:
                attacker_soldier.health -= defender_soldier.power

            if attacker_soldier.health <= 0:
                attacker_army.remove(attacker_soldier)

            if defender_soldier.health <= 0:
                defender_army.remove(defender_soldier)

        if not attacker_army and not defender_army:
            print("The fight is a draw")
        elif not attacker_army:
            print(f"{attacker.name} lost to {defender.name}")
        else:
            print(f"{defender.name} lost to {attacker.name}")

        attacker.update(attacker_army)
        defender.update(defender_army)

        if attacker.balance <= 0:
            attacker.balance = 0
        if defender.balance <= 0:
            defender.balance = 0

    @classmethod
    def day_end(cls):
        for user in cls._users:
            if user.balance > 0:
                user.balance += 50
        print(
            f'End of the day, players balance: '
            f'{", ".join([f"{user.name}: {user.balance}" for user in cls._users])}'
        )
        not_eliminated_users = [user.name for user in cls._users if user.balance != 0]
        if len(not_eliminated_users) == 1:
            print(f"{not_eliminated_users[0]} wins")


if __name__ == '__main__':
    com = input()
    while com != 'END':
        c = com.split()
        match c[0]:
            case 'CREATE_USER':
                Game.add_user(c[1])
            case 'BUY':
                Game.buy_soldier(c[1], c[2], int(c[3]))
            case 'ATTACK':
                Game.attack(c[1], c[2])
            case 'DAY':
                Game.day_end()
        com = input()

