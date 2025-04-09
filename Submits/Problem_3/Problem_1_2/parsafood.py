from abc import ABC, abstractmethod

class Food(ABC):
    id_counter = 0

    def __init__(self, name):
        self.food_id = Food.id_counter
        Food.id_counter += 1
        self.name = name
        self.price = 0

    @abstractmethod
    def calculate_price(self):
        pass

    def __add__(self, other):
        return self.price + other.price


class Pizza(Food):
    size_prices = {
        "Small": 8,
        "Medium": 12,
        "Large": 16
    }
    pizza_topping_prices = {
        "Extra Cheese": 2,
        "Extra Sauce": 1.5,
        "Olives": 1
    }

    def __init__(self, size, pizzatype, extras):
        super().__init__(pizzatype)
        self.size = size
        self.extras = extras

    def calculate_price(self):
        self.price = Pizza.size_prices[self.size]
        for extra in self.extras:
            self.price += Pizza.pizza_topping_prices.get(extra, 0)
        return self.price


class Burger(Food):
    meat_layer_prices = {
        "Single Layer": 6,
        "Double Layer": 9,
        "Triple Layer": 12
    }
    burger_topping_prices = {
        "Egg": 1.5,
        "Bacon": 2,
        "Cheese": 1
    }

    def __init__(self, meat_layer, bread_type, extras):
        super().__init__("Burger")
        self.meat_layer = meat_layer
        self.bread_type = bread_type
        self.extras = extras

    def calculate_price(self):
        self.price = Burger.meat_layer_prices[self.meat_layer]
        for extra in self.extras:
            self.price += Burger.burger_topping_prices.get(extra, 0)
        return self.price


class Drink(Food):
    drinks_volume = {
        "300ml": 2,
        "500ml": 3,
        "1L": 5
    }

    def __init__(self, volume, drink_type):
        super().__init__(drink_type)
        self.volume = volume

    def calculate_price(self):
        self.price = Drink.drinks_volume.get(self.volume, 0)
        return self.price


class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0.0

    def add_item(self, item, quantity):
        price = item.calculate_price() * quantity
        order_item = {
            "id": len(self.items) + 1,
            "item": item,
            "quantity": quantity,
            "price": price
        }
        self.items.append(order_item)
        self.total_price += price

    def remove_item(self, item_id):
        for order_item in self.items:
            if order_item["id"] == item_id:
                self.total_price -= order_item["price"]
                self.items.remove(order_item)
                return

    def calculate_total(self):
        return self.total_price

    def apply_discount(self, discount_code):
        discount_map = {
            "DISCOUNT10": 0.1,
            "DISCOUNT20": 0.2,
            "DISCOUNT30": 0.3
        }
        discount = discount_map.get(discount_code.upper(), 0)
        if discount > 0:
            discounted_price = self.total_price * (1 - discount)
            return discounted_price
        return self.total_price

    def display_order(self):
        if not self.items:
            print("Order is empty.")
            return
        print("Order Summary:")
        for order_item in self.items:
            item = order_item["item"]
            extras_text = ', '.join(item.extras) if hasattr(item, 'extras') else "No extras"
            print(f"{order_item['quantity']}x {item.name} with extras: {extras_text} (ID: {order_item['id']}) - ${order_item['price']:.2f}")
        print(f"Total Price: ${self.calculate_total():.2f}")


pizza1 = Pizza("Large", "Pepperoni", ["Extra Cheese", "Extra Sauce"])
pizza2 = Pizza("Medium", "Margherita", ["Olives"])
burger1 = Burger("Double Layer", "Sesame", ["Bacon", "Cheese"])
burger2 = Burger("Triple Layer", "Brioche", ["Egg"])
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
print(f"Total price after DISCOUNT10: ${test_order.apply_discount('DISCOUNT10'):.2f}")
print(f"Total price after DISCOUNT20: ${test_order.apply_discount('DISCOUNT20'):.2f}")
print(f"Total price after DISCOUNT30: ${test_order.apply_discount('DISCOUNT30'):.2f}")
