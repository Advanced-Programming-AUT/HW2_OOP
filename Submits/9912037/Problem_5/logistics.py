from vehicle import VehicleClassForLogistics
from city_distance import CityDistanceMatrixClass
from fuel_price import FuelPriceManagementClass


class LogisticsManagementSystemClass:
    def __init__(self):
        self.vehicles_list_attribute = []
        self.city_distance_object = CityDistanceMatrixClass()
        self.fuel_price_object = FuelPriceManagementClass()
        self.next_vehicle_id_attribute = 1

    def add_vehicle_method(self, vehicle_type_input, fixed_cost_input, variable_cost_input, fuel_consumption_input):
        new_vehicle = VehicleClassForLogistics(
            vehicle_type_input,
            self.next_vehicle_id_attribute,
            fixed_cost_input,
            variable_cost_input,
            fuel_consumption_input
        )
        self.vehicles_list_attribute.append(new_vehicle)
        self.next_vehicle_id_attribute += 1
        return new_vehicle

    def add_trip_method(self, vehicle_id_input, origin_input, destination_input, cargo_weight_input):
        distance = self.city_distance_object.get_distance_between_cities_method(origin_input, destination_input)
        if distance == 0:
            return False

        vehicle_found = None
        for vehicle_item in self.vehicles_list_attribute:
            if vehicle_item.id_number_of_vehicle_attribute == vehicle_id_input:
                vehicle_found = vehicle_item
                break

        if not vehicle_found:
            return False

        fuel_type = ''
        if vehicle_found.type_of_vehicle_attribute == 'PLANE':
            fuel_type = 'JET_FUEL'
        elif vehicle_found.type_of_vehicle_attribute == 'TRUCK':
            fuel_type = 'DIESEL'
        else:
            fuel_type = 'GASOLINE'

        fuel_price = self.fuel_price_object.get_fuel_price_method(fuel_type)
        vehicle_found.add_trip_method(distance, fuel_price)
        return True

    def set_fuel_price_method(self, fuel_type_input, price_input):
        return self.fuel_price_object.set_fuel_price_method(fuel_type_input, price_input)

    def generate_monthly_report_method(self):
        total_fixed_cost = 0
        total_variable_cost = 0
        total_fuel_cost = 0

        for vehicle_item in self.vehicles_list_attribute:
            total_fixed_cost += vehicle_item.fixed_maintenance_cost_attribute
            total_variable_cost += vehicle_item.monthly_variable_cost_attribute
            total_fuel_cost += vehicle_item.monthly_fuel_cost_attribute

        total_operational_cost = total_fixed_cost + total_variable_cost + total_fuel_cost

        report_string = ""
        report_string += "End of month report:\n"
        report_string += "Total fixed maintenance cost: " + str(total_fixed_cost) + "\n"
        report_string += "Total variable maintenance cost: " + str(total_variable_cost) + "\n"
        report_string += "Total fuel cost: " + str(total_fuel_cost) + "\n"
        report_string += "Total operational cost: " + str(total_operational_cost) + "\n"
        report_string += "Detailed costs:\n"

        for vehicle_item in self.vehicles_list_attribute:
            report_string += vehicle_item.get_vehicle_details_method()

        for vehicle_item in self.vehicles_list_attribute:
            vehicle_item.reset_monthly_data_method()

        return report_string