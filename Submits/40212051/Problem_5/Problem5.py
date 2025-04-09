from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, fixed_cost, variable_cost, fuel_per_km, fuel_type):
        self.vehicle_id = vehicle_id
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost
        self.fuel_per_km = fuel_per_km
        self.fuel_type = fuel_type
        self.distance_traveled = 0

    def add_trip(self, distance):
        self.distance_traveled += distance

    def get_fixed_cost(self):
        return self.fixed_cost

    def get_variable_cost(self):
        return self.variable_cost * self.distance_traveled

    def get_fuel_cost(self, fuel_price):
        return self.fuel_per_km * self.distance_traveled * fuel_price[self.fuel_type]

class Plane(Vehicle):
    def __init__(self, vehicle_id, fixed, variable, fuel):
        super().__init__(vehicle_id, fixed, variable, fuel, "JET_FUEL")

class Truck(Vehicle):
    def __init__(self, vehicle_id, fixed, variable, fuel):
        super().__init__(vehicle_id, fixed, variable, fuel, "DIESEL")

class Pickup(Vehicle):
    def __init__(self, vehicle_id, fixed, variable, fuel):
        super().__init__(vehicle_id, fixed, variable, fuel, "GASOLINE")

class Car(Vehicle):
    def __init__(self, vehicle_id, fixed, variable, fuel):
        super().__init__(vehicle_id, fixed, variable, fuel, "GASOLINE")

class Trip(object):
    def __init__(self, vehicle, origin, destination, distance):
        self.vehicle = vehicle
        self.origin = origin
        self.destination = destination
        self.distance = distance
        vehicle.add_trip(distance)

class LogisticsSystem(object):
    def __init__(self):
        self.vehicles = {}
        self.fuel_prices = {}
        self.next_id = 1
        self.city_distances = {
            'A': {'B': 100, 'C': 200, 'D': 150, 'E': 300},
            'B': {'A': 100, 'C': 250, 'D': 180, 'E': 400},
            'C': {'A': 200, 'B': 250, 'D': 120, 'E': 350},
            'D': {'A': 150, 'B': 180, 'C': 120, 'E': 280},
            'E': {'A': 300, 'B': 400, 'C': 350, 'D': 280}
        }

    def add_vehicle(self, vehicle_type, fixed, variable, fuel):
        vehicle_classes = {
            "PLANE": Plane,
            "TRUCK": Truck,
            "PICKUP": Pickup,
            "CAR": Car
        }
        vehicle = vehicle_classes[vehicle_type](self.next_id, fixed, variable, fuel)
        self.vehicles[self.next_id] = vehicle
        print(f"Vehicle {vehicle_type} added with ID: {self.next_id}")
        self.next_id += 1

    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type] = price
        print(f"Fuel price for {fuel_type} set to {price}")

    def add_trip(self, vehicle_id, origin, destination, cargo_weight):
        if vehicle_id not in self.vehicles:
            print("Invalid vehicle ID.")
            return
        distance = self.city_distances[origin][destination]
        vehicle = self.vehicles[vehicle_id]
        Trip(vehicle, origin, destination, distance)
        #__name__ khoobe?
        print(f"Trip registered: {type(vehicle).__name__} from {origin} to {destination} carrying {cargo_weight}kg")

    def end_month_report(self):
        total_fixed = total_variable = total_fuel = 0
        print("\nMonthly Report:")
        for v in self.vehicles.values():
            fixed = v.get_fixed_cost()
            variable = v.get_variable_cost()
            fuel = v.get_fuel_cost(self.fuel_prices)
            total_fixed += fixed
            total_variable += variable
            total_fuel += fuel
            print(f"Vehicle {v.vehicle_id} ({type(v).__name__}):")
            print(f"  Fixed: {fixed}")
            print(f"  Variable: {variable}")
            print(f"  Fuel: {fuel}")
        print("\nTotal Summary:")
        print(f"  Total Fixed: {total_fixed}")
        print(f"  Total Variable: {total_variable}")
        print(f"  Total Fuel: {total_fuel}")
        print(f"  Total Cost: {total_fixed + total_variable + total_fuel}")
