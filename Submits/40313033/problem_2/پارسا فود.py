class Food:
    food_counter = 1

    def __init__(self, name):
        self.food_id = Food.food_counter
        Food.food_counter += 1
        self.name = name


class Drink(Food):
    prices = {"300ml": 2, "500ml": 3, "1L": 5}

    def __init__(self, size, drink_type):
        super().__init__(f"{size} {drink_type}")
        self.size = size
        self.drink_type = drink_type

    def calculate_price(self):
        return self.prices[self.size]


class Pizza(Food):
    prices = {"Small": 8, "Medium": 12, "Large": 16}
    extras_prices = {"Extra Cheese": 2, "Extra Sauce": 1.5, "Olives": 1}

    def __init__(self, size, kind, extras=[]):
        super().__init__(f"{size} {kind} Pizza")
        self.size = size
        self.kind = kind
        self.extras = extras

    def calculate_price(self):
        price = self.prices[self.size]
        for extra in self.extras:
            price += self.extras_prices.get(extra, 0)
        return price


class Burger(Food):
    prices = {"Single": 6, "Double": 9, "Triple": 12}
    extras_prices = {"Cheese": 1, "Bacon": 2, "Egg": 1.5}

    def __init__(self, layers, bun, extras=[]):
        super().__init__(f"{layers} Burger with {bun} Bun")
        self.layers = layers
        self.bun = bun
        self.extras = extras

    def calculate_price(self):
        price = self.prices[self.layers]
        for extra in self.extras:
            price += self.extras_prices.get(extra, 0)
        return price


class Order:
    discount_codes = {"DISCOUNT10": 0.10}

    def __init__(self):
        self.items = {}

    def add_item(self, food, quantity):
        self.items[food.food_id] = (food, quantity)

    def remove_item(self, food_id):
        self.items.pop(food_id, None)

    def calculate_total(self):
        return sum(food.calculate_price() * i for food, i in self.items.values())

    def apply_discount(self, code):
        discount = self.discount_codes.get(code, 0)
        return round(self.calculate_total() * (1 - discount), 2)

    def display_order(self):
        print("Order Summary:")
        for food, i in self.items.values():
            print(
                f"{i}x {food.name} (ID: {food.food_id}) - ${food.calculate_price()} each")
        print(f"Total Price: ${self.calculate_total()}")


order = Order()

while True:
    try:
        command = input().strip()
        if not command:
            break

        parts = command.split(" ", 1)
        action = parts[0]

        if action == "ADD":
            details = parts[1].split('" "')
            food_type = details[0].replace('"', '')

            if food_type == "Pizza":
                size, kind = details[1], details[2]
                extras = details[3:-1] if len(details) > 4 else []
                quantity = int(details[-1].replace('"', ''))
                food = Pizza(size, kind, extras)

            elif food_type == "Burger":
                layers, bun = details[1], details[2]
                extras = details[3:-1] if len(details) > 4 else []
                quantity = int(details[-1].replace('"', ''))
                food = Burger(layers, bun, extras)

            elif food_type == "Drink":
                size, drink_type = details[1], details[2]
                quantity = int(details[3].replace('"', ''))
                food = Drink(size, drink_type)

            else:
                print("Invalid food type! try again")
                continue

            order.add_item(food, quantity)

        elif action == "REMOVE":
            food_id = int(parts[1])
            order.remove_item(food_id)

        elif action == "SHOW":
            order.display_order()

        elif action == "DISCOUNT":
            code = parts[1].strip()
            print(f"Total price after {code}: ${order.apply_discount(code)}")

    except EOFError:
        break
