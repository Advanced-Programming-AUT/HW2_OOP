class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.fixed_cost = fixed_cost
        self.variable_cost_per_km = variable_cost_per_km
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.trips = []

    def add_trip(self, origin, destination, cargo_weight, distance, fuel_price):
        fuel_cost = self.fuel_consumption_per_km * distance * fuel_price
        variable_cost = self.variable_cost_per_km * distance
        self.trips.append({"origin": origin, "destination": destination, "cargo_weight": cargo_weight, "distance": distance, "fuel_cost": fuel_cost, "variable_cost": variable_cost})
        return fuel_cost, variable_cost

    def calculate_total_cost(self):
        total_variable_cost = sum([trip["variable_cost"] for trip in self.trips])
        total_fuel_cost = sum([trip["fuel_cost"] for trip in self.trips])
        return self.fixed_cost, total_variable_cost, total_fuel_cost


class Fleet:
    def __init__(self):
        self.vehicles = []
        self.fuel_prices = {}

    def add_vehicle(self, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        vehicle_id = len(self.vehicles) + 1
        new_vehicle = Vehicle(vehicle_id, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km)
        self.vehicles.append(new_vehicle)
        print(f"Vehicle {vehicle_type} added with fixed cost: {fixed_cost}, variable cost per km: {variable_cost_per_km}")

    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type] = price
        print(f"Fuel price for {fuel_type} set to {price} per liter.")

    def get_fuel_price(self, fuel_type):
        return self.fuel_prices.get(fuel_type, 0)

    def add_trip(self, vehicle_id, origin, destination, cargo_weight, distance):
        vehicle = self.vehicles[vehicle_id - 1]
        if vehicle.vehicle_type == "PLANE":
            fuel_type = "JET"
        elif vehicle.vehicle_type == "TRUCK":
            fuel_type = "DIESEL"
        else:
            fuel_type = "PETROL"
        fuel_price = self.get_fuel_price(fuel_type)
        fuel_cost, variable_cost = vehicle.add_trip(origin, destination, cargo_weight, distance, fuel_price)
        print(f"Trip registered: {vehicle.vehicle_type} from {origin} to {destination} carrying {cargo_weight} kg.")
        return fuel_cost, variable_cost

    def end_month_report(self):
        total_fixed_cost = sum([vehicle.fixed_cost for vehicle in self.vehicles])
        total_variable_cost = sum([sum([trip["variable_cost"] for trip in vehicle.trips]) for vehicle in self.vehicles])
        total_fuel_cost = sum([sum([trip["fuel_cost"] for trip in vehicle.trips]) for vehicle in self.vehicles])
        total_operational_cost = total_fixed_cost + total_variable_cost + total_fuel_cost

        print("End of month report:")
        print(f"Total fixed maintenance cost: {total_fixed_cost}")
        print(f"Total variable maintenance cost: {total_variable_cost}")
        print(f"Total fuel cost: {total_fuel_cost}")
        print(f"Total operational cost: {total_operational_cost}")
        print("Detailed costs:")

        for vehicle in self.vehicles:
            fixed_cost, variable_cost, fuel_cost = vehicle.calculate_total_cost()
            print(f"{vehicle.vehicle_type} (ID: {vehicle.vehicle_id}):")
            print(f"  Fixed maintenance: {fixed_cost}")
            print(f"  Variable maintenance: {variable_cost}")
            print(f"  Fuel cost: {fuel_cost}")


def main():
    fleet = Fleet()

    fleet.add_vehicle("TRUCK", 1000000, 500, 3)
    fleet.add_vehicle("PLANE", 5000000, 2000, 10)
    fleet.set_fuel_price("DIESEL", 15000)
    fleet.set_fuel_price("JET", 50000)

    fleet.add_trip(1, "A", "B", 2000, 100)
    fleet.add_trip(2, "A", "C", 5000, 200)

    fleet.end_month_report()


if __name__ == "__main__":
    main()
