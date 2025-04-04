import math

# Vehicle class to manage vehicles
class Vehicle:
    id_counter = 1

    def __init__(self, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption):
        self.id = Vehicle.id_counter
        Vehicle.id_counter += 1
        self.vehicle_type = vehicle_type
        self.fixed_cost = fixed_cost
        self.variable_cost_per_km = variable_cost_per_km
        self.fuel_consumption = fuel_consumption
        self.total_distance = 0  # Total distance traveled
        self.fuel_cost = 0  # Fuel cost for the vehicle

    def __str__(self):
        return f"{self.vehicle_type} (ID: {self.id})"

# Trip class to manage trips
class Trip:
    def __init__(self, vehicle_id, origin, destination, cargo_weight):
        self.vehicle_id = vehicle_id
        self.origin = origin
        self.destination = destination
        self.cargo_weight = cargo_weight

# Logistics class to manage the system
class Logistics:
    def __init__(self):
        self.vehicles = []
        self.trips = []
        self.fuel_prices = {"JET FUEL": 0, "DIESEL": 0, "GASOLINE": 0}
        self.distance_matrix = {
            "A": {"A": 0, "B": 100, "C": 200, "D": 150, "E": 300},
            "B": {"A": 100, "B": 0, "C": 250, "D": 180, "E": 400},
            "C": {"A": 200, "B": 250, "C": 0, "D": 120, "E": 350},
            "D": {"A": 150, "B": 180, "C": 120, "D": 0, "E": 280},
            "E": {"A": 300, "B": 400, "C": 350, "D": 280, "E": 0},
        }

    def add_vehicle(self, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption):
        vehicle = Vehicle(vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption)
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle_type} added with ID: {vehicle.id}")

    def set_fuel_price(self, fuel_type, price):
        if fuel_type in self.fuel_prices:
            self.fuel_prices[fuel_type] = price
            print(f"Fuel price for {fuel_type} set to {price} per liter.")
        else:
            print(f"Invalid fuel type: {fuel_type}")

    def add_trip(self, vehicle_id, origin, destination, cargo_weight):
        vehicle = next((v for v in self.vehicles if v.id == vehicle_id), None)
        if not vehicle:
            print(f"Vehicle with ID {vehicle_id} not found.")
            return

        if origin not in self.distance_matrix or destination not in self.distance_matrix:
            print("Invalid origin or destination.")
            return

        distance = self.distance_matrix[origin][destination]
        if cargo_weight > {
            "PLANE": 10000,
            "TRUCK": 5000,
            "PICKUP": 1500,
            "CAR": 500,
        }[vehicle.vehicle_type]:
            print(f"Cargo weight exceeds capacity for {vehicle.vehicle_type}.")
            return

        trip = Trip(vehicle_id, origin, destination, cargo_weight)
        self.trips.append(trip)
        vehicle.total_distance += distance
        fuel_price = self.fuel_prices[
            "JET FUEL" if vehicle.vehicle_type == "PLANE" else "DIESEL" if vehicle.vehicle_type == "TRUCK" else "GASOLINE"
        ]
        vehicle.fuel_cost += distance * vehicle.fuel_consumption * fuel_price
        print(f"Trip registered: {vehicle.vehicle_type} from {origin} to {destination} carrying {cargo_weight} kg.")

    def end_month(self):
        total_fixed_cost = sum(vehicle.fixed_cost for vehicle in self.vehicles)
        total_variable_cost = sum(vehicle.total_distance * vehicle.variable_cost_per_km for vehicle in self.vehicles)
        total_fuel_cost = sum(vehicle.fuel_cost for vehicle in self.vehicles)
        total_operational_cost = total_fixed_cost + total_variable_cost + total_fuel_cost

        print("\nEnd of month report:")
        print(f"Total fixed maintenance cost: {total_fixed_cost}")
        print(f"Total variable maintenance cost: {total_variable_cost}")
        print(f"Total fuel cost: {total_fuel_cost}")
        print(f"Total operational cost: {total_operational_cost}")
        print("Detailed costs:")

        for vehicle in self.vehicles:
            variable_cost = vehicle.total_distance * vehicle.variable_cost_per_km
            print(
                f"{vehicle.vehicle_type} (ID: {vehicle.id}): Fixed maintenance: {vehicle.fixed_cost}, "
                f"Variable maintenance: {variable_cost}, Fuel cost: {vehicle.fuel_cost}"
            )


def logistics_menu():
    logistics = Logistics()
    print("Welcome to the Logistics Management System!")

    while True:
        print("\nMenu:")
        print("1. Add Vehicle")
        print("2. Set Fuel Price")
        print("3. Add Trip")
        print("4. End Month Report")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("Add a new vehicle:")
            vehicle_type = input("Enter vehicle type (CAR/PICKUP/TRUCK/PLANE): ")
            fixed_cost = int(input("Enter fixed maintenance cost: "))
            variable_cost_per_km = int(input("Enter variable maintenance cost per km: "))
            fuel_consumption = float(input("Enter fuel consumption per km: "))
            logistics.add_vehicle(vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption)

        elif choice == "2":
            print("Set fuel price:")
            fuel_type = input("Enter fuel type (JET FUEL/DIESEL/GASOLINE): ")
            price = int(input("Enter price per liter: "))
            logistics.set_fuel_price(fuel_type, price)

        elif choice == "3":
            print("Add a new trip:")
            vehicle_id = int(input("Enter vehicle ID: "))
            origin = input("Enter origin city (A/B/C/D/E): ")
            destination = input("Enter destination city (A/B/C/D/E): ")
            cargo_weight = int(input("Enter cargo weight (kg): "))
            logistics.add_trip(vehicle_id, origin, destination, cargo_weight)

        elif choice == "4":
            logistics.end_month()

        elif choice == "5":
            print("Exiting the Logistics Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Example execution
if __name__ == "__main__":
    logistics_menu()

