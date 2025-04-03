from food import AbstractFoodClassParent


class DrinkClassChild(AbstractFoodClassParent):
    def __init__(self, size_input_string, type_input_string):
        super().__init__("Drink")
        self.size_attribute = size_input_string
        self.type_attribute = type_input_string

    def calculate_price_method(self):
        price_value = 0
        if self.size_attribute == "360ml":
            price_value = 3
        elif self.size_attribute == "560ml":
            price_value = 4
        elif self.size_attribute == "1L":
            price_value = 5

        if self.type_attribute == "Juice":
            price_value += 1
        elif self.type_attribute == "Soda":
            price_value += 0.5

        return price_value

    def get_drink_details_method(self):
        return f"{self.size_attribute} {self.type_attribute}"