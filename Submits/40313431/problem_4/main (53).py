import random


class User:
    kind_soldier = {'Infantry': 10, 'Cavalry': 25, 'Archer': 20, 'Heavy Cavalry': 50}

    def __init__(self, name, cavalry='none', number_cavalry=0, infantry='non', number_infantry=0, archer='non',
                 number_archer=0, heavy='non', number_heavy=0, money=100, lis_soldier=None):
        if lis_soldier is None:
            lis_soldier = []
        self.cavalry = cavalry
        self.number_cavalry = number_cavalry
        self.infantry = infantry
        self.number_infantry = number_infantry
        self.archer = archer
        self.number_archer = number_archer
        self.heavy = heavy
        self.number_heavy = number_heavy
        self.money = money
        self.lis_soldier = lis_soldier
        self.name = name

    def end_day(self):
        self.money += 50


def attack(a, b, lis):
    a1 = a
    b1 = b
    m1 = 0
    m2 = 0
    helath = 0
    health2 = 0
    power1 = 0
    power2 = 0
    chance1 = 0
    chance2 = 0
    sarbaz = 0
    sarbaz2 = 0
    for i in range(len(lis)):
        if lis[i].name == a:
            m1 = i
    for i in range(len(lis)):
        if lis[i].name == b:
            m2 = i
    while (len(lis[m1].lis_soldier) != 0) and (len(lis[m2].lis_soldier) != 0):
        r = random.random()
        for i in range(len(lis)):
            if lis[i].name == a:
                k1 = i
                sarbaz = random.choice(lis[i].lis_soldier)
                helath = 0
                health2 = 0
                power1 = 0
                power2 = 0
                chance1 = 0
                chance2 = 0
                if sarbaz[0] == 'Cavalry':
                    power1 = 2
                    chance1 = 0.6
                elif sarbaz[0] == 'Infantry':
                    power1 = 1
                    chance1 = 0.8
                elif sarbaz[0] == 'Archer':
                    power1 = 1.5
                    chance1 = 0.75
                elif sarbaz[0] == 'HeavyCavalry':
                    power1 = 4
                    chance1 = 0.4
        for i in range(len(lis)):
            if lis[i].name == b:
                k = i
                sarbaz2 = random.choice(lis[i].lis_soldier)
                if sarbaz2[0] == 'Cavalry':
                    power2 = 2
                    chance2 = 0.6
                elif sarbaz2[0] == 'Infantry':
                    power2 = 1
                    chance2 = 0.8
                elif sarbaz2[0] == 'Archer':
                    power2 = 1.5
                    chance2 = 0.75
                elif sarbaz2[0] == 'HeavyCavalry':
                    power2 = 4
                    chance2 = 0.4

        if r <= chance1:
            sarbaz2[1] -= power1
            if sarbaz2[1] <= 0:
                if sarbaz2[0] == 'Cavalry':
                    lis[k].number_cavalry -= 1
                elif sarbaz2[0] == 'Infantry':
                    lis[k].number_infantry -= 1
                elif sarbaz2[0] == 'Archer':
                    lis[k].number_archer -= 1
                elif sarbaz2[0] == 'HeavyCavalry':
                    lis[k].number_heavy -= 1

               
                new_list = []
                for soldier in lis[k].lis_soldier:
                    if soldier != sarbaz2:
                        new_list.append(soldier)
                lis[k].lis_soldier = new_list

        temp = a
        a = b
        b = temp

    for i in range(len(lis)):
        if lis[i].name == a1:
            k1 = i
    for i in range(len(lis)):
        if lis[i].name == b1:
            k = i
            break
    if len(lis[m1].lis_soldier) == 0:
        loser = a1
        winner = b1
        loser_index = m1
        winner_index = m2
    else:
        loser = b1
        winner = a1
        loser_index = m2
        winner_index = m1
    loss_amount = min(50, lis[winner_index].money)

    lis[loser_index].money -= loss_amount
    lis[winner_index].money += loss_amount

    return f"{loser} lost the battle\n"


request = input()
user_list = []
finalr = ""
kind_soldier = {'Infantry': 10, 'Cavalry': 25, 'Archer': 20, 'Heavy Cavalry': 50}
while request != 'END':
    desireresult = ""

    if 'CREATE_USER' in request:
        p = request.split()
        z = User(p[1])
        user_list.append(z)
        finalr += f"Registered  {p[1]} with initial money of 100"

    if 'BUY' in request:
        p = request.split()
        for i in range(len(user_list)):
            if p[1] == user_list[i].name:
                if p[2] == 'Cavalry':
                    if (float(user_list[i].money) - int(p[3]) * 25) > 0:
                        user_list[i].cavalry = p[2]
                        user_list[i].number_cavalry = int(p[3])
                        for _ in range(int(p[3])):
                            user_list[i].lis_soldier.append([p[2], 5])
                        user_list[i].money -= int(p[3]) * 25
                        finalr += f" {p[1]} bought {p[3]} {p[2]}"
                elif p[2] == 'Infantry':
                    if (float(user_list[i].money) - int(p[3]) * 10) > 0:
                        user_list[i].infantry = p[2]
                        user_list[i].number_infantry = int(p[3])

                        for _ in range(int(p[3])):
                            user_list[i].lis_soldier.append([p[2], 3])

                        user_list[i].money -= int(p[3]) * 10
                        finalr += f" {p[1]} bought {p[3]} {p[2]}"
                elif p[2] == 'Archer':
                    if (float(user_list[i].money) - int(p[3]) * 20) > 0:
                        user_list[i].archer = p[2]
                        user_list[i].number_archer = int(p[3])
                        for _ in range(int(p[3])):
                            user_list[i].lis_soldier.append([p[2], 2])
                        user_list[i].money -= int(p[3]) * 20
                        finalr += f" {p[1]} bought {p[3]} {p[2]}"
                elif p[2] == 'HeavyCavalry':
                    if (float(user_list[i].money) - int(p[3]) * 50) > 0:
                        user_list[i].heavy = p[2]
                        user_list[i].number_heavy = int(p[3])
                        for _ in range(int(p[3])):
                            user_list[i].lis_soldier.append([p[2], 10])
                        user_list[i].money -= int(p[3]) * 50
                        finalr += f" {p[1]} bought {p[3]} {p[2]}"

    if 'ATTACK' in request:
        p = request.split()
        finalr += f"{p[1]} and {p[2]} started a battle\n"
        m = attack(p[1], p[2], user_list)
        finalr += m
        e = m.split()
        if e[0] == p[1]:
            finalr += f"{p[2]} has taken 50 coin from {p[1]}\n"
            for i in range(len(user_list)):
                if user_list[i].name == p[1]:
                    if user_list[i].money <= 0:
                        finalr += f"{p[1]} is Eliminated\n"
                        user_list.pop(i)
                        break
        elif e[0] == p[2]:
            finalr += f"{p[1]} has taken 50 coin from {p[2]}\n"
            for i in range(len(user_list)):
                if user_list[i].name == p[2]:
                    if user_list[i].money <= 0:
                        finalr += f"{p[2]} is Eliminated\n"
                        user_list.pop(i)
                        break

       
        if not user_list:
            break

    if request == 'DAY END':
        for i in range(len(user_list)):
            user_list[i].end_day()
        finalr += 'End of the day,players budgets :'
        for i in range(len(user_list)):
            finalr += f'{user_list[i].name} = {user_list[i].money}  ,'
        finalr += f"\n"

    request = input()
    if request == 'END':  
        break
    finalr += "\n"

print(finalr)