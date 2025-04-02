list_all_vehicle = []     
class Vehicle:
    def __init__(self , type, fixed_cost, variable_cost_per_km, fuel_consumption_per_km, id):
        self.type = type
        self.fixed_cost = int(fixed_cost)
        self.variable_cost_per_km = int(variable_cost_per_km)
        self.fuel_consumption_per_km = int(fuel_consumption_per_km)
        self.id = id
        list_all_vehicle.append(self)
        if self.type == "PLANE":
            self.fuel = "JET_FUEL"
        if self.type == "TRUCK":
            self.fuel = "DIESEL"
        if self.type == "PICKUP" or self.type == "CAR":
            self.fuel = "BENZIN"
            
price_of_fuel = {}
dict_all_distances = {"A B": 100, "A C": 200, "A D": 150, "A E": 300, "B C": 250, "B D": 180, "B E": 400, "C D": 120, "C E": 350, "D E": 280}
list_all_trips_month = []
id = 1
order = "a"
while order[0] != "Exit":
    order = input().split()
    if order[0] == "ADD_VEHICLE":
        
        vehicle = Vehicle(order[1], order[2], order[3], order[4], id)
        id += 1
        print(f"Vehicle {order[1]} added with fixed cost: {order[2]} , variable cost per km: {order[3]} , fuel consumption per km: {order[4]}\n")
         
    if order[0] == "SET_FUEL_PRICE":
        price_of_fuel[order[1]] = int(order[2])
        print(f"Fuel price for {order[1]} set to {order[2]} per liter.\n")
        
    if order[0] == "ADD_TRIP":
        for vehicle in list_all_vehicle:
            if vehicle.id == int(order[1]):
                vehicle = vehicle
                break
        origin = order[2]
        distination = order[3]
        if ord(order[3]) < ord(order[2]):
            origin = order[3]
            distination = order[2]
        distance = dict_all_distances[f"{origin} {distination}"]
        list_all_trips_month.append([vehicle, distance])
        print(f"Trip registered: {vehicle.type} from {order[2]} to {order[3]} carrying {order[4]} kg.\n")
        
    if order[0] == "END_MONTH":
        print("End of month report:")
        fixed_cost = 0
        variable_cost = 0
        fuel_cost = 0
        all_costs = 0
        for vehicle_distance in list_all_trips_month:
            vehicle = vehicle_distance[0]
            distance = vehicle_distance[1]
            fixed_cost += vehicle.fixed_cost
            variable_cost += vehicle.variable_cost_per_km * distance
            fuel_cost += vehicle.fuel_consumption_per_km * distance * price_of_fuel[vehicle.fuel]
        all_costs = fixed_cost + fuel_cost + variable_cost
        print(f"Total fixed maintenance cost: {fixed_cost}\n")
        print(f"Total variable maintenance cost: {variable_cost}\n")
        print(f"Total fuel cost: {fuel_cost}\n")
        print(f"Total operational cost: {all_costs}\n")
        print("Detaieled costs: ")
        for vehicle_distance in list_all_trips_month:
            vehicle = vehicle_distance[0]
            distance = vehicle_distance[1]
            print(f" {vehicle.type} (ID: {vehicle.id}):")
            print(f"  - Fixed maintenance: {vehicle.fixed_cost}")
            print(f"  - Variable maintenance: {vehicle.variable_cost_per_km * distance}")
            print(f"  - Fuel cost: {vehicle.fuel_consumption_per_km * distance * price_of_fuel[vehicle.fuel]}\n")
        list_all_trips_month.clear()