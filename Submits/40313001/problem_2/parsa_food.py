from abc import ABC, abstractmethod

class Food(ABC):
    food_id_counter = 1

    def __init__(self, name):
        self.food_id = Food.food_id_counter
        Food.food_id_counter += 1
        self.name = name

    @abstractmethod
    def calculate_price(self):
        pass

    def __add__(self, other):
        return self.calculate_price() + other.calculate_price()

    def __mul__(self, quantity):
        return self.calculate_price() * quantity


class Pizza(Food):
    SIZE_PRICES = {"Small": 8, "Medium": 12, "Large": 16}
    EXTRA_PRICES = {"Cheese": 2, "Extra Sauce": 1.5, "Olives": 1}

    def __init__(self, size, pizza_type, extras=[]):
        super().__init__(f"{size} {pizza_type} Pizza")
        self.size = size
        self.pizza_type = pizza_type
        self.extras = extras

    def calculate_price(self):
        price = self.SIZE_PRICES[self.size]
        price += sum(self.EXTRA_PRICES[extra] for extra in self.extras if extra in self.EXTRA_PRICES)
        return price


class Burger(Food):
    LAYER_PRICES = {"Single": 6, "Double": 9, "Triple": 12}
    EXTRA_PRICES = {"Cheese": 1, "Bacon": 2, "Egg": 1.5}

    def __init__(self, layers, bun_type, extras=[]):
        super().__init__(f"{layers} Burger with {bun_type} Bun")
        self.layers = layers
        self.bun_type = bun_type
        self.extras = extras

    def calculate_price(self):
        price = self.LAYER_PRICES[self.layers]
        price += sum(self.EXTRA_PRICES[extra] for extra in self.extras if extra in self.EXTRA_PRICES)
        return price


class Drink(Food):
    SIZE_PRICES = {"300ml": 2, "500ml": 3, "1L": 5}

    def __init__(self, size, drink_type):
        super().__init__(f"{size} {drink_type}")
        self.size = size
        self.drink_type = drink_type

    def calculate_price(self):
        return self.SIZE_PRICES[self.size]


class Order:
    DISCOUNT_CODES = {"DISCOUNT10": 0.10}

    def __init__(self):
        self.items = {}

    def add_item(self, food, quantity):
        self.items[food.food_id] = (food, quantity)

    def remove_item(self, food_id):
        if food_id in self.items:
            del self.items[food_id]

    def calculate_total(self):
        return sum(food * quantity for food, quantity in self.items.values())

    def apply_discount(self, code):
        discount = self.DISCOUNT_CODES.get(code, 0)
        return round(self.calculate_total() * (1 - discount), 2)

    def display_order(self):
        print("Order Summary:")
        for food, quantity in self.items.values():
            print(f"{quantity}x {food.name} (ID: {food.food_id}) - ${food.calculate_price()} each")
        print(f"Total Price: ${self.calculate_total()}")

#voroodi test
pizza = Pizza("Large", "Pepperoni", extras=["Cheese", "Extra Sauce"])
burger = Burger("Double", "Brioche", extras=["Bacon", "Cheese"])
drink = Drink("500ml", "Soda")

order = Order()
order.add_item(pizza, 2)
order.add_item(burger, 1)
order.add_item(drink, 3)

order.display_order()
print(f"Total price after DISCOUNT10: ${order.apply_discount('DISCOUNT10')}")
