import random
class Gameplay:
    def __init__(self,name,initial_money=100):
        self.name=name
        self.credit = initial_money
        self.soldierlist=[]
        print(f'created {self.name} with initial money {self.credit}')
        gamer_list.append(self)
    @staticmethod
    def daily_credit_rise():
        for th in gamer_list:
            th.credit += 50
            print(f'{th.name} received a 50 dollar increase total:{th.credit}')
    def purchase_soldier(self,chosensoldier,number):
       for i in s:
                if i.expertise==chosensoldier:
                    if self.credit > i.cost * number:
                        self.credit -= i.cost * number
                        for j in range(number):
                            self.soldierlist.append(i)
                        print(f'{self.name} bought {number}x {chosensoldier} successfully')
                    else:
                        print('not enough money')
    def attack(self,other):
        print(f'battle started between {self.name} and {other.name} ')
        while(len(self.soldierlist) > 0 and len(other.soldierlist) > 0):
            x = random.randint(0,int(len(self.soldierlist)))
            x2 = x % int(len(self.soldierlist))
            y = random.randint(0,int(len(other.soldierlist)))
            y2 = y % int(len(other.soldierlist))
            if (self.soldierlist[x2]).binary_strike() == 1:
                other.soldierlist[y2].strength -= self.soldierlist[x2].power

            for items in other.soldierlist:
                if int(items.strength) <= 0:
                    other.soldierlist.remove(items)
                    print(f'{other.name} lost a/an {items.expertise}')

            if int(len(self.soldierlist))==0 or int(len(other.soldierlist))== 0:
                break
            z = random.randint(0, int(len(other.soldierlist)))
            z2 = z % int(len(other.soldierlist))
            w = random.randint(0, int(len(self.soldierlist)))
            w2 = w % int(len(self.soldierlist))
            if (other.soldierlist[z2]).binary_strike() == 1:
                self.soldierlist[w2].strength -= other.soldierlist[z2].power

            for ite in self.soldierlist:
                 if int(ite.strength) == 0:
                    self.soldierlist.remove(ite)
                    print(f'{self.name} lost a/an {ite.expertise}')

        if len(self.soldierlist) == 0:
            print(f'{other.name} won the battle')
            other.credit += 60
            self.credit -= 60
            print(f'{self.name} lost $60 to opponent {other.name}')
        elif len(other.soldierlist) == 0:
            print(f'{self.name} won the battle')
            self.credit += 60
            other.credit -= 60
            print(f'{other.name} lost $60 to opponent {self.name}')
        if self.credit <= 0:
            print(f'{self.name} is eliminated')
            gamer_list.remove(self)
        if other.credit == 0:
            print(f'{other.name} is eliminated')
            gamer_list.remove(other)
        if len(gamer_list) == 1:
            print(f'{gamer_list[0].name} is the overall winner with remaining credit {gamer_list[0].credit}')

gamer_list=[]
class Soldiers:
    def __init__(self,expertise,cost,power,strike_chance,strength):
        self.expertise=expertise
        self.cost=cost
        self.power=power
        self.prob=strike_chance
        self.strength=strength

    def binary_strike(self):
        r=random.random()
        if r<=self.prob:
            return 1
        else:
            return 0

s=[]
s.append(Soldiers('Infantry',10,1,0.8,3))
s.append(Soldiers('Cavalry',25,2,0.6,5))
s.append(Soldiers('Archer',20,1.5,0.75,2))
s.append(Soldiers('Heavy Cavalry',50,4,0.4,10))

'''Test:
g1=Gameplay('bob',200)
g2=Gameplay('alison',300)
g1.purchase_soldier('Archer',2)
g1.purchase_soldier('Cavalry',2)
g2.purchase_soldier('Cavalry',3)
g1.attack(g2)
Gameplay.daily_credit_rise()'''

l=[]
x=input()
while (True):
    if not x:
        break
    else:
        l.append(x)
        x=input()
for item in l:
    y=item.split()
    match y[0]:
        case 'CREATE_USER':
            Gameplay(y[1])
        case 'BUY':
            for it in gamer_list:
                if it.name == y[1]:
                    it.purchase_soldier(y[2],int(y[3]))
        case 'ATTACK':
            print(':)')
            for t in gamer_list:
                if t.name == y[1]:
                    for k in gamer_list:
                        if k.name == y[2]:
                            t.attack(k)
        case 'DAY':
            if y[1] == 'END':
                Gameplay.daily_credit_rise()
