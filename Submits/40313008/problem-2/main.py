

from abc import ABC, abstractmethod

class Food(ABC):
    id_counter = 1

    def __init__(self, name):
        self.food_id = Food.id_counter
        Food.id_counter += 1
        self.name = name

    @abstractmethod
    def calculate_price(self):
        pass

    def __add__(self, other):
        return self.calculate_price() + other.calculate_price()

    def __mul__(self, quantity):
        return self.calculate_price() * quantity


class Pizza(Food):
    def __init__(self, size, pizza_type, extras=[]):
        super().__init__(pizza_type)
        self.size = size
        self.extras = extras

    def calculate_price(self):
        size_prices = {"Small": 8, "Medium": 12, "Large": 16}
        extras_prices = {"Cheese": 1.5, "Extra Sauce": 1, "Olives": 2}
        price = size_prices[self.size]
        for extra in self.extras:
            price += extras_prices.get(extra, 0)
        return price


class Burger(Food):
    def __init__(self, layer, bun_type, extras=[]):
        super().__init__("Burger")
        self.layer = layer
        self.bun_type = bun_type
        self.extras = extras

    def calculate_price(self):
        layer_prices = {"Single": 6, "Double": 9, "Triple": 12}
        extras_prices = {"Egg": 1.5, "Bacon": 2, "Cheese": 1}
        price = layer_prices[self.layer]
        for extra in self.extras:
            price += extras_prices.get(extra, 0)
        return price


class Drink(Food):
    def __init__(self, volume, drink_type):
        super().__init__(drink_type)
        self.volume = volume

    def calculate_price(self):
        volume_prices = {"300ml": 2, "500ml": 3, "1L": 5}
        return volume_prices[self.volume]


class Order:
    discount_codes = {"DISCOUNT10": 0.1, "DISCOUNT15": 0.15}

    def __init__(self):
        self.items = {}

    def add_item(self, food, quantity):
        if food.food_id in self.items:
            self.items[food.food_id]["quantity"] += quantity
        else:
            self.items[food.food_id] = {"food": food, "quantity": quantity}

    def remove_item(self, food_id):
        if food_id in self.items:
            del self.items[food_id]
        else:
            print("Item not found in order.")

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["food"] * item["quantity"]
        return total

    def apply_discount(self, code):
        if code in self.discount_codes:
            total = self.calculate_total()
            discount = self.discount_codes[code]
            return total * (1 - discount)
        else:
            print("Invalid discount code.")
            return self.calculate_total()

    def display_order(self):
        print("Order Summary:")
        for item in self.items.values():
            food = item["food"]
            quantity = item["quantity"]
            print(f"{quantity}x {food.name} (ID: {food.food_id}) - ${food.calculate_price()} each")
        print(f"Total Price: ${self.calculate_total()}")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pizza = Pizza("Large", "Pepperoni", extras=["Cheese", "Extra Sauce"])
    burger = Burger("Double", "Brioche", extras=["Bacon", "Cheese"])
    drink = Drink("500ml", "Soda")

    order = Order()
    order.add_item(pizza, 2)
    order.add_item(burger, 1)
    order.add_item(drink, 3)

    order.display_order()
    print(f"Total price after DISCOUNT10: ${order.apply_discount('DISCOUNT10')}")



