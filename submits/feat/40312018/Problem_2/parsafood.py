from abc import ABC, abstractmethod

class Food(ABC):
    id_counter = 1

    def __init__(self, name):
        self.id = Food.id_counter
        Food.id_counter += 1
        self.name = name

    @abstractmethod
    def calculate_price(self):
        pass

    def __add__(self, other):
        if isinstance(other, Food):
            return self.calculate_price() + other.calculate_price()
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return self.calculate_price() * other
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)


class Pizza(Food):
    size_base = {"Small": 8, "Medium": 12, "Large": 16}
    extras_price = {"Cheese": 2, "Extra Sauce": 1.5, "Olives": 1}

    def __init__(self, size, extras=None):
        name = f"{size} Pizza"
        super().__init__(name)
        self.size = size
        self.extras = extras if extras is not None else []

    def calculate_price(self):
        base = Pizza.size_base.get(self.size, 0)
        extras_cost = sum(Pizza.extras_price.get(extra, 0) for extra in self.extras)
        return base + extras_cost

    def __str__(self):
        extras_str = ", ".join(self.extras) if self.extras else "No extras"
        return f"{self.name} with extras: {extras_str} (ID: {self.id}) - ${self.calculate_price():.2f} each"


class Burger(Food):
    layers_base = {"Single": 10, "Double": 12, "Triple": 13.5}

    def __init__(self, layers, extras=None):
        name = f"{layers} Burger"
        super().__init__(name)
        self.layers = layers
        self.extras = extras if extras is not None else []

    def calculate_price(self):
        base = Burger.layers_base.get(self.layers, 0)
        return base

    def __str__(self):
        extras_str = ", ".join(self.extras) if self.extras else "No extras"
        return f"{self.name} with extras: {extras_str} (ID: {self.id}) - ${self.calculate_price():.2f} each"


class Drink(Food):
    volume_price = {"300ml": 2, "500ml": 3, "1L": 5}

    def __init__(self, volume, drink_type):
        name = f"{volume} {drink_type}"
        super().__init__(name)
        self.volume = volume
        self.drink_type = drink_type

    def calculate_price(self):
        return Drink.volume_price.get(self.volume, 0)

    def __str__(self):
        return f"{self.name} (ID: {self.id}) - ${self.calculate_price():.2f} each"


class Order:
    def __init__(self):
        self.items = {}
        self.discount_codes = {"DISCOUNT10": 0.10, "DISCOUNT20": 0.20, "DISCOUNT30": 0.30}

    def add_item(self, food, quantity):
        if food.id in self.items:
            self.items[food.id] = (food, self.items[food.id][1] + quantity)
        else:
            self.items[food.id] = (food, quantity)
        print(f"Added {quantity}x {food.name} (ID: {food.id}) to the order.")

    def remove_item(self, food_id):
        if food_id in self.items:
            del self.items[food_id]
            print(f"Item with ID {food_id} removed from order.")
        else:
            print("Item not found in order.")

    def calculate_total(self):
        total = 0
        for food, quantity in self.items.values():
            total += food.calculate_price() * quantity
        return total

    def apply_discount(self, code):
        discount = self.discount_codes.get(code.upper(), 0)
        total = self.calculate_total()
        discounted_total = total * (1 - discount)
        return round(discounted_total, 2)

    def display_order(self):
        print("\nOrder Summary:")
        if not self.items:
            print("No items in order.")
            return
        for food, quantity in self.items.values():
            print(f"{quantity}x {food} ")
        total = self.calculate_total()
        print(f"Total Price: ${total:.2f}")


def food_order_menu():
    pizza1 = Pizza("Large", extras=["Cheese", "Extra Sauce"])
    pizza2 = Pizza("Medium", extras=["Olives"])
    burger1 = Burger("Double", extras=["Bacon", "Cheese"])
    burger2 = Burger("Triple", extras=["Egg"])
    drink1 = Drink("500ml", "Soda")
    drink2 = Drink("1L", "Juice")

    available_foods = {pizza1.id: pizza1, pizza2.id: pizza2,burger1.id: burger1,burger2.id: burger2, drink1.id: drink1, drink2.id: drink2}

    order = Order()

    while True:
        print("\n--- Available Foods ---")
        for food in available_foods.values():
            print(food)
        print("\n--- Options ---")
        print("1. Add item to order")
        print("2. Remove item from order")
        print("3. View order summary")
        print("4. Apply discount code")
        print("5. Finalize Order (Exit)")
        choice = input("Enter your choice: ")

        if choice == "1":
                i = int(input("Enter product ID to add: "))
                j = int(input("Enter quantity: "))
                if i not in available_foods:
                    print("Invalid product ID.")
                    continue
                if j <= 0:
                    print("Quantity must be positive.")
                    continue
                order.add_item(available_foods[i], j)
        elif choice == "2":
                i = int(input("Enter product ID to remove from order: "))
                order.remove_item(i)
        elif choice == "3":
            order.display_order()
        elif choice == "4":
            code = input("Enter discount code: ")
            discounted_total = order.apply_discount(code)
            print(f"Total price after {code.upper()}: ${discounted_total}")
        elif choice == "5":
            print("Finalizing order...")
            order.display_order()
            total = order.calculate_total()
            print(f"Final Total Price: ${total:.2f}")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Welcome to Parasa Food Ordering System!")
    food_order_menu()
