from abc import ABC, abstractmethod
import random
class Food(ABC):
    def __init__(self, name):
        self.food_id = random.randint(0,10)
        self.name = name

    @abstractmethod
    def calculate_price(self):
        pass

    def __add__(self, other):
        if isinstance(other, Food):
            return self.calculate_price() + other.calculate_price()
        return NotImplemented

class Pizza(Food):
    def __init__(self, size, kind, topping=None):
        super().__init__(f"{size} {kind}")
        self.size = size
        self.kind = kind
        self.topping = topping if topping is not None else []

    def calculate_price(self):
        result_price = 0
        if self.size == "Small":
            result_price += 8
        elif self.size == "Medium":
            result_price += 12
        elif self.size == "Large":
            result_price += 16

        for p in self.topping:
            if p == "Extra Cheese":
                result_price += 2
            elif p == "Extra Sauce":
                result_price += 1.5
            elif p == "Olives":
                result_price += 1

        return result_price

class Burger(Food):
    def __init__(self, layer, bread, toppings=None):
        super().__init__(f"{layer} Burger with {bread} bun")
        self.layer = layer
        self.bread = bread
        self.topping = toppings if toppings is not None else []

    def calculate_price(self):
        result_price = 0
        if self.layer == "Single Layer":
            result_price += 8
        elif self.layer == "Double Layer":
            result_price += 12
        elif self.layer == "Triple Layer":
            result_price += 16

        for p2 in self.topping:
            if p2 == "Cheese":
                result_price += 1
            elif p2 == "Egg":
                result_price += 1.5
            elif p2 == "Bacon":
                result_price += 2

        return result_price

class Drink(Food):
    def __init__(self, size, kind):
        super().__init__(f"{size} {kind}")
        self.size = size
        self.kind = kind

    def calculate_price(self):
        result_price = 0
        if self.size == "300ml":
            result_price += 2
        elif self.size == "500ml":
            result_price += 3
        elif self.size == "1L":
            result_price += 5
        return result_price

class Order:
    def __init__(self):
        self.items = {}
        self.discount_code = {"DISCOUNT10": 0.10, "DISCOUNT20": 0.20}
        self.final_code = None

    def add_item(self, food, quantity):
        if food.food_id in self.items:
            self.items[food.food_id]['quantity'] += quantity
        else:
            self.items[food.food_id] = {
                'food': food,
                'quantity': quantity
            }

    def remove_item(self, food_id):
        if food_id in self.items:
            del self.items[food_id]

    def calculate_total(self):
        total = sum(item['food'].calculate_price() * item['quantity'] for item in self.items.values())

        if self.final_code:
            discount_percent = self.discount_code[self.final_code]
            total -= total * discount_percent

        return total

    def apply_discount(self, code):
        if code in self.discount_code:
            self.final_code = code
        else:
            print("Invalid discount code.")

    def display_order(self):
        print("Order Details:")
        for item in self.items.values():
            food = item['food']
            quantity = item['quantity']
            price = food.calculate_price()
            print(f"{quantity}X {food.name} ID:({food.food_id}), Unit Price: ${price:.2f}, Total: ${price * quantity:.2f}")

        total_price = self.calculate_total()
        print(f"Total Price before discount: ${total_price:.2f}")

##### Main
pizza = Pizza("Large", "Pepperoni", topping=["Extra Cheese", "Extra Sauce"])
burger = Burger("Double Layer", "Brioche", toppings=["Bacon", "Cheese"])
drink = Drink("500ml", "Soda")

order = Order()
order.add_item(pizza, 2)
order.add_item(burger, 1)
order.add_item(drink, 3)

order.display_order()

order.apply_discount('DISCOUNT10')

total_after_discount = order.calculate_total()

print(f"Total price after DISCOUNT10: ${total_after_discount:.2f}")