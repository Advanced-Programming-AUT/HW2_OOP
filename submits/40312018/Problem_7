import os
import pickle
import re

class Product:
    id_count = 1

    def __init__(self, name, category, price, stock, seller_username):
        self.id = Product.id_count
        Product.id_count += 1
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)
        self.seller = seller_username
        self.ratings = []

    def average_rating(self):
        if self.ratings:
            return round(sum(self.ratings) / len(self.ratings), 1)
        return 0

    def __str__(self):
        return (f"{self.id}. {self.name} - Seller: {self.seller} - Price: ${self.price} - "f"Stock: {self.stock} - Rating: {self.average_rating()}")

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password, "customer")
        self.balance = 0.0
        self.cart = {}
        self.rated_products = set()

class Seller(User):
    def __init__(self, username, password):
        super().__init__(username, password, "seller")
        self.my_products = []


class Store:
    def __init__(self):
        self.users = {}
        self.products = {}
        self.current_user = None

    def save_data(self):
        with open("store_data.pkl", "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load_data():
        if os.path.exists("store_data.pkl"):
            with open("store_data.pkl", "rb") as f:
                store = pickle.load(f)
            return store
        return Store()

    def signup(self, username, password, role):
        if re.match(r'^(?=(.*[A-Za-z]){3,})[A-Za-z0-9_]+$', username) is None:
            return "Invalid username format."
        if username in self.users:
            return "Username already exists."
        if len(password) < 8:
            return "Password must be at least 8 characters."
        if role not in ["customer", "seller"]:
            return "Role must be either 'customer' or 'seller'."
        if role == "customer":
            self.users[username] = Customer(username, password)
        else:
            self.users[username] = Seller(username, password)
        self.save_data()
        return "Account created successfully!"

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            return f"Login successful! Logged in as {user.role}."
        return "Invalid username or password."

    def logout(self):
        self.current_user = None
        return "Logged out successfully."

    def add_product(self, name, category, price, stock):
        if not isinstance(self.current_user, Seller):
            return "Only sellers can add products."
        for p in self.products.values():
            if p.name.lower() == name.lower():
                return "Product already exists."
        product = Product(name, category, price, stock, self.current_user.username)
        self.products[product.id] = product
        self.current_user.my_products.append(product.id)
        self.save_data()
        return f"Product '{name}' added successfully with ID {product.id}."

    def add_stock(self, product_id, stock):
        if not isinstance(self.current_user, Seller):
            return "Only sellers can add stock."

        product = self.products.get(product_id)
        if not product:
            return "Product not found."
        if product.seller != self.current_user.username:
            return "You can only add stock to your own products."
        product.stock += int(stock)
        self.save_data()
        return f"Stock updated. New stock for {product.name}: {product.stock}"

    def view_my_products(self):
        if not isinstance(self.current_user, Seller):
            return "Only sellers can view their products."
        result = []
        for i in self.current_user.my_products:
            product = self.products.get(i)
            if product:
                result.append(str(product))
        return "\n".join(result) if result else "No products found."

    def view_products(self):
        if not self.products:
            return "No products available."
        result = []
        for j in self.products.values():
            result.append(str(j))
        return "\n".join(result)

    def search_products(self, request, value):
        result = []
        if request == "name":
            for j in self.products.values():
                if value.lower() in j.name.lower():
                    result.append(str(j))
        elif request == "price":
                r1, r2 = map(float, value.split('-'))
                for p in self.products.values():
                    if r1 <= p.price <= r2:
                        result.append(str(p))
        elif request == "category":
            for p in self.products.values():
                if value.lower() == p.category.lower():
                    result.append(str(p))
        else:
            return "Invalid search request."
        return "\n".join(result) if result else "No products found matching the request."

    def add_to_cart(self, product_id, quantity):
        if not isinstance(self.current_user, Customer):
            return "Only customers can add to cart."
        product = self.products.get(product_id)
        if not product:
            return "Product not found."
        quantity = int(quantity)
        if quantity > product.stock:
            return f"Not enough stock available. Stock: {product.stock}"
        cart = self.current_user.cart
        cart[product_id] = cart.get(product_id, 0) + quantity
        self.save_data()
        return f"Added {quantity} of '{product.name}' to your cart."

    def view_cart(self):
        if not isinstance(self.current_user, Customer):
            return "Only customers can view cart."
        cart = self.current_user.cart
        if not cart:
            return "Your cart is empty."
        result = []
        for i, j in cart.items():
            product = self.products.get(i)
            if product:
                result.append(f"{product.id}. {product.name} - Price: ${product.price} - Quantity: {j}")
        return "\n".join(result)

    def remove_from_cart(self, product_id):
        if not isinstance(self.current_user, Customer):
            return "Only customers can remove items from cart."
        cart = self.current_user.cart
        if product_id in cart:
            del cart[product_id]
            self.save_data()
            return "Product removed from cart."
        return "Product not found in cart."

    def finalize_order(self):
        if not isinstance(self.current_user, Customer):
            return "Only customers can finalize orders."
        total_cost = 0.0
        for i, j in self.current_user.cart.items():
            product = self.products.get(i)
            if product:
                if j > product.stock:
                    return f"not enough stock for {product.name}."
                total_cost += product.price * j

        if total_cost > self.current_user.balance:
            return "not enough balance."
        for i, j in self.current_user.cart.items():
            product = self.products.get(i)
            if product:
                product.stock -= j
        self.current_user.balance -= total_cost
        self.current_user.cart.clear()
        self.save_data()
        return f"Order finalized! Total cost: ${total_cost}"

    def add_balance(self, amount):
        if not isinstance(self.current_user, Customer):
            return "Only customers can add balance."

            a = float(amount)
            self.current_user.balance += a
            self.save_data()
            return f"Balance updated! New balance: ${self.current_user.balance}"


    def rate_product(self, product_id, rating):
        if not isinstance(self.current_user, Customer):
            return "Only customers can rate products."
        if product_id not in self.current_user.rated_products:
            product = self.products.get(product_id)
            if product:
                    rating = float(rating)
                    if not (0 <= rating <= 5):
                        return "Rating must be between 0 and 5."
                    product.ratings.append(rating)
                    self.current_user.rated_products.add(product_id)
                    self.save_data()
                    return f"Thank you for rating '{product.name}' with {rating} stars."
            return "Product not found."
        else:
            return "You have already rated this product."


def main_menu(store):
    while True:
        print("\nMain Menu:")
        if store.current_user.role == "customer":
            print("1. View Products")
            print("2. Search Product")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Remove from Cart")
            print("6. Finalize Order")
            print("7. Rate Purchased Products")
            print("8. Add Balance")
            print("9. Logout")
            choice = input(">> ")
            if choice == "1":
                print("\nProducts:")
                print(store.view_products())
            elif choice == "2":
                print("Search by:")
                print("1. Name")
                print("2. Price Range")
                print("3. Category")
                n = input(">> ")
                if n == "1":
                    name = input("Enter product name: ")
                    print("Results:")
                    print(store.search_products("name", name))
                elif n == "2":
                    pr = input("Enter price range (min-max): ")
                    print("Results:")
                    print(store.search_products("price", pr))
                elif n == "3":
                    cat = input("Enter category: ")
                    print("Results:")
                    print(store.search_products("category", cat))
                else:
                    print("Invalid search option.")
            elif choice == "3":
                    i = int(input("Enter product ID to add to cart: "))
                    j = int(input("Enter quantity: "))
                    print(store.add_to_cart(i, j))
            elif choice == "4":
                print("Your Cart:")
                print(store.view_cart())
            elif choice == "5":
                    i = int(input("Enter product ID to remove from cart: "))
                    print(store.remove_from_cart(i))
            elif choice == "6":
                print(store.finalize_order())
            elif choice == "7":
                    i = int(input("Enter product ID to rate: "))
                    rate = input("Enter rating (0-5): ")
                    print(store.rate_product(i, rate))
            elif choice == "8":
                a = input("Enter amount to add: ")
                print(store.add_balance(a))
            elif choice == "9":
                print(store.logout())
                break
            else:
                print("Invalid option.")
        elif store.current_user.role == "seller":
            print("1. Add Product")
            print("2. Add Stock to Product")
            print("3. View My Products")
            print("4. Logout")
            choice = input(">> ")
            if choice == "1":
                name = input("Enter product name: ")
                category = input("Enter category: ")
                price = input("Enter price: ")
                stock = input("Enter initial stock: ")
                print(store.add_product(name, category, price, stock))
            elif choice == "2":
                    i = int(input("Enter product ID to add stock: "))
                    extra = int(input("Enter quantity to add: "))
                    print(store.add_stock(i, extra))
            elif choice == "3":
                print("Your Products:")
                print(store.view_my_products())
            elif choice == "4":
                print(store.logout())
                break
            else:
                print("Invalid option.")

def menu(store):
    while True:
        print("\nWelcome to the Online Store!")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        choice = input(">> ")
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            result = store.login(username, password)
            print(result)
            if store.current_user:
                main_menu(store)
        elif choice == "2":
            username = input("Enter a username: ")
            password = input("Enter a password (min 8 characters): ")
            role = input("Enter role (customer/seller): ")
            result = store.signup(username, password, role.lower())
            print(result)
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    store = Store.load_data()
    menu(store)
