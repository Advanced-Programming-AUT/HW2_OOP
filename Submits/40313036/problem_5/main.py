maximum_wight = {
    'PLANE': 10000,
    'TRUCK': 5000,
    'PICKUP': 1500,
    'CAR': 500
}
matrix = [[0, 100, 200, 150, 300],
[100, 0, 250, 180, 400],
[200, 250, 0, 120, 350],
[150, 180, 120, 0, 280],
[300, 400, 350, 280, 0]]
alphs = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
fuel = {'JET_FUEL': 0,
        'DIESEL': 0,
        'GAS': 0}
fuel_type = {
    'PLANE': 'JET_FUEL',
    'TRUCK': 'DIESEL',
    'PICKUP': 'GAS',
    'CAR': 'GAS'
}

class Vehicle:
    def __init__(self, id, type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km):
        self.id = id
        self.type = type
        self.fixed_cost = fixed_cost
        self.variable_cost_per_km = variable_cost_per_km
        self.variable_maintenance = 0
        self.fuel_cost = 0
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.maximum_wight = maximum_wight[type]

    def add_trip(self, origin, destination):
        self.variable_maintenance += self.variable_cost_per_km*matrix[alphs[origin]][alphs[destination]]
        self.fuel_cost += self.fuel_consumption_per_km*fuel[fuel_type[self.type]]*matrix[alphs[origin]][alphs[destination]]

inp = input('>> ').split()
last_id = 0
vehicles = {}
while inp[0] != 'END_MONTH':
    if inp[0] == 'ADD_VEHICLE':
        vehicles[last_id] = Vehicle(last_id, inp[1], int(inp[2]), int(inp[3]), int(inp[4]))
        print(f'Vehicle {vehicles[last_id].type} added with fixed cost: {vehicles[last_id].fixed_cost} , variable cost per km: {vehicles[last_id].variable_cost_per_km}')
        last_id += 1
    elif inp[0] == 'SET_FUEL_PRICE':
        fuel[inp[1]] = int(inp[2])
        print(f'Fuel price for {inp[1]} set to {inp[2]} per liter.')
    elif inp[0] == 'ADD_TRIP':
        if maximum_wight[vehicles[int(inp[1])-1].type] >= int(inp[4]):
            vehicles[int(inp[1])-1].add_trip(inp[2], inp[3])
            print(f'Trip registered: {vehicles[int(inp[1])-1].type} from {inp[2]} to {inp[3]} carrying {inp[4]} kg.')
        else:
            print('The wight exces the maximum wight')
    inp = input('>> ').split()

print('End of month report:')
total_fixed_maintenace_cost = 0
total_variable_maintenance_cost = 0
total_fuel_cost = 0
for vehicle in vehicles:
    total_fixed_maintenace_cost += vehicles[vehicle].fixed_cost
    total_variable_maintenance_cost += vehicles[vehicle].variable_maintenance
    total_fuel_cost += vehicles[vehicle].fuel_cost
total_operational_cost = total_fixed_maintenace_cost+total_variable_maintenance_cost+total_fuel_cost
print(f'''Total fixed maintenace cost: {total_fixed_maintenace_cost}
Total variable maintenace cost: {total_variable_maintenance_cost}
Total fuel cost: {total_fuel_cost}
Total operational cost: {total_operational_cost}
Detailed costs:''')
for id in range(last_id):
    print(f'\t{vehicles[id].type} (ID: {id+1}):')
    print(f'''\t\tFixed maintenace: {vehicles[id].fixed_cost}
\t\tVariable maintenace: {vehicles[id].variable_maintenance}
\t\tFuel cost: {vehicles[id].fuel_cost}''')