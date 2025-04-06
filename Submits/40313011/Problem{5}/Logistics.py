jet_fuel_price = 0
diesel_price = 0
gas_price = 0


def cities_distance(city1, city2):
    cities_distance_list = [
        [0, 100, 200, 150, 300],
        [100, 0, 250, 180, 400],
        [200, 250, 0, 120, 350],
        [150, 180, 120, 0, 280],
        [300, 400, 350, 280, 0]
    ]
    city1_number = ord(city1) - 65
    city2_number = ord(city2) - 65

    return cities_distance_list[city1_number][city2_number]


class Vehicle:
    def __init__(self, type):
        self.type = type

    def trip_cost(self, origin, destination):
        pass


class Plane(Vehicle):
    def __init__(self):
        super().__init__(Plane)
        self.fixed_cost = 5000000
        self.variable_cost_per_km = 2000
        self.fuel_consumption = 10
        self.capacity = 10000
        self.variable_cost = 0
        self.fuel_cost = 0

    def trip_cost(self, origin, destination):
        distance = cities_distance(origin, destination)
        self.variable_cost += distance * self.variable_cost_per_km
        self.fuel_cost += distance * self.fuel_consumption * jet_fuel_price

    def __str__(self):
        return "PLANE"


class Truck(Vehicle):
    def __init__(self):
        super().__init__(Truck)
        self.fixed_cost = 1000000
        self.variable_cost_per_km = 500
        self.fuel_consumption = 3
        self.capacity = 5000
        self.variable_cost = 0
        self.fuel_cost = 0

    def trip_cost(self, origin, destination):
        distance = cities_distance(origin, destination)
        self.variable_cost += distance * self.variable_cost_per_km
        self.fuel_cost += distance * self.fuel_consumption * diesel_price

    def __str__(self):
        return "TRUCK"


class Pickup(Vehicle):
    def __init__(self):
        super().__init__(Pickup)
        self.fixed_cost = 800000
        self.variable_cost_per_km = 300
        self.fuel_consumption = 2
        self.capacity = 15000
        self.variable_cost = 0
        self.fuel_cost = 0

    def trip_cost(self, origin, destination):
        distance = cities_distance(origin, destination)
        self.variable_cost += distance * self.variable_cost_per_km
        self.fuel_cost += distance * self.fuel_consumption * gas_price

    def __str__(self):
        return "PICKUP"


class Car(Vehicle):
    def __init__(self):
        super().__init__(Car)
        self.fixed_cost = 500000
        self.variable_cost_per_km = 200
        self.fuel_consumption = 1.5
        self.capacity = 500
        self.variable_cost = 0
        self.fuel_cost = 0

    def trip_cost(self, origin, destination):
        distance = cities_distance(origin, destination)
        self.variable_cost += distance * self.variable_cost_per_km
        self.fuel_cost += distance * self.fuel_consumption * gas_price

    def __str__(self):
        return "CAR"


def report(vehicle_list):
    fixed_cost = 0
    variable_cost = 0
    fuel_cost = 0
    print("End of month report: ")
    for vehicle in vehicle_list:
        fixed_cost += vehicle.fixed_cost
        variable_cost += vehicle.variable_cost
        fuel_cost += vehicle.fuel_cost
    print("  Total fixed maintenance cost: ", fixed_cost)
    print("  Total variable maintenance cost: ", variable_cost)
    print("  Total fuel maintenance cost: ", fuel_cost)
    print(f"  Total operational cost: {fixed_cost + variable_cost + fuel_cost}")

    print("Detailed costs: ")
    for vehicle_id in range(len(vehicle_list)):
        vehicle = vehicle_list[vehicle_id]
        print(f"  {vehicle} (ID: {vehicle_id + 1})")
        print(f"    Fixed maintenance: {vehicle.fixed_cost}")
        print(f"    Variable maintenance: {vehicle.variable_cost}")
        print(f"    Fuel maintenance: {vehicle.fuel_cost}")


vehicles_list = []
while True:
    cmd = input()
    cmd = cmd.split()
    if cmd[0] == "ADD_VEHICLE":
        if cmd[1] == "TRUCK":
            vehicle = Truck()
            vehicles_list.append(vehicle)
            print(f"Vehicle {vehicle} added with fixed cost: {vehicle.fixed_cost}, variable cost per km: {vehicle.variable_cost_per_km}, fuel cost per km: {vehicle.fuel_consumption}")
        if cmd[1] == "PICKUP":
            vehicle = Pickup()
            vehicles_list.append(vehicle)
            print(f"Vehicle {vehicle} added with fixed cost: {vehicle.fixed_cost}, variable cost per km: {vehicle.variable_cost_per_km}, fuel cost per km: {vehicle.fuel_consumption}")
        if cmd[1] == "CAR":
            vehicle = Car()
            vehicles_list.append(vehicle)
            print(f"Vehicle {vehicle} added with fixed cost: {vehicle.fixed_cost}, variable cost per km: {vehicle.variable_cost_per_km}, fuel cost per km: {vehicle.fuel_consumption}")
        if cmd[1] == "PLANE":
            vehicle = Plane()
            vehicles_list.append(vehicle)
            print(f"Vehicle {vehicle} added with fixed cost: {vehicle.fixed_cost}, variable cost per km: {vehicle.variable_cost_per_km}, fuel cost per km: {vehicle.fuel_consumption}")
    if cmd[0] == "ADD_TRIP":
        vehicle = vehicles_list[int(cmd[1]) - 1]
        vehicle.trip_cost(cmd[2], cmd[3])
        print(f"Trip registered: {vehicle} from {cmd[2]} to {cmd[3]} carrying {cmd[4]} kg")
    if cmd[0] == "SET_FUEL_PRICE":
        if cmd[1] == "JET_FUEL":
            jet_fuel_price = int(cmd[2])
            print(f"Fuel price for JET_FUEL set to {jet_fuel_price} per liter.")
        if cmd[1] == "GASOLINE":
            gas_price = int(cmd[2])
            print(f"Fuel price for GASOLINE set to {gas_price} per liter.")
        if cmd[1] == "DIESEL":
            diesel_price = int(cmd[2])
            print(f"Fuel price for DIESEL set to {diesel_price} per liter.")
    if cmd[0] == "END_MONTH":
        report(vehicles_list)
        break
