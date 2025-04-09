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
    size_prices = {"Small": 40, "Medium": 70, "Large": 105}
    extra_prices = {"Cheese": 12, "Extra Sauce": 8, "Olives": 8}

    def __init__(self, size, pizza_type, extras=[]):
        super().__init__(f"{size} {pizza_type} Pizza")
        self.size = size
        self.pizza_type = pizza_type
        self.extras = extras

    def calculate_price(self):
        price = self.size_prices[self.size]
        for extra in self.extras:
            price += self.extra_prices.get(extra, 0)
        return price

class Burger(Food):
    layer_prices = {"Single": 60, "Double": 90, "Triple": 120}
    extra_prices = {"Cheese": 10, "Bacon": 20, "Egg": 15}

    def __init__(self, layers, burger_type, extras=[]):
        super().__init__(f"{layers} Burger with {burger_type} Bun")
        self.layers = layers
        self.bun_type = burger_type
        self.extras = extras

    def calculate_price(self):
        price = self.layer_prices[self.layers]
        for extra in self.extras:
            price += self.extra_prices.get(extra, 0)
        return price

class Drink(Food):
    volume_prices = {"300ml": 10, "500ml": 15, "1L": 20}

    def __init__(self, volume, drink_type):
        super().__init__(f"{volume} {drink_type}")
        self.volume = volume
        self.drink_type = drink_type

    def calculate_price(self):
        return self.volume_prices[self.volume]

class Order(object):

#-----Takhfif haye mokhtalef ham add kon-----#
    discount_codes = {"DISCOUNT30": 0.30}

    def __init__(self):
        self.items = {}

    def add_item(self, food, quantity):
        self.items[food] = self.items.get(food, 0) + quantity

    def remove_item(self, food_id):
        self.items = {food: qty for food, qty in self.items.items() if food.food_id != food_id}

    def eval_total(self):
        return sum(food.calculate_price() * qty for food, qty in self.items.items())

    def apply_discount(self, code):
        discount = self.discount_codes.get(code, 0)
        return self.eval_total() * (1 - discount)

    def display_order(self):
        print("Order Summary:")
        for food, qty in self.items.items():
            print(f"{qty}x {food.name} (ID: {food.food_id}) - ${food.calculate_price()} each")
        print(f"Total Price: ${self.eval_total()}")

pizza = Pizza("Large", "Pepperoni", extras=["Cheese", "Extra Sauce"])
burger = Burger("Double", "Brioche", extras=["Bacon", "Cheese"])
drink = Drink("500ml", "Soda")

order = Order()
order.add_item(pizza, 2)
order.add_item(burger, 1)
order.add_item(drink, 3)

order.display_order()
print(f"Total price after DISCOUNT30: ${order.apply_discount('DISCOUNT30')}")