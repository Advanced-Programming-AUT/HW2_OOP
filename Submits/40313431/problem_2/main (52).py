from abc import ABC, abstractmethod


class Food(ABC):
    id = 1

    def __init__(self, price=0):
        self.food_id = Food.id
        self.price = price
        Food.id += 1

    @abstractmethod
    def calculate_price(self):
        pass

    # def __add__(self, other):
    # retrun float(self.price) + float(other.price)


class Pizza(Food):
    all_pizzas = list()

    def __init__(self, size, kind, extra):
        super().__init__()
        self.name = 'pizza'
        self.size = size
        self.kind = kind
        self.extra = extra
        Pizza.all_pizzas.append(self)

    def calculate_price(self):
        price = 0
        if self.size == 'Small':
            price += 8
        elif self.size == 'Medium':
            price += 12
        elif self.size == 'Large':
            price += 16
        if 'Cheese' in self.extra:
            price += 2
        if 'Sauce' in self.extra:
            price += 1.5
        if 'Olives' in self.extra:
            price += 1
        return price


class Burger(Food):
    def __init__(self, number, kind, extra):
        super().__init__()
        self.name = 'burger'
        self.number = number
        self.kind = kind
        self.extra = extra

    def calculate_price(self):
        price = 0
        if self.number == 'Single':
            price += 6
        elif self.number == 'Double':
            price += 9
        elif self.number == 'Triple':
            price += 12
        if 'Cheese' in self.extra:
            price += 1
        if 'Bacon' in self.extra:
            price += 2
        if 'Egg' in self.extra:
            price += 1.5
        return price


class Drink(Food):
    def __init__(self, volume, kind):
        super().__init__()
        self.name = 'drink'
        self.volume = volume
        self.kind = kind

    def calculate_price(self):
        price = 0
        if self.volume == '300ml':
            price += 2
        if self.volume == '500ml':
            price += 3
        if self.volume == '1L':
            price += 5
        return price


class Order(Food):
    def __init__(self):
        super().__init__()
        self.items = {}  

    def add_item(self, food, quantity):
        self.items[food] = quantity

    def calculate_total(self):
        total_price = 0
        for food, quantity in self.items.items():
            total_price += food.calculate_price() * quantity
        return total_price

    def discount(self, discount):
        total_price = self.calculate_total()
        discounted_price = total_price * ((100 - discount) / 100)
        return f"Total price after DISCOUNT {discount}: {discounted_price:.2f}$"

    def display_order(self):
        result = ""
        total_price = 0

        for food, quantity in self.items.items():
            if food.name == 'pizza':
                result += f'{quantity}x {food.size} {food.kind} {food.name} (ID: {food.food_id}) - {food.calculate_price()}$\n'
            elif food.name == 'burger':
                result += f'{quantity}x {food.number} {food.name} with {food.extra} (ID: {food.food_id}) - {food.calculate_price()}$\n'
            elif food.name == 'drink':
                result += f'{quantity}x {food.volume} {food.kind} (ID: {food.food_id}) - {food.calculate_price()}$\n'
            total_price += food.calculate_price() * quantity

        result += f"Total price: {total_price}$\n"
        return result

    def calculate_price(self):
        pass


pizza = Pizza("Large", "Pepproni", extra=["Cheese", "Sauce"])

burger = Burger("Double", "Brioche", extra=['Bacon', 'Cheese'])
drink = Drink("500ml", "Soda")
order = Order()
order.add_item(pizza, 2)
order.add_item(burger,1)
order.add_item(drink,3)
print(order.display_order())
print(order.discount(10))
