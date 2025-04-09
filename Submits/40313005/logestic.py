from abc import ABC
import random

class logistic(ABC):
    def __init__(self, maintenance,km_maintenance,fuel,max_weight,fuel_name):
        self.maintenance = maintenance
        self.fuel = fuel
        self.max_weight = max_weight
        self.km_maintenance = km_maintenance
        self.ID = random.randint(0,500)
        self.fuel_cost = 0
        self.km_maintenance_cost =0
        self.fixed_cost=0
        self.fuel_name = fuel_name
    def init_massage(self):
        print(f"Vehicle {self.__class__.__name__}(ID:{self.ID}) added with fixed cost: {self.maintenance} , variable cost per km: {self.km_maintenance}")\
        
    def trip(self,distance,A,B,weight):
        if weight > self.max_weight:
            print("Invalid trip!")
        else:
            self.fixed_cost += self.maintenance
            self.fuel_cost += distance*fuel_price[self.fuel_name]*self.fuel
            self.km_maintenance_cost += self.km_maintenance * distance
            print(f"Trip registered:  {self.__class__.__name__} from {A} to {B} carrying {weight} kg.({distance}KM)")
class Truck(logistic):
    def __init__(self):
        super().__init__(1_000_000,500,3, 5_000,"DIESEL")

class Airplane(logistic):
    def __init__(self):
        super().__init__(5_000_000, 2_000 ,10, 10_000,"JET_FUEL")

class Pickup(logistic):
    def __init__(self):
        super().__init__(800_000, 300 ,2, 1_500,"Petrol")

class Car(logistic):
    def __init__(self):
        super().__init__(500_000, 200 ,1.5, 500,"Petrol")


logistic_list = []
fuel_price={"DIESEL":0,"JET_FUEL":0,"Petrol":0}
cities = ["A","B","C","D","E"]
distance_matrix = [[0,100,200,150,300],[100,0,250,180,400],[200,250,0,120,350],[150,180,120,0,280],[300,400,350, 280 ,0]]

while(True):
    command = input().split()
    match command[0]:
        case "ADD_VEHICLE":
            match command[1]:
                case "CAR":
                    new_logistic = Car()
                case "PICKUP":
                    new_logistic = Pickup()
                case "TRUCK":
                    new_logistic = Truck()
                case "PLANE":
                    new_logistic = Airplane()
            new_logistic.init_massage()
            logistic_list.append(new_logistic)
        case "ADD_TRIP":
            for vehicle in logistic_list:
                if vehicle.ID == int(command[1]):
                    vehicle.trip(distance_matrix[cities.index(command[2])][cities.index(command[3])],command[2],command[3],int(command[4]))
        case "END_MONTH":
            print("End of month report:")
            fuel_cost = 0
            km_maintenance_cost =0
            fixed_cost=0
            total = 0
            print("Detailed costs:")
            for vehicle in logistic_list:
                print(f"  {vehicle.__class__.__name__} (ID: {vehicle.ID})")
                print(f"    Fixed maintenance:{vehicle.fixed_cost}")
                print(f"    Variable maintenance:{vehicle.km_maintenance_cost}")
                print(f"    Fuel cost:{vehicle.fuel_cost}")
                fixed_cost += vehicle.fixed_cost
                km_maintenance_cost += vehicle.km_maintenance_cost
                fuel_cost += vehicle.fuel_cost
                total += fixed_cost + km_maintenance_cost + fixed_cost
            print("_______________TOTAL_______________")
            print(f"Total fixed maintenance cost:{fixed_cost}")
            print(f"Total variable maintenance cost:{km_maintenance_cost}")
            print(f"Total fuel cost:{fuel_cost}")
            print(f"Total operational cost: {total}")



        case "SET_FUEL_PRICE":
            fuel_price[command[1]]=int(command[2])
            print(f"Fuel price for {command[1]} set to {command[2]} per liter")