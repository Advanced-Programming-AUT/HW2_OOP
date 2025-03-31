class Vehicle:
    fuels = {}
    id = 1

    def __init__(self, vehicle_type, fixed_cost, var_cost, fuel_costs):
        self.type = vehicle_type
        self.fixed_cost = fixed_cost
        self.var_cost = var_cost
        self.fuel_costs = fuel_costs
        self.distance = 0
        self.id = Vehicle.id
        Vehicle.id += 1
        self.set_fuel()
        self.set_max_weight()

    def set_fuel(self):
        match self.type:
            case 'PLANE':
                self.fuel = 'JET_FUEL'
            case 'TRUCK':
                self.fuel = 'DIESEL'
            case 'CAR':
                self.fuel = 'PETROL'
            case 'PICKUP':
                self.fuel = 'PETROL'

    def set_max_weight(self):
        match self.type:
            case 'PLANE':
                self.max_weight = 10000
            case 'TRUCK':
                self.max_weight = 5000
            case 'CAR':
                self.max_weight = 500
            case 'PICKUP':
                self.max_weight = 1500

    @classmethod
    def set_fuel_price(cls, fuel_type, price):
        cls.fuels[fuel_type] = price
        print(f"Fuel price for {fuel_type} set to {price} per liter.")

    def calculate_var_cost(self):
        return self.var_cost * self.distance
    
    def calculate_fuel_cost(self):
        return self.fuel_costs * self.distance * Vehicle.fuels[self.fuel]
    

class Logistic:
    vehicles = []
    citys = {
    'A' : {'B': 100, 'C': 200, 'D': 150, 'E': 300},
    'B' : {'A': 100, 'C': 250, 'D': 180, 'E': 400},
    'C' : {'A': 200, 'B': 250, 'D': 120, 'E': 350}, 
    'D' : {'A': 150, 'B': 180, 'C': 120, 'E': 280}, 
    'E' : {'A': 300, 'B': 400, 'C': 350, 'D': 280},
}

    @classmethod
    def add_vehicle(cls, vehicle_type, fixed_cost, var_cost, fuel_cons):
        vehicle = Vehicle(vehicle_type, fixed_cost, var_cost, fuel_cons)
        cls.vehicles.append(vehicle)
        print(f"Vehicle {vehicle_type} added: ID: {vehicle.id}, fixed_cost: {vehicle.fixed_cost}, "
              f"variable cost per km: {vehicle.var_cost}"
            )

    @classmethod
    def add_trip(cls, vehicle_id, origin, dest, cargo):
        flag = 0
        for vehicle in cls.vehicles:
            if vehicle.id == vehicle_id:
                flag = 1
                if cargo <= vehicle.max_weight:
                    vehicle.distance = cls.citys[origin][dest]
                    print(f"Trip registered: {vehicle.type} with Vehicle_ID : {vehicle.id} "
                      f"from {origin} to {dest} carring {cargo} kg"
                    )
                else:
                    print(f"Could not register Trip: weight is higher than maximum")
        if not flag:
            print("vehicle not found")

    @classmethod
    def end_month(cls):
        fixed_cost = sum(vehicle.fixed_cost for vehicle in cls.vehicles)
        var_cost = sum(vehicle.calculate_var_cost() for vehicle in cls.vehicles)
        fuel_cost = sum(vehicle.calculate_fuel_cost() for vehicle in cls.vehicles)
        print("End of month report")
        print(f"Total fixed maintenance cost: {fixed_cost:,}")
        print(f"Total variable maintenance cost: {var_cost:,}")
        print(f"Total fuel cost:: {fuel_cost:,}")
        print(f"Total operational cost: {fixed_cost + var_cost + fuel_cost:,}")
        print("Detailed costs:")
        for vehicle in cls.vehicles:
            print(f"{vehicle.type} (ID: {vehicle.id})")
            print(f"Fixed maintenance: {vehicle.fixed_cost:,}")
            print(f"Variable maintenance: {vehicle.calculate_var_cost():,}")
            print(f"Fuel cost: {vehicle.calculate_fuel_cost():,}")


if __name__ == "__main__":
    command = input()
    while command != "END_MONTH":
        com = command.split()
        match com[0]:
            case 'ADD_VEHICLE':
                Logistic.add_vehicle(com[1], int(com[2]), int(com[3]), int(com[4]))
            case 'SET_FUEL_PRICE':
                Vehicle.set_fuel_price(com[1], int(com[2]))
            case 'ADD_TRIP':
                Logistic.add_trip(int(com[1]), com[2], com[3], int(com[4]))
            case _:
                print('error')
            
        command = input()
    Logistic.end_month()