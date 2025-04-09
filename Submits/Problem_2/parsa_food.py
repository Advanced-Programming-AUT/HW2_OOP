from abc import ABC, abstractmethod


class Food(ABC):
    ids = 1

    def __init__(self, name, size, food_type, extras):
        self.name = name
        self.food_id = Food.ids
        Food.ids += 1
        self.size = size
        self.food_type = food_type
        self.extras = extras

    @abstractmethod
    def calculate_price(self):
        ...

    def __add__(self, other):
        return self.calculate_price() + other.calculate_price()

    def __mul__(self, other):
        return self.calculate_price() * other


class Pizza(Food):
    prices = {"Small": 8, "Medium": 12, "Large": 16, "Cheese": 2, "Extra Sauce": 1.5, "Olives": 1}

    def __init__(self, size, food_type=None, extras=None):
        super().__init__("pizza", size, food_type, extras)

    def calculate_price(self):
        price = 0
        price += self.prices.get(self.size, 0)
        price += self.prices.get(self.food_type, 0)
        for extra in self.extras:
            price += self.prices[extra]
        return price


class Burger(Food):
    prices = {"Single": 6, "Double": 9, "Triple": 12, "Cheese": 1, "Bacon": 2, "Egg": 1.5}

    def __init__(self, size, food_type=None, extras=None):
        super().__init__("burger", size, food_type, extras)

    def calculate_price(self):
        price = 0
        price += self.prices.get(self.size, 0)
        price += self.prices.get(self.food_type, 0)
        for extra in self.extras:
            price += self.prices[extra]
        return price


class Drink(Food):
    prices = {"300ml": 2, "500ml": 3, "1L": 5}

    def __init__(self, size, food_type=None, extras=None):
        super().__init__(food_type, size, food_type, extras)

    def calculate_price(self):
        price = 0
        price += self.prices.get(self.size, 0)
        price += self.prices.get(self.food_type, 0)
        return price


class Order:
    foods = {}
    discounts = {"DISCOUNT10": 0.1, "DISCOUNT20": 0.2, "DISCOUNT30": 0.3}

    def add_item(self, food, quantity):
        self.foods[food] = quantity

    def remove_item(self, food_id):
        for food in self.foods:
            if food.food_id == food_id:
                del self.foods[food]

    def calculate_total(self):
        total = 0
        for food in self.foods:
            total += food.calculate_price() * self.foods[food]
        return total

    def apply_discount(self, code):
        total = self.calculate_total()
        if code in self.discounts:
            total *= (1 - self.discounts[code])
        return total

    def display_order(self):
        print("Order Summary:")
        for food, quantity in self.foods.items():
            print(f"{quantity}x {food.size} {food.name.capitalize()} "
                  f"{f"with extras: {", ".join([extra for extra in food.extras])} " if food.extras else ''}"
                  f"(ID: {food.food_id}) - ${food.calculate_price()} each")
        print(f"Total: ${self.calculate_total()}")


pizza1 = Pizza("Large", extras=["Cheese", "Extra Sauce"])
pizza2 = Pizza("Medium", extras=["Olives"])
burger1 = Burger("Double", extras=["Bacon", "Cheese"])
burger2 = Burger("Triple", extras=["Egg"])
drink1 = Drink("500ml", "Soda")
drink2 = Drink("1L", "Juice")
test_order = Order()
test_order.add_item(pizza1, 2)
test_order.add_item(pizza2, 1)
test_order.add_item(burger1, 1)

test_order.add_item(burger2, 2)
test_order.add_item(drink1, 3)
test_order.add_item(drink2, 2)
test_order.display_order()
print(f"Total price after DISCOUNT10: ${test_order.apply_discount('DISCOUNT10')}")
print(f"Total price after DISCOUNT20: ${test_order.apply_discount('DISCOUNT20')}")
print(f"Total price after DISCOUNT30: ${test_order.apply_discount('DISCOUNT30')}")

'''
Order Summary:
2x Large Pizza with extras: Cheese, Extra Sauce (ID: 1) - $19.5 each
1x Medium Pizza with extras: Olives (ID: 2) - $13 each
1x Double Burger with extras: Bacon, Cheese (ID: 3) - $12 each
2x Triple Burger with extras: Egg (ID: 4) - $13.5 each
3x 500ml Soda (ID: 5) - $3 each
2x 1L Juice (ID: 6) - $5 each
Total Price: $94.50
Total price after DISCOUNT10: $85.05
Total price after DISCOUNT20: $75.60
Total price after DISCOUNT30: $66.15
'''
