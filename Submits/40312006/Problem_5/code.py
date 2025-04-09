CITY_IDS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
DIST = (
    (0, 100, 200, 150, 300),
    (100, 0, 250, 180, 400),
    (200, 250, 0, 120, 350),
    (150, 180, 120, 0, 280),
    (300, 400, 350, 280, 0)
)

MAX_WEIGHT = {"PLANE": 10000.0, "TRUCK": 5000.0, "PICKUP": 1500.0, "CAR": 500.0}
FUEL_TYPE = {"PLANE": "JET_FUEL", "TRUCK": "DIESEL", "PICKUP": "GASOLINE", "CAR": "GASOLINE"}

class Vehicle:
    def __init__(self, vid: int, vtype: str, fixed_cost: int, variable_cost: int, fuel_rate: float) -> None:
        self.vid = vid
        self.vtype = vtype
        self.fixed_cost = fixed_cost
        self.variable_cost = 0
        self.fuel_cost = 0
        self.fuel_rate = fuel_rate
        self.variable_rate = variable_cost
        self.max_weight = MAX_WEIGHT[vtype]

        print(f"Vehicle {vtype} added with fixed cost: {fixed_cost}, variable cost: {variable_cost}")

    def add_trip(self, origin: str, dest: str, weight: float, fuel_cost: int) -> None:
        if weight > self.max_weight:
            print("Cargo weight exceeds the limit")
            return

        dist = DIST[CITY_IDS[origin]][CITY_IDS[dest]]
        self.variable_cost += self.variable_rate * dist
        self.fuel_cost += int(self.fuel_rate * dist * fuel_cost)

        print(f"Trip registered: {self.vtype} from {origin} to {dest} carrying {weight} kg")

    def get_type(self) -> str:
        return self.vtype

    def get_fixed_cost(self) -> int:
        return self.fixed_cost

    def get_variable_cost(self) -> int:
        return self.variable_cost

    def get_fuel_cost(self) -> int:
        return self.fuel_cost

    def print_costs(self) -> None:
        print(f" {self.vtype} (ID: {self.vid}):")
        print(f"\tFixed maintenance: {self.fixed_cost}")
        print(f"\tVariable maintenance: {self.variable_cost}")
        print(f"\tFuel cost: {self.fuel_cost}")

class Manager:
    def __init__(self):
        self.vehicles = []
        self.fuel_costs = {"JET_FUEL": 0, "DIESEL": 0, "GASOLINE": 0}

    def add_vehicle(self, vtype: str, fixed_cost: int, variable_cost: int, fuel_rate: float) -> None:
        if vtype not in MAX_WEIGHT:
            print("Invalid vehicle type")
            return

        vehicle = Vehicle(len(self.vehicles) + 1, vtype, fixed_cost, variable_cost, fuel_rate)
        self.vehicles.append(vehicle)

    def set_fuel_price(self, ftype: str, cost: int) -> None:
        if ftype not in self.fuel_costs:
            print("Invalid fuel type")
            return

        self.fuel_costs[ftype] = cost
        print(f"Fuel price for {ftype} set to {cost} per liter")

    def add_trip(self, vid: int, origin: str, dest: str, weight: float) -> None:
        if vid > len(self.vehicles):
            print("ID not found")
            return

        if origin not in CITY_IDS:
            print("Origin not found")
            return
        if dest not in CITY_IDS:
            print("Destination not found")
            return

        vehicle = self.vehicles[vid - 1]
        vehicle.add_trip(origin, dest, weight, self.fuel_costs[FUEL_TYPE[vehicle.get_type()]])

    def end_month(self) -> None:
        fixed_cost = sum(map(lambda x: x.get_fixed_cost(), self.vehicles))
        variable_cost = sum(map(lambda x: x.get_variable_cost(), self.vehicles))
        fuel_cost = sum(map(lambda x: x.get_fuel_cost(), self.vehicles))

        print("End of month report:")
        print(f"Total fixed maintenance cost: {fixed_cost}")
        print(f"Total variable maintenance cost: {variable_cost}")
        print(f"Total fuel cost: {fuel_cost}")
        print(f"Total operational cost: {fixed_cost + variable_cost + fuel_cost}")
        print("Detailed costs:")
        for i in self.vehicles:
            i.print_costs()

manager = Manager()

while True:
    inp = input()
    if not inp:
        break

    if inp == "END_MONTH":
        manager.end_month()
        continue

    code, data = inp.split(maxsplit=1)
    match code:
        case "ADD_VEHICLE":
            vtype, fixed_cost, variable_cost, fuel_rate = data.split()
            manager.add_vehicle(vtype, int(fixed_cost), int(variable_cost), int(fuel_rate))
        case "ADD_TRIP":
            vid, origin, dest, weight = data.split()
            manager.add_trip(int(vid), origin, dest, float(weight))
        case "SET_FUEL_PRICE":
            ftype, price = data.split()
            manager.set_fuel_price(ftype, int(price))
        case _:
            print("Invalid execution code")
