class FuelPriceManagementClass:
    def __init__(self):
        self.fuel_prices_dictionary = {
            'GASOLINE': 0,
            'DIESEL': 0,
            'JET_FUEL': 0
        }

    def set_fuel_price_method(self, fuel_type_input, price_input):
        if fuel_type_input in self.fuel_prices_dictionary:
            self.fuel_prices_dictionary[fuel_type_input] = price_input
            return True
        return False

    def get_fuel_price_method(self, fuel_type_input):
        if fuel_type_input in self.fuel_prices_dictionary:
            return self.fuel_prices_dictionary[fuel_type_input]
        return 0