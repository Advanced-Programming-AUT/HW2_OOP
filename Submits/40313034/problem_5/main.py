import sys, os

original_stdout = sys.stdout

os.remove('output.txt')

file1 = open('input.txt', 'r')
file2 = open('output.txt', 'a')

sys.stdout = file2

# ---------- Main Code ----------

class Vehicle:
    ID = 0
    MaximumPortableWeight = {'CAR': 500, 'TRUCK': 5000, 'PICKUP': 1500, 'PLANE': 10000}
    FuelType = {'CAR': 'GASOLINE', 'PICKUP': 'GASOLINE', 'TRUCK': 'DIESEL', 'PLANE': 'JET_FUEL'}

    def __init__(self, type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        # type is one of ['CAR', 'TRUCK', 'PLANE', 'PICKUP']

        if type not in Vehicle.FuelType:
            print('Vehicle type is incorrect!')
            return

        Vehicle.ID += 1
        self.ID = Vehicle.ID

        self.type = type
        self.fixed_cost = fixed_cost
        self.variable_cost_per_km = variable_cost_per_km
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.variable_maintenance = 0
        self.fuel_cost = 0

        print(f'Vehicle {self.type} (ID: {self.ID}) added with {self.fixed_cost = }, {self.variable_cost_per_km = }, and {self.fuel_consumption_per_km = }.')

    def add_trip(self, cargo_distance, cargo_weight, cargo_fuel_price):
        if cargo_weight > Vehicle.MaximumPortableWeight[self.type]:
            print(f'Vehicle {self.type} maximum portable weight is {Vehicle.MaximumPortableWeight[self.type]}!')
            return

        self.variable_maintenance += self.variable_cost_per_km * cargo_distance
        self.fuel_cost += self.fuel_consumption_per_km * cargo_distance * cargo_fuel_price

    def out(self):
        print(f'  {self.type} (ID: {self.ID}):')
        print(f'    Fixed maintenance: {self.fixed_cost}')
        print(f'    Variable maintenance: {self.variable_maintenance}')
        print(f'    Fuel cost: {self.fuel_cost}')

class Logistic:
    Distances = ((0, 100, 200, 150, 300),
                 (100, 0, 250, 180, 400),
                 (200, 250, 0, 120, 350),
                 (150, 180, 120, 0, 280),
                 (300, 400, 350, 280, 0))

    def __init__(self):
        self.vehicles = list()
        self.fuel_price = {'GASOLINE': 0, 'DIESEL': 0, 'JET_FUEL': 0}

    @staticmethod
    def index(city):
        return ord(city) - ord('A')

    def add_vehicle(self, type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        vehicle = Vehicle(type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km)
        self.vehicles.append(vehicle)

    def add_trip(self, vehicle_id, origin, destination, cargo_weight):
        vehicle_id -= 1
        if vehicle_id >= len(self.vehicles) or vehicle_id < 0:
            print('Vehicle ID is incorrect!')
            return

        print(f'Trip registered: {self.vehicles[vehicle_id].type} from {origin} to {destination} carrying {cargo_weight} kg.')

        origin = Logistic.index(origin)
        destination = Logistic.index(destination)

        self.vehicles[vehicle_id].add_trip(Logistic.Distances[origin][destination], cargo_weight, self.fuel_price[Vehicle.FuelType[self.vehicles[vehicle_id].type]])

    def set_fuel_price(self, fuel, price):
        self.fuel_price[fuel] = price
        print(f'Fuel price for {fuel} set to {price} per liter.')

    def end_month(self):
        total_fixed_maintenance, total_variable_maintenance, total_fuel_cost = 0, 0, 0
        for vehicle in self.vehicles:
            total_fixed_maintenance += vehicle.fixed_cost
            total_variable_maintenance += vehicle.variable_maintenance
            total_fuel_cost += vehicle.fuel_cost
        print(f'End of month report:\nTotal fixed maintenance cost: {total_fixed_maintenance}\nTotal variable maintenance: {total_variable_maintenance}\nTotal fuel cost: {total_fuel_cost}')
        print(f'Total operational cost: {total_fixed_maintenance + total_variable_maintenance + total_fuel_cost}')

        print('Detailed costs:')
        for vehicle in self.vehicles:
            vehicle.out()

if __name__ == '__main__':
    logistic = Logistic()
    while 1:
        command = file1.readline().strip()
        command = [line.strip() for line in list(command.split(' ')) if line.strip()]

        if len(command) == 0:
            break

        if command[0] == 'ADD_VEHICLE':
            logistic.add_vehicle(command[1], int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == 'ADD_TRIP':
            logistic.add_trip(int(command[1]), command[2], command[3], int(command[4]))
        elif command[0] == 'END_MONTH':
            logistic.end_month()
        else:
            logistic.set_fuel_price(command[1], int(command[2]))

# ---------- End of Main Code ----------

sys.stdout = original_stdout

file1.close()
file2.close()
