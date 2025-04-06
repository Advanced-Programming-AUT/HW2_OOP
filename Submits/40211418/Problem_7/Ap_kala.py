import pickle
from abc import ABC, abstractmethod
import re


class User(ABC):
    def __init__(self, username, password, roll):
        self.__username = username
        self.__password = password
        self.roll = roll

    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @staticmethod
    @abstractmethod
    def get_menu():
        pass

    
class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password, 'customer')
        self.__balance = 0
        self.__cart = {}
        self.__final_cart = {}
        self.__bought_items = set()
        self.rated_products= set()

    @property
    def balance(self):
        return self.__balance
    
    def add_to_cart(self, product, quantity):
        if isinstance(product, Product):
            if product.stock >= quantity:
                self.__cart[product] = self.__cart.get(product, 0) + quantity
                return f'Product: {product.name} added to cart'
            else:
                return f'not Enough balance ,current stock: {product.stock}'
            
    def remove_from_cart(self, name, quantity):
            for product in self.__cart:
                if product.name == name:
                    in_cart = self.__cart.get(product, 0)
                    if in_cart >= quantity:
                        self.__cart[product] -= quantity
                    else:
                        return 'not enough product in cart'
                if self.__cart[product] <= 0:
                    self.__cart.pop(product)
                product.add_stock(quantity)
                return 'removed successfully'
            
    def add_balance(self, value):
        self.__balance += value

    def view_cart(self):
        return '\n'.join(str(p)+f' in cart: {self.__cart[p]}' for p in self.__cart)

    def finalize_cart(self):
        self.__final_cart = self.__cart
        return 'finalized successfully'
    
    def rate(self, product, n):
        if product in self.__bought_items:
            if product not in self.rated_products:
                product.add_rating(n)
                return 'rate added successfully'
            else:
                return 'product already rated'
        else:
            return 'you can\'t rate this product'

    def buy(self):
        payable = Product.product_sum(self.__final_cart)
        if payable <= self.__balance:
            self.__balance -= payable
            self.__bought_items = self.__bought_items | set(self.__final_cart.keys())
            self.__final_cart.clear()
            self.__cart.clear()
            return 'bought successfully'
        else:
            return 'Not enough balance'

    @staticmethod
    def search(search , search_by, products):
        output = []
        if search_by == 'name':
            for product in products:
                if search in product.name:
                    output.append(product)
        elif search_by == 'category':
            for product in products:
                if search == product.category:
                    output.append(product)
        elif search_by == 'price_range':
            if re.match(r'\d+-\d+', search):
                minimum, maximum = map(int, search.split('-'))
                for product in products:
                    if product.price >= minimum and product.price <= maximum:
                        output.append(product)
            else:
                return 'invalid input'
        return output

    @staticmethod
    def get_menu():
        return "Main menu:\n"\
            "1. View products\n"\
            "2. Search Products\n"\
            "3. Add to Cart\n"\
            "4. View Cart\n"\
            "5. Remove from Cart\n"\
            "6. Finalize Order\n"\
            "7. Rate Purchased Products\n"\
            "8. Add Balance\n"\
            "9. View Balance\n"\
            "10. Log out"
    


class Seller(User):
    def __init__(self, username, password):
        super().__init__(username, password, 'seller')
        self._products = set()

    @property
    def products(self):
        return '\n'.join(str(product) for product in self._products)


    def add_product(self, name, price, stock, category):
        product = Product(name, price, stock, category, self)
        self._products.add(product)
        return product

    def add_stock(self, name, stock):
        for product in self._products:
            if product.name == name and product.seller == self:
                product.add_stock(stock)
                return 'stock updated'
        return 'error happend'


    @staticmethod
    def get_menu():
        return "1. Add product\n"\
                "2. View my products\n"\
                "3. Add stock\n"\
                "4. Log out"
    
    


class Product:
    id = 1
    def __init__(self, name, price, stock, category, seller):
        self.name = name
        self.price = price
        self._stock = stock
        self.category = category
        self.seller = seller
        self._ratings = []
        self.id = Product.id
        Product.id += 1
        


    @property
    def stock(self):
        return self._stock
    
    @property
    def average_rate(self):
        return sum(self._ratings) / len(self._ratings) if self._ratings else 0
    
    @staticmethod
    def product_sum(products):
        amount = 0
        for product in products:
            amount += product.price * products[product]
        return amount
    
    def add_rating(self, rate):
        self._ratings.append(rate)

    def add_stock(self, quantity):
        self._stock += quantity

    def reduce_stock(self, quantity):
        self._stock -= quantity

    

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        elif isinstance(other, int):
            return other + self.price
        
    def __str__(self):
        return f"{self.name} - Seller: {self.seller.username} - Price: {self.price} - stock: {self.stock} - Rating: {self.average_rate}"

    

class Data:
    
    @staticmethod
    def save(file_name, value):
        try:
            with open(file_name, 'wb') as fout:
                pickle.dump(value, fout)
        except:
            print('an error happend while writing to file')
        
    @staticmethod
    def load(file_name):
        try:
            with open(file_name, 'rb') as fin:
                return pickle.load(fin)
        except:
            return False



class Autintication:
    def __init__(self):
        self.userpass = Data.load('userpass.pkl') or {}
        self.users = Data.load('users.pkl') or {}
        
    def sign_up(self, username, password, roll):
        if username in self.userpass.keys():
            print(f"{username} already exist")
            return False
        if not re.match(r'^(?=.*\d)[A-Za-z\d]{8,}$', password):
            print("incorrect password")
            return False
        self.userpass[username] = password
        if roll == 'customer':
            user = Customer(username, password)
            self.users[username] = user
            Data.save('userpass.pkl', self.userpass)
            Data.save('users.pkl', self.users)
            print(self.users)
            return user
        if roll == 'seller':
            user = Seller(username, password)
            self.users[username] = user
            Data.save('userpass.pkl', self.userpass)
            Data.save('users.pkl', self.users)
            return user

    def log_in(self,username, password):
        if username in self.users and self.userpass[username] == password:
            return self.users[username]
        else:
            print("wrong username or password")
            return False
        
def customer_main(products, user):
    users = Data.load('users.pkl') or {}
    while True:
        print(Customer.get_menu())
        choice = input('>> ')
        if choice == '1':
            print('\n'.join(str(product) for product in products))
        elif choice == '2':
            print('search by: \n1.name \n2.Price Range \n3.Category')
            choice = input('>> ')
            if  choice == '1':
                name = input('Enter product name: ')
                print('\n'.join(str(p) for p in Customer.search(name, 'name', products)))
            elif choice == '2':
                range = input('Enter price range: (min-max)')
                print('\n'.join(str(p) for p in Customer.search(range, 'price_range', products)))
            elif choice == '3':
                cat = input('Enter category: ')
                print('\n'.join(str(p) for p in Customer.search(cat, 'category', products)))
            else:
                print('invalid choice')
        elif choice == '3':
            name = input('Enter product name: ')
            quantity = input('Enter quantity: ')
            flag = 0
            if quantity.isdigit():
                for product in products:
                    if product.name == name:
                        print(user.add_to_cart(product, int(quantity)))
                        product.reduce_stock(int(quantity))
                        flag = 1
            else:
                print('invalid input')
            if not flag:
                print('no such a product')
        elif choice == '4':
            print(user.view_cart())
        elif choice == '5':
            name = input('Enter product name: ')
            quantity = input('Enter quantity: ')
            print(user.remove_from_cart(name, int(quantity)))
        elif choice == '6':
            print(user.finalize_cart())
            print(user.buy())
        elif choice == '7':
            name = input('Enter product name: ')
            n = input('Enter your rate to this product (0 - 5.0): ')
            try:
                n = float(n)
                if n < 5 and n > 0:
                    for product in products:
                        if product.name == name:
                            print(user.rate(product, n))
            except ValueError :
                print('invalid input')
        elif choice == '8':
            balance = input('Enter amount: ')
            if balance.isdigit():
                user.add_balance(int(balance))
                print('added successfully')
            else:
                print('invalid input')
        elif choice == '9':
            print(f'Balance: {user.balance}')
        elif choice == '10':
            print('Logging Out')
            users.update({user.username: user})
            Data.save('users.pkl', users)
            Data.save('products.pkl', products)
            break

def seller_main(products, user):
    users = Data.load('users.pkl') or {}
    while True:
        print(Seller.get_menu())
        choice = input('>> ')
        if choice == '1':
            name = input('Enter product name: ')
            price = input('Enter product price:')
            stock = input('Enter product stock: ')
            category = input('Enter product category: ')
            if price.isdigit() and stock.isdigit():
                products.append(user.add_product(name, int(price), int(stock), category))
                Data.save('products.pkl', products)
                print('product added successfully')
            else:
                print('invalid input')
        elif choice == '2':
            name = input('Enter product name: ')
            stock = input('Enter stock: ')
            if stock.isdigit():
                print(user.add_stock(name, int(stock)))
        elif choice == '3':
            print(user.products)

        elif choice == '4':
            users.update({user.username: user})
            Data.save('users.pkl', users)
            break
        else:
            print('invalid input')
        
        


def main():
    products = Data.load('products.pkl') or []
    auth = Autintication()
    while True:
        print("Welcom to AP_online_store")
        print("Main menu: \n1.Sign up \n2.Log in \n3.Exit")
        choice = input('>> ')
        match choice:
            case "1":
                while True:
                    username = input('Enter username: ')
                    password = input('Enter Password: ')
                    roll = input('choose your roll: \n1.customer \n2.seller \n>> ')
                    if roll == '1':
                        user = auth.sign_up(username, password, 'customer')
                        if user:
                            print('sign up done')
                            break
                        else:
                            continue
                    elif roll == '2':
                        user = auth.sign_up(username, password, 'seller')
                        if user:
                            print('sign up done')
                            break
                        else:
                            continue
                    else:
                        print('invalid roll')
                
                if roll == '1':
                    customer_main(products, user)
                elif roll == '2':
                    seller_main(products, user)
                    
                            
                
            case '2':
                while True:
                    username = input('Enter your username: ')
                    password = input('Enter your password: ')
                    user = auth.log_in(username, password)
                    if user:
                        break
                if user.roll == 'customer':
                    customer_main(products, user)

                elif user.roll == 'seller':
                    seller_main(products, user)
            case '3':
                print('goodbye')
                break
            case _:
                print('invalid input')

if __name__ == '__main__':
    main()
