from random import randint, choice

class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 100
        self.army = []

    def recruit(self, unit_type, stats, count):
        unit = Unit(unit_type, self.name, stats[0], stats[1], stats[2])
        self.army.append([unit, count])

    def __lt__(self, opponent):
        if not self.army or not opponent.army:
            return len(self.army) > len(opponent.army)

        my_unit, my_qty = choice(self.army)
        enemy_unit, enemy_qty = choice(opponent.army)

        while self.army and opponent.army:
            turn = randint(0, 1)
            while my_unit.health > 0 and enemy_unit.health > 0:
                if turn % 2 == 1 and randint(0, 100) <= my_unit.accuracy * 100:
                    enemy_unit.health -= my_unit.strength
                elif turn % 2 == 0 and randint(0, 100) <= enemy_unit.accuracy * 100:
                    my_unit.health -= enemy_unit.strength
                turn += 1

            if my_unit.health <= 0:
                self._remove_unit(my_unit, my_qty)

                if not self.army: break
                my_unit, my_qty = choice(self.army)

            if enemy_unit.health <= 0:
                opponent._remove_unit(enemy_unit, enemy_qty)

                if not opponent.army: break
                enemy_unit, enemy_qty = choice(opponent.army)

        return len(self.army) > len(opponent.army)

    def _remove_unit(self, unit, quantity):
        for i, (soldier, qty) in enumerate(self.army):
            if soldier.name == unit.name:
                if quantity == 1:
                    del self.army[i]
                else:
                    self.army[i][1] -= 1
                break


class Unit:
    def __init__(self, name, owner, health, accuracy, strength):
        self.name = name
        self.owner = owner
        self.health = health
        self.accuracy = accuracy
        self.strength = strength


def main():
    players = {}
    unit_info = {
        "Infantry": [10, 0.8, 3],
        "Cavalry": [25, 0.6, 5],
        "Archer": [20, 0.75, 2],
        "Heavy-Cavalry": [50, 0.4, 10]
    }

    while True:
        cmd = input().split()
        if not cmd:
            continue

        action = cmd[0]

        if action == "CREATE_USER":
            name = cmd[1]
            players[name] = Player(name)
            print(f"{name} registered with ${players[name].balance}")
        
        elif action == "BUY":
            user, unit, qty = cmd[1], cmd[2], int(cmd[3])
            cost = unit_info[unit][0] * qty
            if players[user].balance >= cost:
                players[user].balance -= cost
                players[user].recruit(unit, unit_info[unit][1:], qty)
                print(f"{user} purchased {qty} {unit}")
            else:
                print("Insufficient funds")

        elif action == "ATTACK":
            attacker, defender = cmd[1], cmd[2]
            print(f"Battle initiated between {attacker} and {defender}")

            if players[attacker] < players[defender]:
                print(f"{attacker} lost the battle")
                players[attacker].army.clear()
                players[attacker].balance -= 50
                players[defender].balance += 50
            else:
                print(f"{defender} lost the battle")
                players[defender].army.clear()
                players[defender].balance -= 50
                players[attacker].balance += 50

            for p in (attacker, defender):
                if players[p].balance <= 0:
                    print(f"{p} has been eliminated")
                    players[p] = None

        elif action == "DAY" and cmd[1] == "END":
            summary = []
            for p in list(players):
                if players[p]:
                    players[p].balance += 50
                    summary.append(f"{p} = {players[p].balance}")
            print("End of the day, players' balances: " + ", ".join(summary))

        elif action == "exit":
            break


if __name__ == "__main__":
    main()

