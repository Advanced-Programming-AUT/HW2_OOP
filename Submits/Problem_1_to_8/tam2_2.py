from abc import ABC, abstractmethod
discount_codes = {'DISCOUNT10':0.1}

class Food(ABC):
    FoodId = 0
    def __init__(self, name):
        Food.FoodId += 1
        self.food_id = Food.FoodId
        self.name = name
    @abstractmethod
    def calculate_price(self):
        pass
    def __add__(self, other):
        total_price = self.calculate_price() + other.calculate_price()
        return total_price
    def __mul__(self, other):
        total_price = self.calculate_price() * other
        return total_price

class Pizza(Food):
    def __init__(self, size, type, extras = None):
        super().__init__(f'{size} {type} Pizza')
        self.size = size
        self.type = type
        if isinstance(extras, list):
            self.extras = extras
        else:
            self.extras = []
    def calculate_price(self):
        price_size = {'Small':8, 'Medium':12, 'Large':16}
        price_extras = {'Extra Cheese':2, 'Extra Sauce':1.5, 'Olives':1}
        total_price = price_size[self.size]
        for i in self.extras:
            total_price += price_extras[i]
        return total_price

class Burger(Food):
    def __init__(self, meat_layers, extras = None):
        super().__init__(f'{meat_layers} Burger')
        self.meat_layers = meat_layers
        if isinstance(extras, list):
            self.extras = extras
        else:
            self.extras = []
    def calculate_price(self):
        price_meat_layers = {'Single':6, 'Double':9, 'Triple':12}
        price_extras = {'Cheese':1, 'Bacon':2, 'Egg':1.5}
        total_price = price_meat_layers[self.meat_layers]
        for i in self.extras:
            total_price += price_extras[i]
        return total_price

class Drink(Food):
    def __init__(self, volume, type):
        super().__init__(f'{volume} {type}')
        self.volume = volume
        self.type = type
    def calculate_price(self):
        price_volume = {'300ml':2, '500ml':3, '1L':5}
        total_price = price_volume[self.volume]
        return total_price

class Order:
    def __init__(self):
        self.order = {}
    def add_item(self, food, quantity):
        if food.food_id not in self.order:
            self.order[food.food_id] = {'Food':food, 'Quantity':quantity}
        elif food.id in self.order:
            self.order[food.food_id]['Quantity'] += quantity
    def remove_item(self, food_id):
        if food_id in self.order:
            self.order.pop(food_id)
    def calculate_total(self):
        total_price = 0
        for item in self.order.values():
            total_price += item['Food'].calculate_price() * item['Quantity']
        return total_price
    def apply_discount(self, code):
        total_price = self.calculate_total()
        if code in discount_codes:
            total_price *= 1 - discount_codes[code]
        return total_price
    def display_order(self):
        print('Order Summary:')
        for item in self.order.values():
            print(f'{item["Quantity"]}X {item["Food"].name} (ID : {item["Food"].food_id}) -${item["Food"].calculate_price()} each')
        print(f'Total Price : ${self.calculate_total()}')



pizza = Pizza("Large", "Pepperoni", extras=["Extra Cheese", "Olives"])
burger = Burger("Double", extras=["Cheese", "Bacon"])
drink = Drink("500ml", "Soda")

order = Order()
order.add_item(pizza, 2)
order.add_item(burger, 1)
order.add_item(drink, 3)

order.display_order()
print(f'Total price after DISCOUNT10: {order.apply_discount("DISCOUNT10"):.2f}')




