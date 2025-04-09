# Constants for vehicle capacity
capacity_limits = {
    'PLANE': 10000,
    'TRUCK': 5000,
    'PICKUP': 1500,
    'CAR': 500
}

# Distance lookup table
distances = [
    [0, 100, 200, 150, 300],
    [100, 0, 250, 180, 400],
    [200, 250, 0, 120, 350],
    [150, 180, 120, 0, 280],
    [300, 400, 350, 280, 0]
]

# City mapping
location_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

# Fuel prices and type per vehicle
fuel_prices = {'JET_FUEL': 0, 'DIESEL': 0, 'GAS': 0}
fuel_usage_map = {
    'PLANE': 'JET_FUEL',
    'TRUCK': 'DIESEL',
    'PICKUP': 'GAS',
    'CAR': 'GAS'
}

class TransportUnit:
    def __init__(self, uid, category, base_cost, per_km_cost, fuel_usage):
        self.uid = uid
        self.category = category
        self.base_cost = base_cost
        self.per_km_cost = per_km_cost
        self.fuel_efficiency = fuel_usage
        self.trip_cost = 0
        self.fuel_spent = 0
        self.capacity = capacity_limits[category]

    def register_trip(self, from_city, to_city):
        start = location_index[from_city]
        end = location_index[to_city]
        km = distances[start][end]
        self.trip_cost += self.per_km_cost * km
        fuel_type = fuel_usage_map[self.category]
        self.fuel_spent += km * self.fuel_efficiency * fuel_prices[fuel_type]

def run_fleet_management():
    fleet = {}
    unit_counter = 0

    while True:
        command = input(">> ").split()
        if not command:
            continue
        action = command[0]

        if action == 'END_MONTH':
            break

        if action == 'ADD_VEHICLE':
            v_type, fixed, variable, fuel_cons = command[1], int(command[2]), int(command[3]), int(command[4])
            fleet[unit_counter] = TransportUnit(unit_counter, v_type, fixed, variable, fuel_cons)
            print(f"[+] {v_type} registered. Fixed: {fixed}, per-km: {variable}")
            unit_counter += 1

        elif action == 'SET_FUEL_PRICE':
            fuel_type, price = command[1], int(command[2])
            fuel_prices[fuel_type] = price
            print(f"[✓] Fuel rate for {fuel_type} is now {price} per liter")

        elif action == 'ADD_TRIP':
            vehicle_id = int(command[1]) - 1
            start, end, cargo = command[2], command[3], int(command[4])
            if vehicle_id not in fleet:
                print("[!] Vehicle not found.")
                continue
            vehicle = fleet[vehicle_id]
            if cargo <= vehicle.capacity:
                vehicle.register_trip(start, end)
                print(f"[✓] Trip: {vehicle.category} from {start} to {end} with {cargo}kg cargo")
            else:
                print("[!] Cargo exceeds vehicle capacity.")

    print("\n=== Monthly Report ===")
    total_fixed = sum(v.base_cost for v in fleet.values())
    total_variable = sum(v.trip_cost for v in fleet.values())
    total_fuel = sum(v.fuel_spent for v in fleet.values())
    total_all = total_fixed + total_variable + total_fuel

    print(f"Fixed Maintenance: {total_fixed}")
    print(f"Variable Maintenance: {total_variable}")
    print(f"Fuel Expense: {total_fuel}")
    print(f"TOTAL: {total_all}")

    print("\n--- Detailed Breakdown ---")
    for vid, unit in fleet.items():
        print(f"[ID {vid + 1}] {unit.category}")
        print(f"  Fixed: {unit.base_cost}")
        print(f"  Maintenance: {unit.trip_cost}")
        print(f"  Fuel: {unit.fuel_spent}")

run_fleet_management()

