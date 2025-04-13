class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        self.id = vehicle_id
        self.type = vehicle_type
        self.fixed_cost = fixed_cost
        self.variable_cost_per_km = variable_cost_per_km
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.total_distance = 0
        self.fuel_cost = 0
        self.trips = []

    def add_trip(self, distance, cargo_weight, fuel_price):
        self.total_distance += distance
        fuel_consumed = distance * self.fuel_consumption_per_km
        self.fuel_cost += fuel_consumed * fuel_price
        self.trips.append({
            'distance': distance,
            'cargo_weight': cargo_weight,
            'fuel_consumed': fuel_consumed,
            'fuel_cost': fuel_consumed * fuel_price
        })

    def get_fixed_maintenance_cost(self):
        return self.fixed_cost

    def get_variable_maintenance_cost(self):
        return self.total_distance * self.variable_cost_per_km

    def get_total_maintenance_cost(self):
        return self.get_fixed_maintenance_cost() + self.get_variable_maintenance_cost()

    def get_total_cost(self):
        return self.get_total_maintenance_cost() + self.fuel_cost


class LogisticsSystem:
    def __init__(self):
        self.vehicles = {}
        self.vehicle_counter = 1
        self.fuel_prices = {
            'GASOLINE': 0,
            'DIESEL': 0,
            'JET_FUEL': 0
        }
        self.distance_matrix = {
            'A': {'A': 0, 'B': 100, 'C': 200, 'D': 150, 'E': 300},
            'B': {'A': 100, 'B': 0, 'C': 250, 'D': 180, 'E': 400},
            'C': {'A': 200, 'B': 250, 'C': 0, 'D': 120, 'E': 350},
            'D': {'A': 150, 'B': 180, 'C': 120, 'D': 0, 'E': 280},
            'E': {'A': 300, 'B': 400, 'C': 350, 'D': 280, 'E': 0}
        }
        self.current_month_trips = []

    def add_vehicle(self, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        vehicle_id = self.vehicle_counter
        self.vehicle_counter += 1

        type_mapping = {
            'CAR': 'CAR',
            'PICKUP': 'PICKUP',
            'TRUCK': 'TRUCK',
            'PLANE': 'PLANE'
        }

        vehicle_type_std = type_mapping.get(vehicle_type.upper(), vehicle_type.upper())

        vehicle = Vehicle(vehicle_id, vehicle_type_std, fixed_cost, variable_cost_per_km, fuel_consumption_per_km)
        self.vehicles[vehicle_id] = vehicle

        print(f"Vehicle {vehicle_type_std} added with ID: {vehicle_id}, fixed cost: {fixed_cost}, variable cost per km: {variable_cost_per_km}")
        return vehicle_id

    def set_fuel_price(self, fuel_type, price):
        fuel_type_upper = fuel_type.upper()
        if fuel_type_upper in self.fuel_prices:
            self.fuel_prices[fuel_type_upper] = price
            print(f"Fuel price for {fuel_type_upper} set to {price} per liter.")
        else:
            print(f"Error: Unknown fuel type {fuel_type}")

    def add_trip(self, vehicle_id, origin, destination, cargo_weight):
        if vehicle_id not in self.vehicles:
            print(f"Error: Vehicle with ID {vehicle_id} not found")
            return

        origin = origin.upper()
        destination = destination.upper()

        if origin not in self.distance_matrix or destination not in self.distance_matrix[origin]:
            print(f"Error: Invalid route from {origin} to {destination}")
            return

        distance = self.distance_matrix[origin][destination]
        vehicle = self.vehicles[vehicle_id]

        max_capacity = {
            'PLANE': 10000,
            'TRUCK': 5000,
            'PICKUP': 1500,
            'CAR': 500
        }.get(vehicle.type, 0)

        if cargo_weight > max_capacity:
            print(f"Error: Cargo weight {cargo_weight}kg exceeds maximum capacity {max_capacity}kg for {vehicle.type}")
            return

        fuel_type = {
            'PLANE': 'JET_FUEL',
            'TRUCK': 'DIESEL',
            'PICKUP': 'GASOLINE',
            'CAR': 'GASOLINE'
        }.get(vehicle.type, 'GASOLINE')

        fuel_price = self.fuel_prices[fuel_type]

        vehicle.add_trip(distance, cargo_weight, fuel_price)
        self.current_month_trips.append((vehicle_id, origin, destination, cargo_weight))

        print(
            f"Trip registered: {vehicle.type} (ID: {vehicle_id}) from {origin} to {destination} carrying {cargo_weight}kg.")

    def end_month(self):
        total_fixed = 0
        total_variable = 0
        total_fuel = 0

        print("\nEnd of month report:")

        for vehicle_id, vehicle in self.vehicles.items():
            fixed = vehicle.get_fixed_maintenance_cost()
            variable = vehicle.get_variable_maintenance_cost()
            fuel = vehicle.fuel_cost

            total_fixed += fixed
            total_variable += variable
            total_fuel += fuel

            print(f"{vehicle.type} (ID: {vehicle_id}):")
            print(f"    Fixed maintenance: {fixed}")
            print(f"    Variable maintenance: {variable}")
            print(f"    Fuel cost: {fuel}")

        total_operational = total_fixed + total_variable + total_fuel

        print("\nSummary:")
        print(f"Total fixed maintenance cost: {total_fixed}")
        print(f"Total variable maintenance cost: {total_variable}")
        print(f"Total fuel cost: {total_fuel}")
        print(f"Total operational cost: {total_operational}")

        self.current_month_trips = []
        for vehicle in self.vehicles.values():
            vehicle.total_distance = 0
            vehicle.fuel_cost = 0
            vehicle.trips = []

if __name__ == "__main__":
    system = LogisticsSystem()

    system.add_vehicle("TRUCK", 1000000, 500, 3)
    system.add_vehicle("PLANE", 5000000, 2000, 10)
    system.set_fuel_price("DIESEL", 15000)
    system.set_fuel_price("JET_FUEL", 50000)
    system.add_trip(1, "A", "B", 2000)
    system.add_trip(2, "A", "C", 5000)
    system.end_month()
