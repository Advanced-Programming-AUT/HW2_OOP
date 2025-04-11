class Vehicle:
    ids = 0
    vehicles = {}
    destinations = {'A-B': 100, 'A-C': 200, 'A-D': 150, 'A-E': 300, 'B-C': 250,
                    'B-D': 180, 'B-E': 400, 'C-D': 120, 'C-E': 350, 'D-E': 280}
    fuel_price = {}
    trips = []

    def __init__(self, vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        self.vehicle_type = vehicle_type
        self.fixed_cost = fixed_cost
        self.variable_cost_per_km = variable_cost_per_km
        self.fuel_consumption_per_km = fuel_consumption_per_km
        Vehicle.ids += 1
        self.fuel_type = self.fuel_type_setter()
        print(f"Vehicle {self.vehicle_type} added with fixed cost {self.fixed_cost} , "
              f"variable cost per km: {self.variable_cost_per_km}")

    def fuel_type_setter(self):
        if self.vehicle_type == 'PLANE':
            return 'JET_FUEL'
        elif self.vehicle_type == 'TRUCK':
            return 'DIESEL'
        elif self.vehicle_type in ['PICKUP', 'CAR']:
            return 'PETROL'
        else:
            print("Vehicle type not supported")

    @staticmethod
    def set_fuel_price(fuel_type, fuel_price):
        if fuel_type in ['JET_FUEL', 'DIESEL', 'PETROL']:
            Vehicle.fuel_price[fuel_type] = fuel_price
            print(f"Fuel price for {fuel_type} set to {fuel_price} per liter.")
        else:
            print('fuel is not valid')
            return

    def new_trip(self, vehicle_id, origin, destination, cargo_weight):
        vehicle = self.vehicles.get(vehicle_id, None)
        if not vehicle:
            print('vehicle does not exist')
            return
        else:
            distance_key = f"{origin}-{destination}" if origin < destination else f"{destination}-{origin}"
            distance = self.destinations[distance_key]
            variable_cost = distance * self.variable_cost_per_km
            fuel_cost = self.fuel_price[self.fuel_type] * self.fuel_consumption_per_km * distance
            self.trips.append((vehicle_id, self.fixed_cost, variable_cost, fuel_cost))
            print(f"Trip registered: {self.vehicles[vehicle_id].vehicle_type} from {origin} to {destination} "
                  f"carrying {cargo_weight} kg.")

    @staticmethod
    def end_month_of_report():
        print("Enf of month report:")
        total_fixed_cost = sum([trip[1] for trip in Vehicle.trips])
        print(f"Total fixed maintenance cost: {total_fixed_cost}")
        total_variable_cost = sum([trip[2] for trip in Vehicle.trips])
        print(f"Total variable maintenance cost: {total_variable_cost}")
        total_fuel_cost = sum([trip[3] for trip in Vehicle.trips])
        print(f"Total fuel cost: {total_fuel_cost}")
        total_operation_cost = total_fixed_cost + total_variable_cost + total_fuel_cost
        print(f"Total operation cost: {total_operation_cost}")
        for trip in Vehicle.trips:
            print(f" {Vehicle.vehicles[trip[0]].vehicle_type} (ID: {trip[0]}): ")
            print(f"   Fixed maintenance cost: {trip[1]}\n   Variable maintenance: {trip[2]}\n   Fuel cost: {trip[3]}")


def main():
    print("enter exit to exit")
    command = input().split()
    while True:
        match command[0]:
            case 'ADD_VEHICLE':
                vehicle_type = command[1]
                fixed_cost = int(command[2])
                variable_cost_per_km = int(command[3])
                fuel_consumption_per_km = int(command[4])
                vehicle = Vehicle(vehicle_type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km)
                Vehicle.vehicles[Vehicle.ids] = vehicle
            case 'SET_FUEL_PRICE':
                fuel_type = command[1]
                fuel_price = int(command[2])
                Vehicle.set_fuel_price(fuel_type, fuel_price)
            case 'ADD_TRIP':
                vehicle_id = int(command[1])
                origin = command[2]
                destination = command[3]
                cargo_weight = int(command[4])
                Vehicle.vehicles[vehicle_id].new_trip(vehicle_id, origin, destination, cargo_weight)
            case 'END_MONTH':
                Vehicle.end_month_of_report()
            case 'exit':
                return
        command = input().split()


if __name__ == '__main__':
    main()
