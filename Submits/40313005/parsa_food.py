from abc import ABC, abstractmethod
import random


class Food(ABC):
    food_id = 0
    def __init__(self, name):
            self.name = name
            

    @abstractmethod 
    def calculate_price():
        pass

    def operator(self,quantity):
        return(self.calculate_price() * quantity)

class Pizza(Food):
    food_id = random.randrange(0,100)
    def __init__(self,size,type_,extras:list):
        super().__init__("Pizza") 
        self.size = size 
        self.type_ = type_
        self.extras = extras


    def calculate_price(self):
        price = 0
        match self.size:
            case "Small":
                price += 8
            case "medium":
                price += 12
            case "Large":
                price += 16
        if "Cheese" in self.extras:
            price += 2
        if "Extra Sauce" in self.extras:
            price += 1.5
        if "Olives" in self.extras:
            price += 1
        return price
class Burger(Food):
    food_id = random.randrange(0,100)
    def __init__(self,size,type_,extras:list):
        super().__init__("Burger") 
        self.size = size 
        self.type_ = type_
        self.extras = extras


    def calculate_price(self):
        price = 0
        match self.size:
            case "Single":
                price += 6
            case "Double":
                price += 9
            case "Triple":
                price += 12
        if "Cheese" in self.extras:
            price += 1
        if "Bacon" in self.extras:
            price += 2
        if "Egg" in self.extras:
            price += 1.5
        return price
class Drink(Food):
    food_id = random.randrange(0,100)
    def __init__(self,size,type_):
        super().__init__("Burger") 
        self.size = size 
        self.type_ = type_

    def calculate_price(self):
        price = 0
        match self.size:
            case "300ml":
                price += 2
            case "500ml":
                price += 3
            case "1L":
                price += 5
        return price



class Order:
    def __init__(self):
        self.food_list = {}

    def add_item(self,food,quantity):
        self.food_list[food]=quantity

    def remove_item(self,food_id):
        for food in self.food_list:
            if food.food_id == food_id:
                self.food_list.pop(food)

    def calculate_total(self):
        total = 0
        for food in self.food_list:
            total += food.operator(self.food_list[food])
        return total
    def apply_discount(self,code):
        codes={"DISCOUNT10":0.1}
        print(f"Total price after {code}:{self.calculate_total()*(1-codes[code])}")

    def display_order(self):
        print("Order Summary:")
        for food in self.food_list: 
            print(f"{self.food_list[food]}x {food.size} {food.type_} (ID: {food.food_id}) - ${food.calculate_price()} each")
        print(f"Total Price:{self.calculate_total()}")





# Creating different food items
pizza = Pizza("Large", "Pepperoni", extras=["Cheese", "Extra Sauce"])
burger = Burger("Double", "Brioche", extras=["Bacon", "Cheese"])
drink = Drink("500ml", "Soda")
# Creating an order and adding items
order = Order()
order.add_item(pizza, 2) # 2 Large Pepperoni Pizzas with extras
order.add_item(burger, 1) # 1 Double Burger with Brioche bun
order.add_item(drink, 3) # 3 Drinks (500ml each)
# Displaying order details
order.display_order()
# Displaying total price after discount
order.apply_discount('DISCOUNT10')