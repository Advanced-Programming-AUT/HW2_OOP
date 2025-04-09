import sys, os
from abc import ABC, abstractmethod

original_stdout = sys.stdout

os.remove('output.txt')

file1 = open('input.txt', 'r')
file2 = open('output.txt', 'a')

sys.stdout = file2

# ---------- Main Code ----------

class Food(ABC):
    it = 0
    def __init__(self, name):
        Food.it += 1
        self._food_id = Food.it
        self._name = name

    @property
    def food_id(self):
        return self._food_id

    @property
    def name(self):
        return self._name

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __float__(self):
        return self.calculate_price()

    def __add__(self, other):
        return float(self) + float(other)

    def __mul__(self, other):
        return float(self) * float(other)

class Pizza(Food):
    Size = {'Small': 8,
            'Medium': 12,
            'Large': 16}
    Extras = {'Cheese': 2,
              'Extra Sauce': 1.5,
              'Olives': 1}

    def __init__(self, size, flavour, extras):
        '''
        size: one of ['Small', 'Medium', 'Large']
        flavour: one of ['Pepperoni', 'Margherita']
        extras: some of ['Cheese', 'Extra Sauce', 'Olives']
        '''

        super().__init__('Pizza')
        self._size = size
        self._flavour = flavour
        self._extras = extras

    def calculate_price(self):
        price = Pizza.Size[self._size]
        for extra in self._extras:
            price += Pizza.Extras[extra]
        return float(price)

    def __str__(self):
        return f'{self._size} {self._flavour} Pizza (ID: {self.food_id}) - ${float(self)} each'

class Burger(Food):
    Layer = {'Single': 6,
             'Double': 9,
             'Triple': 12}
    Extras = {'Cheese': 1,
              'Bacon': 2,
              'Egg': 1.5}

    def __init__(self, layer, flavour, extras):
        '''
        layer: one of ['Single', 'Double', 'Triple']
        flavour: one of ['Regular', 'Sesame', 'Brioche']
        extras: some of ['Cheese', 'Egg', 'Bacon']
        '''

        super().__init__('Burger')
        self._layer = layer
        self._flavour = flavour
        self._extras = extras

    def calculate_price(self):
        price = Burger.Layer[self._layer]
        for extra in self._extras:
            price += Burger.Extras[extra]
        return float(price)

    def __str__(self):
        return f'{self._layer} Burger with {self._flavour} Bun (ID: {self.food_id}) - ${float(self)} each'

class Drink(Food):
    Volume = {'300ml': 2,
              '500ml': 3,
              '1L': 5}

    def __init__(self, volume, flavour):
        '''
        volume: one of ['300ml', '500ml', '1L']
        flavour: one of ['Water', 'Soda', 'Juice']
        '''

        super().__init__('Drink')
        self._volume = volume
        self._flavour = flavour

    def calculate_price(self):
        return float(Drink.Volume[self._volume])

    def __str__(self):
        return f'{self._volume} {self._flavour} (ID: {self.food_id}) - ${float(self)} each'

class Order:
    def __init__(self):
        self.__orders = dict()

    def add_item(self, food, quantity):
        if food in self.__orders:
            self.__orders[food] += quantity
        else:
            self.__orders[food] = quantity

    def remove_item(self, food_id):
        for food in self.__orders:
            if food.food_id == food_id and self.__orders[food] > 0:
                self.__orders[food] -= 1
                break

    def calculate_total(self):
        price = 0
        for food in self.__orders:
            price += self.__orders[food] * food.calculate_price()
        return price

    def apply_discount(self, code):
        percentile = int(code[8:]) / 100
        percentile = 1 - percentile

        price = self.calculate_total() * percentile

        return price

    def display_order(self):
        print('Order Summary:')
        for food in self.__orders:
            print(str(self.__orders[food]) + 'x', str(food))
        print(f'Total Price: ${self.calculate_total()}')

if __name__ == '__main__':
    # Creating different food items
    pizza = Pizza('Large', 'Pepperoni', extras=['Cheese', 'Extra Sauce'])
    burger = Burger('Double', 'Brioche', extras=['Bacon', 'Cheese'])
    drink = Drink('500ml', 'Soda')

    # Creating an order and adding items
    order = Order()
    order.add_item(pizza, 2) # 2 Large Pepperoni Pizzas with Extras
    order.add_item(burger, 1) # 1 Double Burger with Brioche Bun
    order.add_item(drink, 3) # 3 Drinks (500ml each)

    # Displaying order details
    order.display_order()

    # Displaying total price after discount
    print(f'Total price after DISCOUNT10: ${order.apply_discount('DISCOUNT10')}')

# ---------- End of Main Code ----------

sys.stdout = original_stdout

file1.close()
file2.close()
