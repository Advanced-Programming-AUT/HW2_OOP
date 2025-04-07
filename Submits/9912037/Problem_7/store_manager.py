import pickle
import os
from user import User
from product import Product


class StoreManager:
    def __init__(self):
        self.list_of_all_users = []
        self.list_of_all_products = []
        self.user_currently_logged_in = None
        self.load_all_data()

    def save_all_data(self):
        with open('store_data.pkl', 'wb') as file:
            pickle.dump((self.list_of_all_users, self.list_of_all_products), file)

    def load_all_data(self):
        if os.path.exists('store_data.pkl'):
            with open('store_data.pkl', 'rb') as file:
                self.list_of_all_users, self.list_of_all_products = pickle.load(file)

    def create_user(self, username, password, role):
        if any(user.username_of_this_user == username for user in self.list_of_all_users):
            return False
        if len(password) < 8:
            return False
        if role not in ['customer', 'seller']:
            return False

        new_user = User(username, password, role)
        self.list_of_all_users.append(new_user)
        self.save_all_data()
        return True

    def login(self, username, password):
        for user in self.list_of_all_users:
            if user.username_of_this_user == username and user.password_of_this_user == password:
                self.user_currently_logged_in = user
                return True
        return False

    def logout(self):
        self.user_currently_logged_in = None
        return True

    def get_products_by_seller(self, seller_username):
        return [product for product in self.list_of_all_products if product.seller_of_this_product == seller_username]

    def search_products(self, search_type, search_term):
        if search_type == 'name':
            return [p for p in self.list_of_all_products if search_term.lower() in p.name_of_this_product.lower()]
        elif search_type == 'category':
            return [p for p in self.list_of_all_products if p.category_of_this_product.lower() == search_term.lower()]
        return []

    def add_product(self, name, price, stock, category):
        if self.user_currently_logged_in and self.user_currently_logged_in.role_of_this_user == 'seller':
            new_product = Product(name, self.user_currently_logged_in.username_of_this_user, price, stock, category)
            self.list_of_all_products.append(new_product)
            self.save_all_data()
            return True
        return False