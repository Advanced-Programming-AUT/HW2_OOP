from food import AbstractFoodClassParent


class BurgerClassChild(AbstractFoodClassParent):
    def __init__(self, layers_input_string, bun_type_input_string, extras_input_list=None):
        super().__init__("Burger")
        self.layers_attribute = layers_input_string
        self.bun_type_attribute = bun_type_input_string
        self.extras_list_attribute = extras_input_list if extras_input_list else []

    def calculate_price_method(self):
        base_price_value = 0
        if self.layers_attribute == "Single":
            base_price_value = 65
        elif self.layers_attribute == "Double":
            base_price_value = 95
        elif self.layers_attribute == "Triple":
            base_price_value = 125

        extras_total_price_value = 0
        for extra_item in self.extras_list_attribute:
            if extra_item == "Egg":
                extras_total_price_value += 15
            elif extra_item == "Bacon":
                extras_total_price_value += 25
            elif extra_item == "Cheese":
                extras_total_price_value += 10

        final_price_result = base_price_value + extras_total_price_value
        return final_price_result

    def get_burger_details_method(self):
        details_string = f"{self.layers_attribute} Layer Burger with {self.bun_type_attribute} bun"
        if self.extras_list_attribute:
            details_string += " and " + ", ".join(self.extras_list_attribute)
        return details_string