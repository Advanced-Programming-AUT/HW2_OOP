import abc


class Food(metaclass=abc.ABCMeta):
    def __init__(self, food_id, name):
        self.food_id = food_id
        self.name = name

    def calculate_price(self):
        pass

    def __add__(self, other):
        return self.calculate_price() + other.calculate_price()

    def __mul__(self, count):
        return self.calculate_price() * count


@Food.register
class Pizza:
    def __init__(self, size, extras):
        self.size = size
        self.extras = extras

    def calculate_price(self):
        price = 0
        if self.size == 'Small':
            price = 8
        elif self.size == 'Medium':
            price = 12
        elif self.size == 'Large':
            price = 16
        for extra in self.extras:
            if extra == 'Cheese':
                price += 2
            if extra == 'Extra Sauce':
                price += 1.5
            if extra == 'Olives':
                price += 1
        return price


@Food.register
class Burger:
    def __init__(self, meat_layers, extras):
        self.meat_layers = meat_layers
        self.extras = extras

    def calculate_price(self):
        price = 0
        if self.meat_layers == 'Single':
            price = 6
        elif self.meat_layers == 'Double':
            price = 9
        elif self.meat_layers == 'Triple':
            price = 12
        for extra in self.extras:
            if extra == 'Cheese':
                price += 1
            if extra == 'Bacon':
                price += 2
            if extra == 'Egg':
                price += 1.5
        return price


@Food.register
class Drink:
    def __init__(self, volume, kind):
        self.volume = volume
        self.kind = kind

    def calculate_price(self):
        price = 0
        if self.volume == '300ml':
            price = 2
        if self.volume == '500ml':
            price = 3
        if self.volume == '1L':
            price = 5
        return price


class Order:
    def __init__(self):
        self.orders = dict()
        self.discount_code = {
            'DISCOUNT10': 10,
            'DISCOUNT20': 20,
            'DISCOUNT30': 30
            }

    def add_item(self, item, count):
        if item in self.orders:
            self.orders[item] += count
        else:
            self.orders[item] = count

    def remove_item(self, item, count):
        if item in self.orders:
            self.orders[item] -= count
            if self.orders[item] <= 0:
                del self.orders[item]

    def calculate_total(self):
        totalprice = 0
        for order in self.orders:
            totalprice += self.orders[order] * order.calculate_price()
        return totalprice

    def apply_discount(self, code):
        totalprice = self.calculate_total()
        discount = totalprice * (self.discount_code[code] / 100)
        return totalprice - discount

    def display_order(self):
        print('Order Summary:')
        for item in self.orders:
            print(self.orders[item], end="x ")
            if isinstance(item, Pizza):
                print(f"{item.size} Pizza with ", end="")
                for extra in range(len(item.extras)):
                    print(f"{item.extras[extra]}", end=" ")
                    if extra != len(item.extras) - 1:
                        print(", ", end="")
                print(f"- ${item.calculate_price()} each")
            if isinstance(item, Burger):
                print(f"{item.meat_layers} Burger with ", end="")
                for extra in item.extras:
                    print(f"{extra}", end=" ")
                print(f"- ${item.calculate_price()} each")
            if isinstance(item, Drink):
                print(f"{item.volume} {item.kind}", end="")
                print(f" - ${item.calculate_price()} each")


def main():
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

    print(f"total price : {test_order.calculate_total()}")
    print(f"Total price after DISCOUNT10: ${test_order.apply_discount('DISCOUNT10')}")
    print(f"Total price after DISCOUNT10: ${test_order.apply_discount('DISCOUNT20')}")
    print(f"Total price after DISCOUNT10: ${test_order.apply_discount('DISCOUNT30')}")


main()
