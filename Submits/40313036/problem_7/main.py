import pickle
import os

class User:
    def __init__(self, username, password, security_question, security_answer):
        self.username = username
        self.password = password
        self.security_question = security_question
        self.security_answer = security_answer
        self.balance = 0.0
        self.cart = []
        self.rated_products = []

    def add_balance(self, amount):
        self.balance += amount

    def add_to_cart(self, product, quantity):
        self.cart.append((product, quantity))

    def remove_from_cart(self, index):
        if 0 <= index < len(self.cart):
            return self.cart.pop(index)
        return None

    def clear_cart(self):
        self.cart = []

    def has_rated(self, product_name):
        return product_name in self.rated_products

    def add_rated_product(self, product_name):
        self.rated_products.append(product_name)


class Product:
    def __init__(self, name, seller, price, stock, category):
        self.name = name
        self.seller = seller
        self.price = price
        self.stock = stock
        self.rating = 0.0
        self.category = category
        self.num_ratings = 0

    def update_stock(self, quantity):
        self.stock -= quantity

    def rate(self, rating):
        if self.num_ratings == 0:
            self.rating = rating
        else:
            self.rating = (self.rating * self.num_ratings + rating) / (self.num_ratings + 1)
        self.num_ratings += 1


class Store:
    def __init__(self):
        self.users_file = "users.pkl"
        self.products_file = "products.pkl"
        self.categories_file = "categories.pkl"
        self.current_user = None
        self.users = {}
        self.products = []
        self.categories = []
        self.login_attempts = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, "rb") as f:
                self.users = pickle.load(f)

        if os.path.exists(self.products_file):
            with open(self.products_file, "rb") as f:
                self.products = pickle.load(f)

        if os.path.exists(self.categories_file):
            with open(self.categories_file, "rb") as f:
                self.categories = pickle.load(f)

    def save_data(self):
        with open(self.users_file, "wb") as f:
            pickle.dump(self.users, f)
        with open(self.products_file, "wb") as f:
            pickle.dump(self.products, f)
        with open(self.categories_file, "wb") as f:
            pickle.dump(self.categories, f)

    def register_user(self, username, password, security_question, security_answer):
        if username in self.users or len(password) < 8:
            return False
        self.users[username] = User(username, password, security_question, security_answer)
        self.save_data()
        return True

    def login_user(self, username, password):
        if username not in self.users:
            return False

        if self.users[username].password == password:
            self.login_attempts[username] = 0
            self.current_user = self.users[username]
            return True
        
        self.login_attempts[username] = self.login_attempts.get(username, 0) + 1
        return False

    def recover_password(self, username, answer):
        if username in self.users and self.users[username].security_answer == answer:
            self.login_attempts[username] = 0
            self.current_user = self.users[username]
            return True
        return False

    def search_by_name(self, name):
        return [p for p in self.products if name.lower() in p.name.lower()]

    def search_by_price_range(self, min_price, max_price):
        return [p for p in self.products if min_price <= p.price <= max_price]

    def search_by_category(self, category):
        return [p for p in self.products if p.category == category]

    def add_product_to_cart(self, product_index, quantity):
        if 0 <= product_index < len(self.products):
            product = self.products[product_index]
            if quantity <= product.stock:
                self.current_user.add_to_cart(product, quantity)
                return True
        return False

    def get_cart_summary(self):
        cart = self.current_user.cart
        return [(item[0].name, item[1], item[0].price * item[1]) for item in cart]

    def checkout(self):
        total = sum(product.price * quantity for product, quantity in self.current_user.cart)
        if self.current_user.balance >= total:
            for product, quantity in self.current_user.cart:
                product.update_stock(quantity)
            self.current_user.balance -= total
            self.current_user.clear_cart()
            self.save_data()
            return True
        return False
