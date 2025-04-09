import random


class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.money = 100
        self.soldiers = {}
        self.is_eliminated = False

    def user_created(self):
        print(f"Registered {self.user_name} with initial money of {self.money}")

    def edit_money(self, money=50):
        if not self.is_eliminated:
            self.money += money

    def buy_soldier(self, soldier, quantity):
        if isinstance(soldier, Infantry):
            soldier = Infantry()
        elif isinstance(soldier, Cavalry):
            soldier = Cavalry()
        elif isinstance(soldier, Archer):
            soldier = Archer()
        elif isinstance(soldier, HeavyCavalry):
            soldier = HeavyCavalry()
        price = soldier.cost * quantity
        if price >= self.money:
            print("not enough money")
            return False
        else:
            self.soldiers[soldier] = quantity
            self.money -= price
            return True


class Infantry:
    def __init__(self):
        self.name = "infantry"
        self.cost = 10
        self.power = 1
        self.chance = [1, 1, 1, 1, 0]
        self.health = 3

    def can_beat(self):
        return random.choice(self.chance)


class Cavalry:
    def __init__(self):
        self.name = "cavalry"
        self.cost = 25
        self.power = 2
        self.chance = [1, 1, 1, 0, 0]
        self.health = 5

    def can_beat(self):
        return random.choice(self.chance)


class Archer:
    def __init__(self):
        self.name = "archer"
        self.cost = 20
        self.power = 1.5
        self.chance = [1, 1, 1, 0]
        self.health = 2

    def can_beat(self):
        return random.choice(self.chance)


class HeavyCavalry:
    def __init__(self):
        self.name = "heavy_cavalry"
        self.cost = 50
        self.power = 4
        self.chance = [1, 1, 0, 0, 0]
        self.health = 10

    def can_beat(self):
        return random.choice(self.chance)


class Game:
    def __init__(self):
        self.users = {}

    soldiers = {'infantry': Infantry(),
                'cavalry': Cavalry(),
                'archer': Archer(),
                'heavy_cavalry': HeavyCavalry()}

    def add_user(self, user_name, user):
        self.users[user_name] = user

    def attack(self, attacker, defender):
        if any([not attacker.soldiers, not defender.soldiers]):
            print(f"{" and ".join([user.user_name for user in [attacker, defender] if not user.soldiers])}"
                  f" has no soldiers")
            return
        print(f"{attacker.user_name} and {defender.user_name} started a battle")
        attacker_soldier = random.choice(list(attacker.soldiers.keys()))
        defender_soldier = random.choice(list(defender.soldiers.keys()))

        while attacker.soldiers and defender.soldiers:
            print(f"Attacker {attacker.user_name} with {attacker_soldier.name} \n"
                  f"Defender {defender.user_name} with {defender_soldier.name}")
            if attacker_soldier.can_beat():
                defender_soldier.health -= attacker_soldier.power
                print(f"{attacker.user_name} hit {defender.user_name} \n{attacker_soldier.name}"
                      f" health: {attacker_soldier.health} \n"
                      f"{defender_soldier.name} health: {defender_soldier.health}")
            else:
                print(f"{attacker.user_name} couldn't hit {defender.user_name} ")
            if defender_soldier.health <= 0:
                if defender.soldiers[defender_soldier] > 0:
                    defender_soldier.health = self.soldiers[defender_soldier.name].health
                    defender.soldiers[defender_soldier] -= 1
                else:
                    del defender.soldiers[defender_soldier]
                    if not defender.soldiers:
                        break
            attacker_soldier = random.choice(list(defender.soldiers.keys()))
            defender_soldier = random.choice(list(attacker.soldiers.keys()))
            attacker, defender = defender, attacker

        loser = attacker if not attacker.soldiers else defender
        winner = defender if loser == attacker else attacker
        loser.edit_money(-50)
        winner.edit_money(50)
        print(f"{loser.user_name} Lost the battle")
        print(f"{winner.user_name} has taken 50 coins from {loser.user_name}")
        if loser.money <= 0:
            loser.money = 0
            print(f"{loser.user_name} is Eliminated")
            loser.is_eliminated = True

    def day_end(self):
        for user in self.users.values():
            user.edit_money()
        print(f"End of the day, players budgets: "
              f"{", ".join([f"{user.user_name} = {user.money}" for user in self.users.values()])}")

    def buy_soldier(self, soldier_type, quantity, user_name):
        user = self.users[user_name]
        if user.buy_soldier(self.soldiers[soldier_type], quantity):
            print(f"{user_name} bought {quantity} {soldier_type}")


def main():
    command = input().split()
    game = Game()
    while command[0] != "END":
        match command[0]:
            case 'CREATE_USER':
                user_name = command[1]
                user = User(user_name)
                user.user_created()
                game.add_user(user_name, user)
            case 'BUY':
                user_name = command[1]
                soldier_type = command[2]
                quantity = int(command[3])
                game.buy_soldier(soldier_type.lower(), quantity, user_name)
            case 'ATTACK':
                attacker = game.users[command[1]]
                defender = game.users[command[2]]
                game.attack(attacker, defender)
            case 'DAY':
                game.day_end()
            case 'END':
                return
        command = input().split()


if __name__ == '__main__':
    main()

'''doc test case
CREATE_USER Alice
CREATE_USER Bob
BUY Alice Infantry 5
BUY Bob Cavalry 2
ATTACK Alice Bob
DAY END
BUY Bob Archer 3
ATTACK Bob Alice
DAY END
    '''
'''doc output
Registered Alice with initial money of 100
Registered Bob with initial money of 100
Alice bought 5 infantry
Bob bought 2 Cavalry
Alice and Bob started a battle
Bob Lost the battle
Alice has taken 50 coin from Bob
End of the day, players budgets: Alice = 150، Bob = 50
Bob bought 3 Archers
Bob and Alice started a battle
Bob lost the battle
Alice has taken 50 coins from Bob
Bob is Eliminated
End of the day, players budgets: Alice = 200، Bob = 0
'''
'''
README
as written in document when user lose the battle his money should decrease 50 and
the winners money should increase and I made the system working like that but in doc test case 
loser don't lose money first time they start battle and he loses at second time.  
'''
