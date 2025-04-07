class Vehicle:
    def __init__(self, vehicle_id, type, fixed_cost, variable_cost, fuel_consumption):
        self.id = vehicle_id
        self.type = type
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost
        self.fuel_consumption = fuel_consumption
        self.trips = []

    def add_trip(self, origin, destination, distance, cargo_weight):
        self.trips.append((origin, destination, distance, cargo_weight))

    def calculate_monthly_costs(self, fuel_price):
        total_variable_cost = sum(
            self.variable_cost * trip[2] for trip in self.trips)
        total_fuel_cost = sum(self.fuel_consumption *
                              trip[2] * fuel_price for trip in self.trips)
        return self.fixed_cost, total_variable_cost, total_fuel_cost


class LogisticsSystem:
    def __init__(self):
        self.vehicles = {}
        self.fuel_prices = {}
        self.distances = {
            'A': {'B': 100, 'C': 200, 'D': 150, 'E': 300},
            'B': {'A': 100, 'C': 250, 'D': 180, 'E': 400},
            'C': {'A': 200, 'B': 250, 'D': 120, 'E': 350},
            'D': {'A': 150, 'B': 180, 'C': 120, 'E': 280},
            'E': {'A': 300, 'B': 400, 'C': 350, 'D': 280},
        }
        self.vehicle_count = 0

    def add_vehicle(self, type, fixed_cost, variable_cost, fuel_consumption):
        self.vehicle_count += 1
        vehicle = Vehicle(self.vehicle_count, type, fixed_cost,
                          variable_cost, fuel_consumption)
        self.vehicles[self.vehicle_count] = vehicle
        print(
            f"Vehicle {type} added with fixed cost: {fixed_cost} , variable cost per km: {variable_cost}")

    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type] = price
        print(f"Fuel price for {fuel_type} set to {price} per liter.")

    def add_trip(self, vehicle_id, origin, destination, cargo_weight):
        if vehicle_id not in self.vehicles:
            print("Invalid vehicle ID.")
            return
        if origin not in self.distances or destination not in self.distances[origin]:
            print("Invalid route.")
            return
        distance = self.distances[origin][destination]
        self.vehicles[vehicle_id].add_trip(
            origin, destination, distance, cargo_weight)
        print(
            f"Trip registered: {self.vehicles[vehicle_id].type} from {origin} to {destination} carrying {cargo_weight} kg.")

    def end_month(self):
        total_fixed_cost = 0
        total_variable_cost = 0
        total_fuel_cost = 0
        print("End of month report:")

        for vehicle in self.vehicles.values():
            fuel_type = {
                'PLANE': 'JET_FUEL',
                'TRUCK': 'DIESEL',
                'PICKUP': 'GASOLINE',
                'CAR': 'GASOLINE'
            }[vehicle.type]
            fuel_price = self.fuel_prices.get(fuel_type, 0)

            fixed_cost, variable_cost, fuel_cost = vehicle.calculate_monthly_costs(
                fuel_price)
            total_fixed_cost += fixed_cost
            total_variable_cost += variable_cost
            total_fuel_cost += fuel_cost

        total_operational_cost = total_fixed_cost + \
            total_variable_cost + total_fuel_cost
        print(f"Total fixed maintenance cost: {total_fixed_cost}")
        print(f"Total variable maintenance cost: {total_variable_cost}")
        print(f"Total fuel cost: {total_fuel_cost}")
        print(f"Total operational cost: {total_operational_cost}")

        print("Detailed costs:")
        for vehicle in self.vehicles.values():
            fuel_type = {
                'PLANE': 'JET_FUEL',
                'TRUCK': 'DIESEL',
                'PICKUP': 'GASOLINE',
                'CAR': 'GASOLINE'
            }[vehicle.type]
            fuel_price = self.fuel_prices.get(fuel_type, 0)

            fixed_cost, variable_cost, fuel_cost = vehicle.calculate_monthly_costs(
                fuel_price)
            print(f" {vehicle.type} (ID: {vehicle.id}):")
            print(f"   Fixed maintenance: {fixed_cost}")
            print(f"   Variable maintenance: {variable_cost}")
            print(f"   Fuel cost: {fuel_cost}")


logistics = LogisticsSystem()

while True:
    try:
        command = input().strip()
        if not command:
            continue

        parts = command.split()
        action = parts[0]

        if action == "ADD_VEHICLE":
            _, type, fixed_cost, variable_cost, fuel_consumption = parts
            logistics.add_vehicle(type, int(fixed_cost), int(
                variable_cost), int(fuel_consumption))

        elif action == "SET_FUEL_PRICE":
            _, fuel_type, price = parts
            logistics.set_fuel_price(fuel_type, int(price))

        elif action == "ADD_TRIP":
            _, vehicle_id, origin, destination, cargo_weight = parts
            logistics.add_trip(int(vehicle_id), origin,
                               destination, int(cargo_weight))

        elif action == "END_MONTH":
            logistics.end_month()

        else:
            print("Invalid command.")
    except KeyboardInterrupt:
        break
