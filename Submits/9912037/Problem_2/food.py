from abc import ABC, abstractmethod

class AbstractFoodClassParent(ABC):
    food_id_counter_variable = 1

    def __init__(self, name_input_string):
        self.food_id_attribute = AbstractFoodClassParent.food_id_counter_variable
        AbstractFoodClassParent.food_id_counter_variable += 1
        self.name_attribute = name_input_string

    @abstractmethod
    def calculate_price_method(self):
        pass

    def __add__(self, other_food_object):
        total_price_value = self.calculate_price_method() + other_food_object.calculate_price_method()
        return total_price_value

    def __mul__(self, multiplier_integer):
        multiplied_price_value = self.calculate_price_method() * multiplier_integer
        return multiplied_price_value