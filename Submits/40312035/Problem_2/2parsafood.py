class Food:
    foodID = 100 #مثلا
    def __init__(self , name):
        self.name = name
        self.fID = Food.foodID ; Food.foodId += 10
        self.price =0

    def calculate_price(self):
        return self.price
    def __add__(self , second):
        return self.calculate_price() + second.calculate_prince()
    def __mul__(self , num):
        return self.calculate_price() * num
    
class Pizza(Food):
    sizes = {
        'small':8,'medium':12,'large':16
    }
    extra = {
        'cheese':2,'sauce':1.5,'olive':1
    }
    def __init__(self , name , size , type , extra):
        super().__init__(name)
        self.size = size ; self.type = type ; self.extra = extra
    def calculate_price(self):
        price = self.sizes[self.size]
        for i in self.extra:
            price += self.extra[i]
        return price

class Burger(Food):
    buns = ['brioche' , 'sesame' , 'regular']
    patty = {
        'single':6,'double':9,'triple':12
    }
    extra = {
        'egg':1.5,'cheese':1,'bacon':1
    }
    def __init__(self, name , patty , extra , bun):
        super().__init__(name)
        self.patty = patty ; self.extra = extra ; self.bun = bun

    def calculate_price(self):
        price = Burger.sizes[self.patty]
        for i in self.extra:
            price += Burger.extra[i]
        return price
    
class Drink(Food):
    hajm = {
        '300ml':2,'500ml':3,'1L':5
    }
    def __init__(self, name , hajm , type):
        super().__init__(name)
        self.type = type ; self.hajm = hajm
    
    def calculate_price(self):
        return Drink.hajm[self.hajm]

class Order:
    discount = {
        'DISCOUNT10':10,'DISCOUNT20':20,'DISCOUNT30':30
    }
    def __init__(self):
        self.things = {}
    def add_item(self , food , quantity):
        if food.fID in self.things:
            f , this = self.things[food.fID]
            self.things[food.fID] = (
                f , 
                this + quantity
            )
        else:
            self.things [food.fID] = (
                f,
                quantity
            )
        
    def remove_item(self , fID):
        if fID in self.things:
            del self.things[fID]
            
    def calculate_total(self):
        t = 0
        for i,j in self.things.values():
            t += i.price * j
        return t
    def apply_discount(self , code):
        if code in Order.discount:
            disc = Order.discount[code]
            t = self.calculate_total()
            return (t*(1-(disc/100)))
        else: return self.calculate_total()
        
    def display_order(self):
        for i,j in self.things.value():
            print(f"{i.name}: {j}ta , {i.price}toman")
        t= self.calculate_total()
        print(f"total is {t} toman")