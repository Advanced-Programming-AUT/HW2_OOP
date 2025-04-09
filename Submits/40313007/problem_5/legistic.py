class Vehicle:
    def __init__(self, vehicle_id, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        self.vehicle_id = vehicle_id
        self.fixed_cost = fixed_cost
        self.variable_cost_per_km = variable_cost_per_km
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.trips = []

    def add_trip(self, distance, cargo_weight):
        self.trips.append((distance, cargo_weight))

    def calculate_fixed_cost(self):
        return self.fixed_cost

    def calculate_variable_cost(self):
        return sum(distance * self.variable_cost_per_km for distance, _ in self.trips)

    def calculate_fuel_cost(self, fuel_price):
        return sum(distance * self.fuel_consumption_per_km * fuel_price for distance, _ in self.trips)

    def reset_trips(self):
        self.trips.clear()


class Truck(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, 1000000, 500, 3)


class Plane(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, 5000000, 2000, 10)


class Pickup(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, 1500, 2, 0.3)


class Car(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, 500, 1.5, 0.2)


class LogisticsManagement:

    city_distances = {
        'A': {'B': 100, 'C': 200, 'D': 150, 'E': 300},
        'B': {'A': 100, 'C': 250, 'D': 180, 'E': 400},
        'C': {'A': 200, 'B': 250, 'D': 120, 'E': 350},
        'D': {'A': 150, 'B': 180, 'C': 120, 'E': 280},
        'E': {'A': 300, 'B': 400, 'C': 350, 'D': 280},
    }

    def __init__(self):
        self.vehicles = {}
        self.fuel_prices = {}
        self.trips = []
        self.vehicle_count = 0

    def add_vehicle(self, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        self.vehicle_count += 1
        vehicle = None

        if vehicle_type == "TRUCK":
            vehicle = Truck(self.vehicle_count)
        elif vehicle_type == "PLANE":
            vehicle = Plane(self.vehicle_count)
        elif vehicle_type == "PICKUP":
            vehicle = Pickup(self.vehicle_count)
        elif vehicle_type == "CAR":
            vehicle = Car(self.vehicle_count)
        else:
            print("Unknown vehicle type.")
            return

        self.vehicles[self.vehicle_count] = vehicle
        print(f"Vehicle {vehicle_type} added with fixed cost: {fixed_cost}, variable cost per km: {variable_cost_per_km}")

    def add_trip(self, vehicle_id, origin, destination, cargo_weight):
        if vehicle_id not in self.vehicles:
            print(f"Invalid vehicle ID: {vehicle_id}")
            return

        if origin not in self.city_distances or destination not in self.city_distances[origin]:
            print("Invalid origin or destination.")
            return

        distance = self.city_distances[origin][destination]
        vehicle = self.vehicles[vehicle_id]
        vehicle.add_trip(distance, cargo_weight)
        self.trips.append((vehicle, origin, destination, cargo_weight))
        print(f"Trip registered: {vehicle_id} from {origin} to {destination} carrying {cargo_weight} kg.")

    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type] = price
        print(f"Fuel price for {fuel_type} set to {price} per liter.")

    def end_month_report(self):
        total_fixed_cost = sum(vehicle.calculate_fixed_cost() for vehicle in self.vehicles.values())
        total_variable_cost = sum(vehicle.calculate_variable_cost() for vehicle in self.vehicles.values())

        total_fuel_cost = sum(
            vehicle.calculate_fuel_cost(self.fuel_prices.get('DIESEL', 0)) +
            vehicle.calculate_fuel_cost(self.fuel_prices.get('JET_FUEL', 0))
            for vehicle in self.vehicles.values()
        )

        total_operational_cost = total_fixed_cost + total_variable_cost + total_fuel_cost

        print("End of month report:")
        print(f"Total fixed maintenance cost: {total_fixed_cost}")
        print(f"Total variable maintenance cost: {total_variable_cost}")
        print(f"Total fuel cost: {total_fuel_cost}")
        print(f"Total operational cost: {total_operational_cost}")

        print("Detailed costs:")
        for vehicle in self.vehicles.values():
            fuel_cost = vehicle.calculate_fuel_cost(self.fuel_prices.get('DIESEL', 0)) + \
                        vehicle.calculate_fuel_cost(self.fuel_prices.get('JET_FUEL', 0))
            print(f"{vehicle.__class__.__name__} (ID: {vehicle.vehicle_id}):")
            print(f"  Fixed maintenance: {vehicle.calculate_fixed_cost()}")
            print(f"  Variable maintenance: {vehicle.calculate_variable_cost()}")
            print(f"  Fuel cost: {fuel_cost}")

        for vehicle in self.vehicles.values():
            vehicle.reset_trips()
        self.trips.clear()


logistics_manager = LogisticsManagement()

logistics_manager.add_vehicle("TRUCK", 1000000, 500, 3)
logistics_manager.add_vehicle("PLANE", 5000000, 2000, 10)

logistics_manager.set_fuel_price("DIESEL", 15000)
logistics_manager.set_fuel_price("JET_FUEL", 50000)

logistics_manager.add_trip(1, "A", "B", 2000)  # Trip with Truck
logistics_manager.add_trip(2, "A", "C", 5000)  # Trip with Plane

logistics_manager.end_month_report()