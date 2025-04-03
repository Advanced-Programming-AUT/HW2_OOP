from PARSA_FOOD.burger import BurgerClassChild
from PARSA_FOOD.drink import DrinkClassChild
from PARSA_FOOD.pizza import PizzaClassChild


class OrderManagementClass:
    def __init__(self):
        self.items_dictionary_attribute = {}
        self.discount_codes_dictionary = {
            "DISCOUNT10": 0.1,
            "DISCOUNT15": 0.15
        }

    def add_item_to_order_method(self, food_object, quantity_integer=1):
        if food_object.food_id_attribute in self.items_dictionary_attribute:
            self.items_dictionary_attribute[food_object.food_id_attribute]["quantity"] += quantity_integer
        else:
            self.items_dictionary_attribute[food_object.food_id_attribute] = {
                "food": food_object,
                "quantity": quantity_integer
            }

    def remove_item_from_order_method(self, food_object):
        if food_object.food_id_attribute in self.items_dictionary_attribute:
            del self.items_dictionary_attribute[food_object.food_id_attribute]

    def calculate_total_price_method(self):
        total_price_value = 0
        for item_id in self.items_dictionary_attribute:
            item_data = self.items_dictionary_attribute[item_id]
            total_price_value += item_data["food"].calculate_price_method() * item_data["quantity"]
        return total_price_value

    def apply_discount_code_method(self, discount_code_string):
        total_before_discount = self.calculate_total_price_method()
        if discount_code_string in self.discount_codes_dictionary:
            discount_percentage = self.discount_codes_dictionary[discount_code_string]
            discounted_price = total_before_discount * (1 - discount_percentage)
            return discounted_price
        return total_before_discount

    def display_order_details_method(self):
        order_details_string = "Order Summary:\n"
        for item_id in self.items_dictionary_attribute:
            item_data = self.items_dictionary_attribute[item_id]
            food_object = item_data["food"]
            quantity = item_data["quantity"]
            price = food_object.calculate_price_method()

            if isinstance(food_object, PizzaClassChild):
                details = food_object.get_pizza_details_method()
            elif isinstance(food_object, BurgerClassChild):
                details = food_object.get_burger_details_method()
            elif isinstance(food_object, DrinkClassChild):
                details = food_object.get_drink_details_method()
            else:
                details = food_object.name_attribute

            order_details_string += f"{quantity}x {details} (ID: {food_object.food_id_attribute}) - ${price} each\n"

        order_details_string += f"Total Price: ${self.calculate_total_price_method()}\n"
        return order_details_string