class Vehicle:
    car_id = 1
    fuel_dict = {}
    trip_dic = {}
    city_distance = {
        'AB': 100, 'AC': 200, 'AD': 150, 'AE': 300, 'BA': 100, 'BB': 0, 'BC': 250, 'BD': 180, 'BE': 400,
        'CA': 200, 'CB': 250, 'CC': 0, 'CD': 120, 'CE': 350, 'DA': 150, 'DB': 180, 'DC': 120, 'DD': 0, 'DE': 280,
        'EA': 300, 'EB': 400, 'EC': 350, 'ED': 280, 'EE': 0
    }
    vehicle_dic = {}

    @classmethod
    def add_vehicle(cls, data): #getting the vehicle data from inout
        parts = data.split()
        type_ = parts[1]
        cost_per_month = parts[2]
        vary_cost = parts[3]
        fuel_consume = parts[4]
        car_id = cls.car_id
        cls.vehicle_dic[(type_, car_id)] = {
            'cost_per_month': int(cost_per_month),
            'vary_cost': int(vary_cost),
            'fuel_consume': float(fuel_consume),
            'fuel_type': 'DIESEL' if type_ == 'TRUCK' else 'JET_FUEL' if type_ == 'PLANE' else 'BENZINE'
        }
        cls.car_id += 1 #each time a vehicle is added it gets an id
        return f"Vehicle {type_} added with fixed cost: {cost_per_month} , variable cost per km: {vary_cost}"

    @classmethod
    def set_fuel_price(cls, data):
        parts = data.split()
        fuel_name = parts[1]
        fuel_price = int(parts[2])
        cls.fuel_dict[fuel_name] = fuel_price
        return f"Fuel price for {fuel_name} set to {fuel_price} per liter."

    @classmethod
    def add_trip(cls, data):
        parts = data.split()
        vehicle_id = int(parts[1])
        origin = parts[2]
        destination = parts[3]
        cargo_weight = parts[4]
        way_distance = cls.city_distance[origin + destination] # distance between origin and destination
        for (type_, car_id), details in cls.vehicle_dic.items():
            if car_id == vehicle_id:
                fixed_cost = details['cost_per_month']
                # calculating variable cost: vary_cost * distance
                vary_cost = details['vary_cost'] * way_distance
                # calculating fuel cost: fuel_price * distance * fuel_consume
                fuel_cost = cls.fuel_dict[details['fuel_type']] * way_distance * details['fuel_consume']
                cls.trip_dic[(type_, car_id)] = {
                    'car_id': car_id,
                    'fixed_cost': fixed_cost,
                    'vary_cost': vary_cost,
                    'fuel_cost': fuel_cost
                }
                return f"Trip registered: {type_} from {origin} to {destination} carrying {cargo_weight} kg."
        # if no vehicle with the provided id is found, raise an error
        raise ValueError(f"Vehicle ID {vehicle_id} not found")

    @classmethod
    def report_monthly_pay(cls):
        results = ["End of month report:"]
        total_fixed_cost = sum(details['fixed_cost'] for details in cls.trip_dic.values())
        total_vary_cost = sum(details['vary_cost'] for details in cls.trip_dic.values())
        total_fuel_cost = sum(details['fuel_cost'] for details in cls.trip_dic.values())
        total_operational_cost = total_fixed_cost + total_vary_cost + total_fuel_cost
        # adding summary of the costs to the report
        results.extend([
            f"Total fixed maintenance cost: {int(total_fixed_cost)}",
            f"Total variable maintenance cost: {int(total_vary_cost)}",
            f"Total fuel cost: {int(total_fuel_cost)}",
            f"Total operational cost: {int(total_operational_cost)}",
            "Detailed costs:"
        ])
        # adding detailed costs for each vehicle trip
        for (type_, car_id), details in cls.trip_dic.items():
            results.extend([
                f"{type_} (ID: {car_id}):",
                f"Fixed maintenance: {int(details['fixed_cost'])}",
                f"Variable maintenance: {int(details['vary_cost'])}",
                f"Fuel cost: {int(details['fuel_cost'])}"
            ])
        return "\n".join(results)

# Processing commands
def process_commands(commands):
    results = []
    for command in commands:
        parts = command.split()
        action = parts[0]
        if action == "ADD_VEHICLE":
            results.append(Vehicle.add_vehicle(command))
        elif action in ["FUEL_PRICE", "SET_FUEL_PRICE"]:
            results.append(Vehicle.set_fuel_price(command))
        elif action == "ADD_TRIP":
            results.append(Vehicle.add_trip(command))
        elif action == "END_MONTH":
            results.append(Vehicle.report_monthly_pay())
    return "\n".join(results)


# Geting commands from user input
while True:
    try:
        command_number = int(input('Enter number of commands: '))
        break
    except ValueError:
        print("Please enter a valid number")

commands = []
for _ in range(command_number):
    command = input()
    commands.append(command)


print(process_commands(commands))