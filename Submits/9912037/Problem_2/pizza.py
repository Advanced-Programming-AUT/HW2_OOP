from food import AbstractFoodClassParent


class PizzaClassChild(AbstractFoodClassParent):
    def __init__(self, size_input_string, type_input_string, extras_input_list=None):
        super().__init__("Pizza")
        self.size_attribute = size_input_string
        self.type_attribute = type_input_string
        self.extras_list_attribute = extras_input_list if extras_input_list else []

    def calculate_price_method(self):
        base_price_value = 0
        if self.size_attribute == "Small":
            base_price_value = 85
        elif self.size_attribute == "Medium":
            base_price_value = 125
        elif self.size_attribute == "Large":
            base_price_value = 165

        extras_total_price_value = 0
        for extra_item in self.extras_list_attribute:
            if extra_item == "Extra Cheese":
                extras_total_price_value += 25
            elif extra_item == "Extra Sauce":
                extras_total_price_value += 1.55
            elif extra_item == "Olives":
                extras_total_price_value += 15

        final_price_result = base_price_value + extras_total_price_value
        return final_price_result

    def get_pizza_details_method(self):
        details_string = f"{self.size_attribute} {self.type_attribute} Pizza"
        if self.extras_list_attribute:
            details_string += " with " + ", ".join(self.extras_list_attribute)
        return details_string