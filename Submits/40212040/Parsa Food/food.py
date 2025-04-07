from abc import ABC, abstractmethod

class Food(ABC):

    def __init__(self,name):
        self.name = name
    @abstractmethod
    def calculate_price(self):
        return 0
    @abstractmethod
    def print_this_item_as_order(self,order):
        pass

all_menu=[]
class Pizza(Food):

    food_type = 'pizza'
    def __init__(self,name,s,extras:list):
        super().__init__(name)
        self.size = s
        self.extras= extras
        self.idd = len(all_menu) + 1
        all_menu.append(self)
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,s):
        if s not in ['Small','Medium','Large']:
            print('invalid string is given as size')
        else:
            self._size = s
    def calculate_price(self):
        overall=0
        match self.size:
            case 'Small':
                overall += 8
            case 'Medium':
                overall += 12
            case 'Large':
                overall += 16
        if 'Cheese' in self.extras:
            overall += 2
        if 'Extra Sauce' in self.extras:
            overall += 1.5
        if 'Olives' in self.extras:
            overall += 1
        return overall
    def __add__(self,other):
        if isinstance(other,Food):
            return self.calculate_price() + other.calculate_price()
    def __mul__(self, integer):
        if isinstance(integer,int):
            return self.calculate_price() * integer

    def print_this_item_as_order(self,order):
        print(f'{order.orders[self]}x {self.size} {self.food_type}',end=' ')
        for it in self.extras:
            print(f'{it}',end=',')
        print(f'{self.idd}', end=' ')
        print(f'-${self.calculate_price()} each')

class Burger(Food):
    food_type = 'burger'
    def __init__(self, name, layer,extras:list,bread='Regular'):
        super().__init__(name)
        self.layers = layer
        self.bread_type = bread
        self.idd = len(all_menu) + 1
        self.extras = extras
        all_menu.append(self)
    @property
    def layers(self):
        return self._layers
    @layers.setter
    def layers(self,layer):
        if layer not in ['Single','Double','Triple']:
            print('invalid number of layers')
        else:
            self._layers=layer

    @property
    def bread_type(self):
        return self._bread_type

    @bread_type.setter
    def bread_type(self, bread):
        if bread not in ['Brioche', 'Sesame', 'Regular']:
            print('invalid number of layers')
        else:
            self._bread_type = bread

    def calculate_price(self):
        overall=0
        match self.layers:
            case 'Single':
                overall += 6
            case 'Double':
                overall += 9
            case 'Triple':
                overall += 12
        if 'Egg' in self.extras:
                overall += 1.5
        if 'Bacon' in self.extras:
                overall += 2
        if 'Cheese' in self.extras:
                overall += 1
        return overall

    def __add__(self, other):
        if isinstance(other, Food):
            return self.calculate_price() + other.calculate_price()
    def __mul__(self, integer):
        if isinstance(integer, int):
            return self.calculate_price() * integer
    def print_this_item_as_order(self,order):
        print(f'{order.orders[self]}x {self.layers} {self.food_type} with {self.bread_type} bread ', end=' ')
        for it in self.extras:
            print(f'{it}', end=', ')
        print(f'ID:{self.idd}', end=' ')
        print(f'${self.calculate_price()} each')

class Drink(Food):
    food_type ='drink'
    def __init__(self, name,volume,kind):
        super().__init__(name)
        self.volume=volume
        self.kind=kind
        self.idd = len(all_menu) + 1
        all_menu.append(self)
    def calculate_price(self):
        overall=0
        match self.volume:
            case '300ml':
                overall += 2
            case '500ml':
                overall += 3
            case '1L':
                overall += 5
        return overall
    def __add__(self, other):
        if isinstance(other,Food):
            return self.calculate_price() + other.calculate_price()
    def __mul__(self, integer):
        if isinstance(integer,int):
            return self.calculate_price() * integer

    def print_this_item_as_order(self,order):
        print(f'{order.orders[self]}x {self.volume} {self.food_type}', end=' ')
        print(f'{self.idd}', end=' ')
        print(f'-${self.calculate_price()} each')

Discounts = {'DISCOUNT10': 0.1, 'DISCOUNT20': 0.2, 'DISCOUNT30': 0.3, 'DISCOUNT40': 0.4, 'DISCOUNT50': 0.5,
                 'DISCOUNT60': 0.6, 'DISCOUNT70': 0.7, 'DISCOUNT80': 0.8, 'DISCOUNT90': 0.9}
class Order:
    def __init__(self):
        self.orders=dict()
        self.price = 0
    def add_item(self,food:Food,number):
        self.orders.setdefault(food,int(number))
        print (f'{food.name} is added to order list')
    def remove_item(self,food_id):
        for item in self.orders.keys():
            if item.idd == food_id:
                self.orders.pop(item)

    def apply_discount(self,code):
        x=self.calculate_total()
        z=self.price * Discounts[code]
        self.price= x - z
        return self.price

    def calculate_total(self):
        self.price=0
        for item in self.orders.keys():
            y = item.calculate_price()
            self.price += y * self.orders[item]
        return self.price
    def display_order(self):
        for item in self.orders.keys():
            item.print_this_item_as_order(self)
        self.calculate_total()
        print(f'total price: {self.price}')


pizza1 = Pizza('pizza1',"Large", extras=["Cheese" , "Extra Sauce"])
pizza2 = Pizza('pizza2',"Medium", extras=["Olives"])
burger1 = Burger('burger1',"Double", extras=["Bacon", "Cheese"])
burger2 = Burger('burger2',"Triple", extras=["Egg"])
drink1 = Drink('drink1',"500ml", "Soda")
drink2 = Drink('drink2',"1L", "Juice")
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
