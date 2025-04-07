class VehicleClassForLogistics:
    def __init__(self, vehicle_type_input, vehicle_id_input, fixed_cost_input, variable_cost_input, fuel_consumption_input):
        self.type_of_vehicle_attribute = vehicle_type_input
        self.id_number_of_vehicle_attribute = vehicle_id_input
        self.fixed_maintenance_cost_attribute = fixed_cost_input
        self.variable_cost_per_km_attribute = variable_cost_input
        self.fuel_consumption_per_km_attribute = fuel_consumption_input
        self.total_distance_traveled_attribute = 0
        self.monthly_fuel_cost_attribute = 0
        self.monthly_variable_cost_attribute = 0

    def add_trip_method(self, distance_input, fuel_price_input):
        self.total_distance_traveled_attribute += distance_input
        fuel_cost_for_trip = distance_input * self.fuel_consumption_per_km_attribute * fuel_price_input
        self.monthly_fuel_cost_attribute += fuel_cost_for_trip
        variable_cost_for_trip = distance_input * self.variable_cost_per_km_attribute
        self.monthly_variable_cost_attribute += variable_cost_for_trip
        return fuel_cost_for_trip + variable_cost_for_trip

    def get_monthly_cost_method(self):
        total_cost = self.fixed_maintenance_cost_attribute + self.monthly_variable_cost_attribute + self.monthly_fuel_cost_attribute
        return total_cost

    def reset_monthly_data_method(self):
        self.total_distance_traveled_attribute = 0
        self.monthly_fuel_cost_attribute = 0
        self.monthly_variable_cost_attribute = 0

    def get_vehicle_details_method(self):
        details_string = ""
        details_string += self.type_of_vehicle_attribute + " (ID: " + str(self.id_number_of_vehicle_attribute) + "):\n"
        details_string += "    Fixed maintenance: " + str(self.fixed_maintenance_cost_attribute) + "\n"
        details_string += "    Variable maintenance: " + str(self.monthly_variable_cost_attribute) + "\n"
        details_string += "    Fuel cost: " + str(self.monthly_fuel_cost_attribute) + "\n"
        return details_string