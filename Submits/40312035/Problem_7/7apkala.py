class User:
    def __init__(self , username , password):
        self.username = username ; self.password = password
        self.balance = 0
        self.cart = [] ; self.orders = [] ; self.reviews = set()
    def add_balance(self , amount):
        self.balance += amount
    def hazf_from_cart(self):
        for i in self.cart:
            i['product'].anbar += i['quantity']
            self.cart.remove(i) ; return
    def sabt(self , name):
        total = ...
        if total > self.balance:
            return "!!!"
        for i in self.cart:
            if i['quantity'] > i['product'].anbar:
                return "!!!"
        self.balance -= total
        self.orders.append(name) ; print('done')
        return 
    def show_cart(self):
        return self.car



class Customer(User):
    def menu(self):
        return {
            1 : "view products",
            2 : "search product",
            3 : "add to cart",
            4 : "view cart",
            5 : "remove",
            6 : "finalize",
            7 : "rate purchased product",
            8 : "add balance",
            9 : "logout"
        }

    def add_to_cart(self , product , quantity):
        if quantity > product.anbar:
            return "!!"
        
        for i in self.cart:
            new_quantity = i['quantity']+quantity
            if new_quantity >product.anbar:
                return "!!"
            i['quantity'] = new_quantity
            return "!!"
        self.cart.append({'product': product,'quantity': quantity})
        print('done') ; return 




class Forooshande(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    def menu(self):
        return {
            1 : "view products",
            2 : "add product",
            3 : "update anbar",
            4 : "logout"
        }
    def add_product(self , name , price , category):
        pass
class Product:
    def __init__(self, name, price, category, anbar, seller):
        self.name = name
        self.price = price
        self.category = category
        self.anbar = anbar
        self.seller = seller
        self.ratings = {} 

    def add_rating(self , username , rating):
            self.ratings[username] = rating
    def get_v_rating(self):
        return sum(self.ratings.values())/len(self.ratings)

    def __str__(self):
        pass