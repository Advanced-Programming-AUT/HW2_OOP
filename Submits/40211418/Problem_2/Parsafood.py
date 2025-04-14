from abc import ABC, abstractmethod


class Food(ABC):
    food_id = 1

    @abstractmethod
    def __init__(self):
        self.id = Food.food_id
        Food.food_id += 1

    @abstractmethod
    def calculate_price(self):
        ...

    @abstractmethod
    def __add__(self, other):
        ...
    
    @abstractmethod
    def __mul__(self, other):
        ...


class Pizza(Food):
    price_dict = {'Small': 8, 'Medium': 12, 'Large': 16}
    extra_prices_dict = {'Cheese': 2, 'Extra Sauce': 1.5, 'Olives': 1}

    def __init__(self, size, kind, extras):
        super().__init__()
        self.size = size
        self.kind = kind
        self.extras = extras

    def calculate_price(self):
        base_price = Pizza.price_dict.get(self.size, 0)
        additional_price = sum(Pizza.extra_prices_dict.get(extra, 0) for extra in self.extras)
        return base_price + additional_price

    def __add__(self, other):
        if isinstance(other, Food):
            return self.calculate_price() + other.calculate_price()
        raise TypeError

    def __mul__(self, num: int):
        return self.calculate_price() * num


class Burger(Food):
    price_dict = {'Single': 6, 'Double': 9, 'Triple': 12}
    extra_prices_dict = {'Cheese': 1, 'Bacon': 2, 'Egg': 1.5}

    def __init__(self, layer, bread, extras):
        super().__init__()
        self.layer = layer
        self.bread = bread
        self.extras = extras

    def calculate_price(self):
        base_price = Burger.price_dict.get(self.layer, 0)
        additional_price = sum(Burger.extra_prices_dict.get(extra, 0) for extra in self.extras)
        return base_price + additional_price

    def __add__(self, other):
        if isinstance(other, Food):
            return self.calculate_price() + other.calculate_price()
        raise TypeError

    def __mul__(self, num: int):
        return self.calculate_price() * num


class Drink(Food):
    price_dict = {'300ml': 2, '500ml': 3, '1L': 5}

    def __init__(self, volume, kind):
        super().__init__()
        self.kind = kind
        self.volume = volume

    def calculate_price(self):
        return Drink.price_dict.get(self.volume, 0)

    def __add__(self, other):
        if isinstance(other, Food):
            return self.calculate_price() + other.calculate_price()
        raise TypeError

    def __mul__(self, num: int):
        return self.calculate_price() * num


class Order:
    discounts_dict = {'DISCOUNT10': 10, 'DISCOUNT20': 20}

    def __init__(self):
        self.foods = {}
        self.total_price = 0

    def add_item(self, food, quantity):
        self.foods[food] = quantity

    def remove_item(self, food_id):
        for food in self.foods.keys():
            if food.id == food_id:
                self.foods.pop(food)
                break

    def calculate_total(self):
        self.total_price = sum(food * quantity for food, quantity in self.foods.items())
        return self.total_price

    def apply_discount(self, code):
        discount_percent = Order.discounts_dict.get(code, 0)
        return self.total_price - self.total_price * discount_percent / 100

    def display_order(self):
        print('Order summary:')
        for food, quantity in self.foods.items():
            if isinstance(food, Pizza):
                extras = ' and '.join(food.extras)
                print(f'{quantity}x {food.size} {food.kind} pizza with {extras} '
                      f'(ID: {food.id}) - ${food.calculate_price()} each')
            elif isinstance(food, Burger):
                extras = ' and '.join(food.extras)
                print(f'{quantity}x {food.layer} Burger with {food.bread} and {extras} '
                      f'(ID: {food.id}) - ${food.calculate_price()} each')
            elif isinstance(food, Drink):
                print(f'{quantity}x {food.volume} {food.kind} (ID: {food.id}) - '
                      f'${food.calculate_price()} each')

        print(f'Total Price: ${self.calculate_total()}')


if __name__ == '__main__':
    pizza = Pizza("Large", "Pepperoni", extras=["Cheese", "Extra Sauce"])
    burger = Burger("Double", "Brioche", extras=["Bacon", "Cheese"])
    drink = Drink("500ml", "Soda")
    order = Order()
    order.add_item(pizza, 2) # 2 Large Pepperoni Pizzas with extras
    order.add_item(burger, 1) # 1 Double Burger with Brioche
    order.add_item(drink, 3)
    order.display_order()
    print(f"Total price after DISCOUNT10: ${order.apply_discount('DISCOUNT10')}")