from abc import ABC, abstractmethod

class Food(ABC):
    food_iter = 1

    def __init__(self, name):
        self.name = name
        self.food_id = Food.food_iter
        Food.food_iter += 1

    @abstractmethod
    def calculate_price(self):
        pass

    def add(self, other):
        if isinstance(other, Food):
            return self.calculate_price() + other.calculate_price()
        raise TypeError("Can only add Food objects")

    def mul(self, number):
        if isinstance(number, int):
            return self.calculate_price() * number
        return NotImplemented

class Pizza(Food):
    PRICES = {
        'size': {'small': 8, 'medium': 12, 'large': 16},
        'type': {'Pepperoni': 0, 'Margherita': 0},
        'extras': {'Extra Cheese': 2, 'Extra Sauce': 1.5, 'Olives': 1}
    }

    def __init__(self, size, type_="Pepperoni", extras=[]):
        display_size = size.capitalize()
        super().__init__(f"{display_size} Pizza with extras: {', '.join(extras) if extras else 'None'}")
        self.size = size.lower()
        self.type_ = type_
        self.extras = extras

    def calculate_price(self):
        return (Pizza.PRICES['size'][self.size] +
                Pizza.PRICES['type'][self.type_] +
                sum(Pizza.PRICES['extras'][extra] for extra in self.extras))

class Burger(Food):
    PRICES = {
        'layers': {'Single': 6, 'Double': 9, 'Triple': 12},
        'bun': {'Regular': 0, 'Sesame': 1, 'Brioche': 1.5},
        'extras': {'Cheese': 1, 'Bacon': 2, 'Egg': 1.5}
    }

    def __init__(self, layers, bun="Regular", extras=[]):
        super().__init__(f"{layers} Burger with extras: {', '.join(extras) if extras else 'None'}")
        self.layers = layers
        self.bun = bun
        self.extras = extras

    def calculate_price(self):
        return (Burger.PRICES['layers'][self.layers] +
                Burger.PRICES['bun'][self.bun] +
                sum(Burger.PRICES['extras'][extra] for extra in self.extras))

class Drink(Food):
    PRICES = {
        'volume': {'300ml': 2, '500ml': 3, '1L': 4},
        'type': {'Water': 0, 'Juice': 0, 'Soda': 0}
    }

    def __init__(self, volume, type_):
        super().__init__(f"{volume} {type_}")
        self.volume = volume
        self.type_ = type_

    def calculate_price(self):
        return Drink.PRICES['volume'][self.volume] + Drink.PRICES['type'][self.type_]

class Order:
    def __init__(self):
        self.discount_dict = {'DISCOUNT10': 10, 'DISCOUNT20': 20, 'DISCOUNT30': 30}
        self.orders_dict = {}

    def add_item(self, food, quantity):
        self.orders_dict[food] = quantity

    def calculate_total(self):
        price = 0
        for food, quantity in self.orders_dict.items():
            price += food.calculate_price() * quantity
        return price

    def apply_discount(self, code):
        if code in self.discount_dict:
            discount_percentage = self.discount_dict[code]
            total = self.calculate_total()
            discounted_price = total * (1 - discount_percentage / 100)
            return discounted_price
        return self.calculate_total()

    def display_order(self):
        print("Order Summary:")
        for food, quantity in self.orders_dict.items():
            price_each = food.calculate_price()
            price_str = f"{price_each:.1f}" if price_each.is_integer() else f"{price_each}"
            print(f"{quantity}x {food.name} (ID: {food.food_id}) - ${price_str} each")

#checking code using test case
pizza1 = Pizza("large", extras=["Extra Cheese", "Extra Sauce"])
pizza2 = Pizza("medium", extras=["Olives"])
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
print(f"Total Price: ${test_order.calculate_total():.2f}")
print(f"Total price after DISCOUNT10: ${test_order.apply_discount('DISCOUNT10'):.2f}")
print(f"Total price after DISCOUNT20: ${test_order.apply_discount('DISCOUNT20'):.2f}")
print(f"Total price after DISCOUNT30: ${test_order.apply_discount('DISCOUNT30'):.2f}")