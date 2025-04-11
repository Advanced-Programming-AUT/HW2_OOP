import abc
class Food(metaclass=abc.ABCMeta):
    id_counter=1
    def __init__(self, name):
        self.name = name
        self.food_id = Food.id_counter
        Food.id_counter += 1
    @abc.abstractmethod
    def calculate_price(self):
        pass
    def __add__(self, other):
        return self.calculate_price() + other.calculate_price()
    def __mul__(self, number):
        return self.calculate_price() * number
class Pizza(Food):
    prices = {
        "Small" : 8,
        "Medium" : 12,
        "Large" : 16
    }
    extras_prices = {
        "Cheese" : 2,
        "Extra Sauce" : 1.5,
        "Olives" : 1
    }
    def __init__(self, size, pizza, extra=None):
        super().__init__(f"{size} {pizza} Pizza")
        self.size = size
        self.pizza = pizza
        self.extra = extra
    def calculate_price(self):
        price = self.prices[self.size]
        if self.extra:
            for extra in self.extra:
                price += self.extras_prices[extra]
        return price
class Burger(Food):
    prices = {
        "Single" : 6,
        "Double" : 9,
        "Triple" : 12
    }
    extras_prices = {
        "Cheese" : 1,
        "Bacon" : 2,
        "Egg" : 1.5
    }
    def __init__(self, layers, bread, extra=None):
        super().__init__(f"{layers} Burger with {bread} Bun")
        self.layers = layers
        self.bread = bread
        self.extra = extra
    def calculate_price(self):
        price = self.prices[self.layers]
        if self.extra:
            for extra in self.extra:
                price += self.extras_prices[extra]
        return price

class Drink(Food):
    prices = {
        "300ml" : 2,
        "500ml" : 3,
        "1L" : 5
    }
    def __init__(self, size, drink):
        super().__init__(f"{size} {drink}")
        self.size = size
        self.drink = drink
    def calculate_price(self):
        return self.prices[self.size]
class Order:
    discount_code = {
        "DISCOUNT10" : 0.1,
        "DISCOUNT20" : 0.2,
        "DISCOUNT30": 0.3,
    }
    def __init__(self):
        self.foods = {}
    def add_item(self, food, quantity):
        self.foods[food.food_id] = {
            "food" : food,
            "quantity" : quantity
        }
    def remove_item(self, food_id):
        if food_id in self.foods:
            del self.foods[food_id]
    def calculate_total(self):
        total_price = 0
        for food_data in self.foods.values():
            total_price += food_data["food"].calculate_price() * food_data["quantity"]
        return total_price
    def apply_discount(self, code):
        discount = self.discount_code.get(code, 0)
        return self.calculate_total() * (1-discount)
    def display_order(self):
        print("Order Summary:")
        for foods in self.foods.values():
            food = foods["food"]
            print(f'{foods["quantity"]}x {food.name} (ID: {food.food_id}) - ${food.calculate_price()} each')
        print(f"Total Price: ${self.calculate_total()}")

def main():
    pizza1 = Pizza("Large", ["Cheese", "Extra Sauce"])
    pizza2 = Pizza("Medium", ["Olives"])
    burger1 = Burger("Double", ["Bacon", "Cheese"])
    burger2 = Burger("Triple", ["Egg"])
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
if __name__ == "__main__":
    main()
