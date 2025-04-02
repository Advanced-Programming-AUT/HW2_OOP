from abc import ABC, abstractmethod


class Food(ABC):
    food_id_count = 1

    def __init__(self, name):
        self.food_id = Food.food_id_count
        Food.food_id_count += 1
        self.name = name

    @abstractmethod
    def calculate_price(self):
        pass

    def __add__(self, other):
        return self.calculate_price() + other.calculate_price()

    def __mul__(self, number):
        return self.calculate_price() * number


class Pizza(Food):
    size_prices = {"Small": 8, "Medium": 12, "Large": 16}
    extras_prices = {"Cheese": 2, "Extra Sauce": 1.5, "Olives": 1, "Mushrooms": 2, "Peppers": 1.5}

    def __init__(self, size, type, extras=[]):
        super().__init__(type)
        self.size = size
        self.extras = extras

    def calculate_price(self):
        price = Pizza.size_prices[self.size]
        for extra in self.extras:
            price += Pizza.extras_prices.get(extra, 0)
        return price


class Burger(Food):
    layer_prices = {"Single": 6, "Double": 9, "Triple": 12}
    extras_prices = {"Cheese": 1, "Bacon": 2, "Egg": 1.5, "Lettuce": 1, "Tomato": 1}

    def __init__(self, layer, bun, extras=[]):
        super().__init__("Burger")
        self.layer = layer
        self.bun = bun
        self.extras = extras

    def calculate_price(self):
        price = Burger.layer_prices[self.layer]
        for extra in self.extras:
            price += Burger.extras_prices.get(extra, 0)
        return price


class Drink(Food):
    size_prices = {"300ml": 2, "500ml": 3, "1L": 5}

    def __init__(self, size, type, sugar_free=False):
        super().__init__(type)
        self.size = size
        self.sugar_free = sugar_free

    def calculate_price(self):
        price = Drink.size_prices[self.size]
        if self.sugar_free:
            price += 0.5
        return price


class Order:
    discount_codes = {"DISCOUNT10": 10, "STUDENT20": 20}

    def __init__(self):
        self.items = {}

    def add_item(self, food, quantity):
        self.items[food.food_id] = (food, quantity)

    def remove_item(self, food_id):
        if food_id in self.items:
            del self.items[food_id]

    def calculate_total(self):
        return sum(food.calculate_price() * quantity for food, quantity in self.items.values())

    def apply_discount(self, code):
        if code in Order.discount_codes:
            discount = Order.discount_codes[code]
            return self.calculate_total() * (1 - discount / 100)
        return self.calculate_total()

    def display_order(self):
        for food, quantity in self.items.values():
            print(f"{quantity}x {food.name} (ID: {food.food_id}) - ${food.calculate_price()} each")
        print(f"Total Price: ${self.calculate_total()}")



order = Order()
while True:
    request = input("select  (Pizza, Burger, Drink) or 'done' to end: ").strip()
    if request.lower() == 'done':
        break

    if request == "Pizza":
        size = input("choose the  size (Small, Medium, Large): ")
        type_ = input("choose the type (Margherita, Pepperoni, Veggie): ")
        extras = input("choose  extras (Cheese, Extra Sauce, Olives, Mushrooms, Peppers) separated by commas: ").split(
            ',')
        pizza = Pizza(size, type_, extras)
        quantity = int(input("choose the quantity: "))
        order.add_item(pizza, quantity)
    elif request == "Burger":
        layer = input("choose the layer (Single, Double, Triple): ")
        bun = input("choose the bun type (Brioche, Sesame, Regular): ")
        extras = input("choose extras (Cheese, Bacon, Egg, Lettuce, Tomato) separated by commas: ").split(',')
        burger = Burger(layer, bun, extras)
        quantity = int(input("choose the quantity: "))
        order.add_item(burger, quantity)
    elif request == "Drink":
        size = input("choose the size (300ml, 500ml, 1L): ")
        type_ = input("choose the type (Water, Juice, Soda, Tea, Coffee): ")
        sugar_free = input("Do you want it sugar-free? (y/n): ").strip().lower() == "y"
        drink = Drink(size, type_, sugar_free)
        quantity = int(input("choose the quantity: "))
        order.add_item(drink, quantity)
    else:
        print(" Try again...")

order.display_order()
discount_code = input(" please Enter  the  code (or press enter to skip): ").strip()
if discount_code:
    print(f"Total price after discount: ${order.apply_discount(discount_code)}")