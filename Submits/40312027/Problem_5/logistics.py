class Vehicle:
    def __init__(self, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        self.vehicle_type = vehicle_type
        self.fixed_cost = fixed_cost
        self.variable_cost_per_km = variable_cost_per_km
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.vehicle_id = None

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def calculate_costs(self, distance, fuel_price):
        fuel_cost = self.fuel_consumption_per_km * distance * fuel_price
        variable_cost = self.variable_cost_per_km * distance
        total_cost = self.fixed_cost + variable_cost + fuel_cost
        return fuel_cost, variable_cost, total_cost

class Trip:
    def __init__(self, vehicle_id, origin, destination, cargo_weight):
        self.vehicle_id = vehicle_id
        self.origin = origin
        self.destination = destination
        self.cargo_weight = cargo_weight
        self.distance = self.calculate_distance(origin, destination)

    def calculate_distance(self, origin, destination):
        distances = {
            ('A', 'B'): 100, ('A', 'C'): 200, ('A', 'D'): 150, ('A', 'E'): 300,
            ('B', 'A'): 100, ('B', 'C'): 250, ('B', 'D'): 180, ('B', 'E'): 400,
            ('C', 'A'): 200, ('C', 'B'): 250, ('C', 'D'): 120, ('C', 'E'): 350,
            ('D', 'A'): 150, ('D', 'B'): 180, ('D', 'C'): 120, ('D', 'E'): 280,
            ('E', 'A'): 300, ('E', 'B'): 400, ('E', 'C'): 350, ('E', 'D'): 280
        }
        return distances.get((origin, destination), 0)

class LogisticsSystem:
    def __init__(self):
        self.vehicles = {}
        self.trips = []
        self.fuel_prices = {}

    def add_vehicle(self, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        vehicle_id = len(self.vehicles) + 1
        vehicle = Vehicle(vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km)
        vehicle.set_vehicle_id(vehicle_id)
        self.vehicles[vehicle_id] = vehicle
        print(f"Vehicle {vehicle_type} is added with fixed cost: {fixed_cost}, variable cost each km: {variable_cost_per_km}")

    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type] = price
        print(f"Fuel price for {fuel_type} set to {price} each liter.")

    def add_trip(self, vehicle_id, origin, destination, cargo_weight):
        trip = Trip(vehicle_id, origin, destination, cargo_weight)
        self.trips.append(trip)
        print(f"Trip is registered: {self.vehicles[vehicle_id].vehicle_type} from {origin} to {destination} carrying {cargo_weight} kg.")

    def end_month(self):
        total_fixed_cost = sum(vehicle.fixed_cost for vehicle in self.vehicles.values())
        total_variable_cost = 0
        total_fuel_cost = 0
        for trip in self.trips:
            vehicle = self.vehicles[trip.vehicle_id]
            fuel_type = 'DIESEL' if vehicle.vehicle_type == 'TRUCK' else 'JET_FUEL' if vehicle.vehicle_type == 'PLANE' else 'GASOLINE'
            fuel_price = self.fuel_prices.get(fuel_type, 0)
            fuel_cost, variable_cost, _ = vehicle.calculate_costs(trip.distance, fuel_price)
            total_variable_cost += variable_cost
            total_fuel_cost += fuel_cost

        total_operational_cost = total_fixed_cost + total_variable_cost + total_fuel_cost
        print(" report of end of the month:")
        print(f"Total fixed maintenance cost: {total_fixed_cost}")
        print(f"Total variable maintenance cost: {total_variable_cost}")
        print(f"Total fuel cost: {total_fuel_cost}")
        print(f"Total operational cost: {total_operational_cost}")
        print("Detailed costs:")
        for vehicle in self.vehicles.values():
            fuel_type = 'DIESEL' if vehicle.vehicle_type == 'TRUCK' else 'JET_FUEL' if vehicle.vehicle_type == 'PLANE' else 'GASOLINE'
            fuel_price = self.fuel_prices.get(fuel_type, 0)
            fuel_cost, variable_cost, _ = vehicle.calculate_costs(100, fuel_price)
            print(f"{vehicle.vehicle_type} (ID: {vehicle.vehicle_id}):")
            print(f"  Fixed maintenance: {vehicle.fixed_cost}")
            print(f"  Variable maintenance: {variable_cost}")
            print(f"  Fuel cost: {fuel_cost}")


logistics_system = LogisticsSystem()


def process_input(request):
    request = request.strip().split()
    if request[0] == 'ADD_VEHICLE':
        vehicle_type = request[1]
        fixed_cost = int(request[2])
        variable_cost_per_km = int(request[3])
        fuel_consumption_per_km = int(request[4])
        logistics_system.add_vehicle(vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km)

    elif request[0] == 'SET_FUEL_PRICE':
        fuel_type = request[1]
        price = int(request[2])
        logistics_system.set_fuel_price(fuel_type, price)

    elif request[0] == 'ADD_TRIP':
        vehicle_id = int(request[1])
        origin = request[2]
        destination = request[3]
        cargo_weight = int(request[4])
        logistics_system.add_trip(vehicle_id, origin, destination, cargo_weight)

    elif request[0] == 'END_MONTH':
        logistics_system.end_month()

# Main interactive loop
while True:
    print("\nEnter your request:")
    print("ADD_VEHICLE <vehicle_type> <fixed_cost> <variable_cost_per_km> <fuel_consumption_per_km>")
    print("SET_FUEL_PRICE <fuel_type> <price>")
    print("ADD_TRIP <vehicle_id> <origin> <destination> <cargo_weight>")
    print("END_MONTH")
    print("EXIT ")

    user_input = input("Enter your request: ")

    if user_input == 'EXIT':
        break
    else:
        process_input(user_input)