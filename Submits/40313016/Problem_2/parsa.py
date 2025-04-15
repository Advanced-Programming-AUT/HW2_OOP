from abc import ABC, abstractmethod, abstractclassmethod
class Food(ABC):
    @property
    @abstractmethod
    def food_id(self):
        pass
    @property
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def __add__(self, other):
        pass
    @abstractmethod
    def __mul__(self, other):
        pass
    @abstractclassmethod
    def calculated_price(self):
        pass  
class Pizza(Food):
    def __init__(self, size, type, name, *extras):
        self.size = size
        self.type = type
        self._name = name
        self.list_all_extras = list(extras)
        self.quantity = 0
        self.dict_price = {"small": 8, "medium": 12, "large": 16, "Extra Cheese": 2, "Extra Sauce": 1.5, "Olive": 1}
    @property
    def food_id(self):
        return self._food_id
    @property
    def name(self):
        return self._name
    def __add__(self, other):
        if isinstance(other, Food):
            return self.quantity * self.calculated_price() + other.quantity * other.calculated_price()
        else:
            return self.quantity * self.calculated_price() + other
    def __mul__(self, quantity):
        return self.calculated_price() * int(quantity)
    def calculated_price(self):
        self.sum_of_prices = 0
        self.sum_of_prices += self.dict_price[self.size]
        for extra_order in self.list_all_extras:
            self.sum_of_prices += self.dict_price[extra_order]
        return self.sum_of_prices
    
class Burger(Food):
    def __init__(self, layers, type_of_braed, name, *extras):
        self.layers = layers
        self.type_of_braed = type_of_braed
        self._name = name
        self.list_all_extras = list(extras)
        self.dict_price = {"Single Layer": 6, "Double Layer": 9, "Triple Layer": 12, "Cheese": 1, "Bacon": 2, "Egg": 1.5}
    @property
    def food_id(self):
        return self._food_id
    @property
    def name(self):
        return self._name   
    def __add__(self, other):
        if isinstance(other, Food):
            return self.quantity * self.calculated_price() + other.quantity * other.calculated_price()
        else:
            return self.quantity * self.calculated_price() + other
    def __mul__(self, quantity):
        return self.calculated_price() * int(quantity) 
    def calculated_price(self):
       self.sum_of_prices = 0
       self.sum_of_prices += self.dict_price[self.layers]
       for extra_order in self.list_all_extras:
           self.sum_of_prices += self.dict_price[extra_order]
       return self.sum_of_prices
   
class Drink(Food):
    def __init__(self, v_of_drink, type_of_drink, name):
        self.v_of_drink = v_of_drink
        self.type_of_drink = type_of_drink
        self._name = name
        self.dict_price = {"300ml": 2, "500ml": 3, "1L": 5}
    @property
    def food_id(self):
        return self._food_id
    @property
    def name(self):
        return self._name   
    def __add__(self, other):
        if isinstance(other, Food):
            return self.quantity * self.calculated_price() + other.quantity * other.calculated_price()
        else:
            return self.quantity * self.calculated_price() + other
    def __mul__(self, quantity):
        return self.calculated_price() * int(quantity)    
    def calculated_price(self):
       self.sum_of_prices = 0
       self.sum_of_prices += self.dict_price[self.v_of_drink]
       return self.sum_of_prices
   
class Order:
    food_id = 0
    code_of_discounts = {"123456": 0.9, "DISCOUNT": 0.8, "246810": 0.6}
    def __init__(self, name):
        self.name= name
        self.dict_all_order = {}
        self.total_price = 0 
    def add_item(self, food, quantity):
        Order.food_id += 1
        food._food_id = Order.food_id
        self.dict_all_order[food] = quantity
    def remove_item(self, food_id):
        for food in self.dict_all_order.keys():
            if food.food_id == food_id:
                self.dict_all_order.pop(food)
                print(f"The food with ID: {food.food_id} Deleted")
                break
    def calculated_total(self):
        for food in self.dict_all_order.keys():
            self.total_price += food * int(self.dict_all_order[food]) 
    def apply_discount(self, code):
        if code not in Order.code_of_discounts:
            print("Your code is wrong!")
        else:
            self.code = code
            discount = Order.code_of_discounts[code]
            self.price_after_discount = discount * self.total_price
    def display_order(self):
        print(f"order {self.name}:")
        for food in self.dict_all_order.keys():
            if isinstance(food, Pizza): 
                quantity = self.dict_all_order[food]
                print(f"- {quantity}x {food.size} {food.type} Pizza (ID: {food.food_id}) - ${food.sum_of_prices} each")
            if isinstance(food, Burger):
                quantity = self.dict_all_order[food]
                print(f"- {quantity}x {food.layers} Burger with {food.type_of_braed} (ID: {food.food_id}) - ${food.sum_of_prices} each")
            if isinstance(food, Drink):
                quantity = self.dict_all_order[food]
                print(f"- {quantity}x {food.v_of_drink} {food.type_of_drink} (ID: {food.food_id}) - ${food.sum_of_prices} each")
        print(f"Total Price: ${self.total_price}")
        try:
            print(f"Total price after {self.code}: ${order.price_after_discount}")
        except:
            print("Not Discount!")
            
order = Order("MOHAMMADIAN")

food = Drink("500ml", "soda", "A")
food5 = Drink("300ml", "ZAM ZAM", "name")
food1 = Pizza("small", "pepperoni", "A", "Olive")
food2 = Pizza("medium", "pepperoni", "A", "Olive")
food3 = Burger("Double Layer", "Brioche", "A", "Cheese")

order.add_item(food, 10)
order.add_item(food1, 4)
order.add_item(food2, 4)
order.add_item(food3, 4)
order.add_item(food5, 2)

order.remove_item(4)

order.calculated_total()

order.apply_discount("123456")

order.display_order()