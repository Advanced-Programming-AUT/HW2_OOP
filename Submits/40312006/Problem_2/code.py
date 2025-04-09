from abc import ABCMeta, abstractmethod

class Food(metaclass=ABCMeta):
    static_id = 0

    def __init__(self, name: str) -> None:
        Food.static_id += 1
        self.food_id = Food.static_id
        self.name = name

    def __add__(self, other) -> float:
        if isinstance(other, Food):
            return self.calculate_price() + other.calculate_price()
        return self.calculate_price() + other

    def __mul__(self, other) -> float:
        return self.calculate_price() * other

    @abstractmethod
    def calculate_price(self) -> float:
        pass

class Pizza(Food):
    def __init__(self, size: str, ptype: str, extras: list[str]) -> None:
        super().__init__("Pizza")
        self.size = size
        self.ptype = ptype
        self.extras = extras

    def calculate_price(self) -> float:
        match self.size:
            case "Small":
                price = 8.0
            case "Medium":
                price = 12.0
            case "Large":
                price = 16.0
            case _:
                raise ValueError

        if "Cheese" in self.extras:
            price += 2.0
        if "Extra Sauce" in self.extras:
            price += 1.5
        if "Olives" in self.extras:
            price += 1.0
        return price

    def __repr__(self) -> str:
        return f"{self.size} {self.ptype} {self.name} (ID: {self.food_id}) - ${self.calculate_price()} each"

class Burger(Food):
    def __init__(self, layer: str, btype: str, extras: list[str]) -> None:
        super().__init__("Burger")
        self.layer = layer
        self.btype = btype
        self.extras = extras

    def calculate_price(self) -> float:
        match self.layer:
            case "Single":
                price = 6.0
            case "Double":
                price = 9.0
            case "Triple":
                price = 12.0
            case _:
                raise ValueError

        if "Cheese" in self.extras:
            price += 1.0
        if "Bacon" in self.extras:
            price += 2.0
        if "Egg" in self.extras:
            price += 1.5
        return price

    def __repr__(self) -> str:
        return f"{self.layer} {self.name} with {self.btype} Bun (ID: {self.food_id}) - ${self.calculate_price()} each"

class Drink(Food):
    def __init__(self, volume: str, dtype: str) -> None:
        super().__init__("Drink")
        self.volume = volume
        self.dtype = dtype

    def calculate_price(self) -> float:
        match self.volume:
            case "300ml":
                return 2.0
            case "500ml":
                return 3.0
            case "1L":
                return 5.0
            case _:
                raise ValueError

    def __repr__(self) -> str:
        return f"{self.volume} {self.dtype} (ID: {self.food_id}) - ${self.calculate_price()} each"

class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, food: Food, quantity: int) -> None:
        self.items[food.food_id] = (food, quantity)

    def remove_item(self, food_id: int) -> None:
        try:
            self.items.pop(food_id)
        except KeyError:
            print(f"Food with id {food_id} not found")

    def calculate_total(self) -> float:
        price = 0.0
        for food, quantity in self.items.values():
            price += food * quantity
        return price

    def apply_discount(self, code: str) -> float:
        discount = discounts.get(code)

        if discount == None:
            return self.calculate_total()
        return self.calculate_total() * (1 - discount / 100)

    def display_order(self) -> None:
        print("Order Summery:")
        for food, quantity in self.items.values():
            print(f"{quantity}x {food}")
        print(f"Total Price: {self.calculate_total()}")

discounts = {"DISCOUNT10": 10}

pizza = Pizza("Large", "Pepperoni", extras=["Cheese", "Extra Sauce"])
burger = Burger("Double", "Brioche", extras=["Bacon", "Cheese"])
drink = Drink("500ml", "Soda")

order = Order()
order.add_item(pizza, 2)
order.add_item(burger, 1)
order.add_item(drink, 3)

order.display_order()

print(f"Total price after DISCOUNT10: ${order.apply_discount('DISCOUNT10')}")
