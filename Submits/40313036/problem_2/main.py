def make_space(s):
    out = ''
    for i in s: out += i + ' '
    return out

class Food:
    def __init__(self, food_id, name):
        self.food_id = food_id
        self.name = name

    def calculate_price(self):
        return 0

    def __add__(self, other):
        return self.calculate_price()+other.calculate_price()

    def __mul__(self, other):
        return self.calculate_price*other

class Pizza(Food):
    def __init__(self, size, type, extras):
        self.size = size
        self.type = type
        self.another = extras

    def calculate_price(self):
        price = {"Small": 8, "Medium": 12, "Large": 16,
                 "Extra Cheese": 2, "Extra Sauce": 1.5, "Olives": 1}
        extra = 0
        for e in self.another: extra += price[e]
        return price[self.size]+extra

    def detail(self):
        return self.size+' '+self.type+" Pizza"+(' with '+make_space(self.another) if len(self.another) > 0 else '')

class Burger(Food):
    def __init__(self, layer, type, extras):
        self.layer = layer
        self.type = type
        self.another = extras

    def calculate_price(self):
        price = {"Single Layer": 6, "Double Layer": 9,
                 "Triple Layer": 9, "Cheese": 1, "Bacon": 2, "Egg": 1.5}
        extra = 0
        for e in self.another: extra += price[e]
        return price[self.layer]+extra

    def detail(self):
        return self.layer+' '+self.type+" Burger"+('with '+make_space(self.another) if len(self.another) > 0 else '')

class Drink(Food):
    def __init__(self, volume, type):
        self.volume = volume
        self.type = type

    def calculate_price(self):
        price = {"300ml": 2, "500ml": 3, "1L": 5}
        return price[self.volume]

    def detail(self):
        return self.volume+' '+self.type

class Order:
    def __init__(self):
        self.item = {}
        self.last_id = 0
        self.code_dict = {"DISCOUNT10": 0.9}
        self.codes = []
        self.discount = 1

    def add_item(self, food, quantity):
        self.item[self.last_id] = [food, quantity]
        self.last_id += 1

    def remove_item(self, food_id):
        if food_id in self.item:
            self.item[food_id][1] = 0

    def calculate_total(self):
        total = 0
        for item in self.item:
            total += self.item[item][0].calculate_price()*self.item[item][1]
        return total

    def apply_discount(self, code):
        self.discount *= self.code_dict[code]
        return self.calculate_total()*self.discount

    def display_order(self):
        for item in self.item:
            if self.item[item][1] > 0:
                print(f"{self.item[item][1]}x {self.item[item][0].detail()} (ID: {item}) - ${self.item[item][0].calculate_price()} each")
        print(f"Total Price: ${self.calculate_total()}")
        print(f"Total price after {make_space(self.codes)}: ${self.calculate_total()*self.discount}")
