
class Vehicle:
    def __init__(self,name,fixed_maintenance=0,variable_maintenance=0,fuel=0):
        self.name=name
        self.idd =int(len(vehicles))+1
        self.fixed=fixed_maintenance
        self.var=variable_maintenance
        self.fuel=fuel
        self.total_fuel=0
        self.V_maintenance_cost=0
        if self.name =='PLANE':
            self.fixed = 5000000
            self.var = 2000
            self.max_w = 10000
            self.fuel = 10
        if self.name =='TRUCK':
            self.fixed = 1000000
            self.var = 500
            self.max_w = 5000
            self.fuel = 3
        if self.name == 'PICKUP':
            self.fixed = 800000
            self.var = 300
            self.max_w = 1500
            self.fuel = 2
        if self.name == 'CAR':
            self.fixed = 500000
            self.var = 200
            self.max_w = 500
            self.fuel = 1.5
        vehicles.append(self)
    def travel(self,city1,city2,cargo_weight):
        x1 = dictionary[f'{city1}{city2}']
        if int(cargo_weight) > self.max_w:
            print(f'Cargo heavier than max weight of {self.name}')
            return None
        if self.name=='CAR' or self.name=='PICKUP':
            for f in fuels:
                if f.name=='PETROLEUM':
                    self.total_fuel += f.cost *(x1 * int(self.fuel))
        if self.name == 'PLANE':
            for f in fuels:
                if f.name == 'JET_FUEL':
                    self.total_fuel += f.cost * (x1 * int(self.fuel))
        if self.name == 'TRUCK':
            for f in fuels:
                if f.name == 'DIESEL':
                    self.total_fuel += f.cost * (x1 * int(self.fuel))
        self.V_maintenance_cost += x1 * int(self.var)

vehicles=[]
dictionary={'AB': 100, 'AC':200, 'AD':150, 'AE':300,'BC':250,'BD':180,'BE':400,'CD':120,'CE':350,'DE':280 }

def costs():
    total, fuel , fixed_m= 0 , 0 , 0
    var_m =0
    for item in vehicles:
        fuel += int(item.total_fuel)
        fixed_m += int(item.fixed)
        var_m += int(item.V_maintenance_cost)
        total +=int(item.total_fuel)+ int(item.V_maintenance_cost) + int(item.fixed)
    return [total,fuel,fixed_m,var_m]

class Fuels:
    def __init__(self,name,cost):
        self.cost=cost
        self.name=name
        @property
        def name(n):
            return self.name
        @name.setter
        def name(n):
            for item in fuels:
                if item._name == n:
                    print(f'new price can not be assigned to {name}')
                    return self.name
            self._name = n
            return self.name

        fuels.append(self)
fuels=[]

l=[]
x=input()
while( True):
    l.append(x)
    x= input()
    if (not x):
        break
for items in l:
    y=items.split(' ')
    if y[0] == 'ADD_TRIP':
        car_id = y[1]
        start = y[2]
        destination = y[3]
        cargo_w = y[4]
        for it in vehicles:
            if int(it.idd) == int(car_id):
                it.travel(start,destination,cargo_w)
    if y[0] == 'ADD_VEHICLE':
        z=Vehicle(y[1],int(y[2]),int(y[3]),int(y[4]))
        print(f'Vehicle {y[1]} added with fixed cost {z.fixed}, var. cost per km {z.var} with id {z.idd}')
    if y[0] == 'END_MONTH':
        z=costs()
        print(f'Total operational cost : {z[0]}')
        print(f'Total fixed maintenance cost : {z[2]}')
        print(f'Total variable maintenance cost : {z[3]}')
        print(f'Total fuel cost : {z[1]}')
    if y[0] == 'SET_FUEL_PRICE':
        Fuels(y[1],int(y[2]))
