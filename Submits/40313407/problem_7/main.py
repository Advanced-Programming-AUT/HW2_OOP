import pickle
import os

class User:
    def __init__(self, username, password, security_question, security_answer):
        self._username = username
        self._password = password
        self._security_question = security_question
        self._security_answer = security_answer
        self._balance = 0.0
        self._cart = []
        self._rated_products = []
        self.temp = 0

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_security_question(self):
        return self._security_question

    def get_security_answer(self):
        return self._security_answer

    def get_balance(self):
        return self._balance

    def add_balance(self, amount):
        self._balance += amount
        print(f"Balance updated: {self._balance}")

    def get_cart(self):
        return self._cart

    def add_to_cart(self, product, quantity):
        self._cart.append((product, quantity))

    def remove_from_cart(self, index):
        if 0 <= index < len(self._cart):
            return self._cart.pop(index)
        return None

    def clear_cart(self):
        self._cart = []

    def has_rated(self, product_name):
        return product_name in self._rated_products

    def add_rated_product(self, product_name):
        self._rated_products.append(product_name)

    def __str__(self):
        return f"User: {self._username}"


class Product:
    def __init__(self, name, seller, price, stock, category):
        self._name = name
        self._seller = seller
        self._price = price
        self._stock = stock
        self._rating = 0.0
        self._category = category
        self._num_ratings = 0

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def get_category(self):
        return self._category

    def get_seller(self):
        return self._seller

    def set_name(self, name):
        self._name = name

    def set_seller(self, seller):
        self._seller = seller

    def set_price(self, price):
        self._price = price

    def set_stock(self, stock):
        self._stock = stock

    def set_rating(self, rating):
        self._rating = rating

    def set_category(self, category):
        self._category = category

    def update_stock(self, quantity):
        self._stock -= quantity

    def rate(self, rating):
        if self._num_ratings == 0:
            self._rating = rating
        else:
            self._rating = (self._rating * self._num_ratings + rating) / (self._num_ratings + 1)
        self._num_ratings += 1

    def __str__(self):
        category = getattr(self, '_category', 'Unknown')
        return (f"{self._name} - Seller: {self._seller} - "
                f"Price: ${self._price} - Stock: {self._stock} - "
                f"Rating: {self._rating} - Category: {category}")


class OnlineStore:
    def __init__(self):
        self.users_file = "users.pkl"
        self.products_file = "products.pkl"
        self.categories_file = "categories.pkl"
        self.current_user = None
        self.login_attempts = {}
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, "rb") as f:
                    self.users = pickle.load(f)
            else:
                self.users = {}
        except (IOError, pickle.PickleError):
            print("Yo, we got a problem loadin' the users file, homie. Startin' fresh.")
            self.users = {}

        try:
            if os.path.exists(self.products_file):
                with open(self.products_file, "rb") as f:
                    self.products = pickle.load(f)
                for product in self.products:
                    if not hasattr(product, '_category'):
                        product._category = "Unknown"
                    if not hasattr(product, '_num_ratings'):
                        product._num_ratings = 0
            else:
                self.products = []
        except (IOError, pickle.PickleError):
            print("Man, somethin' broke while loadin' products, bruh. Startin' with nothin'.")
            self.products = []

        try:
            if os.path.exists(self.categories_file):
                with open(self.categories_file, "rb") as f:
                    self.categories = pickle.load(f)
            else:
                self.categories = []
        except (IOError, pickle.PickleError):
            print("Yo, categories file ain't loadin' right, fam. Startin' empty.")
            self.categories = []

    def save_data(self):
        try:
            with open(self.users_file, "wb") as f:
                pickle.dump(self.users, f)
            with open(self.products_file, "wb") as f:
                pickle.dump(self.products, f)
            with open(self.categories_file, "wb") as f:
                pickle.dump(self.categories, f)
        except IOError:
            print("Ayo, we got a lil' issue savin' the data, homie!")

    def sign_up(self):
        print("\nEnter a username:", end=" ")
        username = input()
        print("Enter a password (8 characters or more):", end=" ")
        password = input()
        print("Enter your security question:", end=" ")
        security_question = input()
        print("Enter the answer to your security question:", end=" ")
        security_answer = input()

        if len(password) < 8:
            print("Yo password gotta be 8 or more, bruh! Try again.")
            return False

        if username in self.users:
            print("This username already taken, homie! Pick another one.")
            return False

        self.users[username] = User(username, password, security_question, security_answer)
        self.save_data()
        print("Account created successfully!")
        return True

    def login(self):
        print("\nEnter your username:", end=" ")
        username = input()
        print("Enter your password:", end=" ")
        password = input()

        if username not in self.users:
            print("Who you, bruh? That username ain't here!")
            return False

        if username not in self.login_attempts:
            self.login_attempts[username] = 0

        if self.users[username].get_password() == password:
            self.login_attempts[username] = 0
            self.current_user = self.users[username]
            print("Login successful! Welcome back!")
            return True
        else:
            self.login_attempts[username] += 1
            if self.login_attempts[username] >= 3:
                print(f"Too many tries, bruh! Answer this: {self.users[username].get_security_question()}")
                answer = input("Your answer: ")
                if answer == self.users[username].get_security_answer():
                    self.login_attempts[username] = 0
                    self.current_user = self.users[username]
                    print("Aight, you good, fam! You in!")
                    return True
                else:
                    print("Nah, that ain't it, homie! You out!")
                    return False
            else:
                print(f"Wrong password, bruh! You got {3 - self.login_attempts[username]} tries left.")
                return False

    def view_all_products(self):
        if not self.products:
            print("No products available!")
            return
        print("\nAll Products:")
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product}")

    def search_by_name(self):
        print("\nEnter product name:", end=" ")
        name = input().lower()
        print("\nResults:")
        found = False
        for i in range(len(self.products)):
            product = self.products[i]
            if name in product.get_name().lower():
                print(f"{i+1}. {product}")
                found = True
        if not found:
            print("Ain't nothin' with that name, bruh!")

    def search_by_price_range(self):
        try:
            print("\nEnter minimum price:", end=" ")
            min_price = float(input())
            print("Enter maximum price:", end=" ")
            max_price = float(input())
            print("\nResults:")
            found = False
            for i, product in enumerate(self.products, 1):
                if min_price <= product.get_price() <= max_price:
                    print(f"{i}. {product}")
                    found = True
            if not found:
                print("Ain't nothin' in that price range, bruh!")
        except ValueError:
            print("Yo, you gotta gimme real numbers, fam!")

    def search_by_category(self):
        if not self.categories:
            print("No categories available!")
            return
        print("\nAvailable Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")
        print("Enter category number:", end=" ")
        try:
            index = int(input()) - 1
            if 0 <= index < len(self.categories):
                category = self.categories[index]
                print(f"\nResults for category '{category}':")
                found = False
                for i, product in enumerate(self.products, 1):
                    if product.get_category() == category:
                        print(f"{i}. {product}")
                        found = True
                if not found:
                    print("Ain't nothin' in that category, bruh!")
            else:
                print("That category number ain't right, homie!")
        except ValueError:
            print("Yo, gimme a real number, fam!")

    def add_to_cart(self):
        self.view_all_products()
        if not self.products:
            return
        print("\nEnter the product number to add to cart:", end=" ")
        try:
            index = int(input()) - 1
            if 0 <= index < len(self.products):
                product = self.products[index]
                print(f"Enter quantity (available stock: {product.get_stock()}):", end=" ")
                quantity = int(input())
                if quantity <= product.get_stock():
                    self.current_user.add_to_cart(product, quantity)
                    print(f"Added {quantity} of {product.get_name()} to your cart!")
                else:
                    print("We ain't got that much in stock, bruh!")
            else:
                print("That product number ain't right, homie!")
        except ValueError:
            print("Yo, gimme a real number, fam!")

    def view_cart(self):
        cart = self.current_user.get_cart()
        if not cart:
            print("\nYour cart is empty!")
            return
        print("\nYour Cart:")
        total = 0
        for i, (product, quantity) in enumerate(cart, 1):
            cost = product.get_price() * quantity
            total += cost
            print(f"{i}. {product.get_name()} - Quantity: {quantity} - Cost: ${cost}")
        print(f"Total: ${total}")

    def remove_from_cart(self):
        self.view_cart()
        if not self.current_user.get_cart():
            return
        print("\nEnter the item number to remove:", end=" ")
        try:
            index = int(input()) - 1
            removed_item = self.current_user.remove_from_cart(index)
            if removed_item:
                print(f"Removed {removed_item[0].get_name()} from your cart!")
            else:
                print("That item number ain't right, bruh!")
        except ValueError:
            print("Yo, gimme a real number, fam!")

    def finalize_order(self):
        cart = self.current_user.get_cart()
        if not cart:
            print("\nYour cart is empty!")
            return
        self.view_cart()
        total = sum(product.get_price() * quantity for product, quantity in cart)
        if self.current_user.get_balance() < total:
            print(f"Yo, you broke, homie! You need ${total}, but you only got ${self.current_user.get_balance()}!")
            return
        for product, quantity in cart:
            product.update_stock(quantity)
        self.current_user.clear_cart()
        self.save_data()
        print("Order finalized successfully!")

    def rate_purchased_products(self):
        self.view_all_products()
        if not self.products:
            return
        print("\nEnter the product number to rate:", end=" ")
        try:
            index = int(input()) - 1
            if 0 <= index < len(self.products):
                product = self.products[index]
                if self.current_user.has_rated(product.get_name()):
                    print(f"You already rated {product.get_name()}, bruh! One time's enough!")
                    return
                print(f"Enter your rating for {product.get_name()} (0-5):", end=" ")
                rating = float(input())
                if 0 <= rating <= 5:
                    product.rate(rating)
                    self.current_user.add_rated_product(product.get_name())
                    self.save_data()
                    print(f"Rating updated for {product.get_name()}!")
                else:
                    print("Yo, rating gotta be between 0 and 5, homie!")
            else:
                print("That product number ain't right, bruh!")
        except ValueError:
            print("Yo, gimme a real number, fam!")

    def add_balance(self):
        print("\nEnter amount to add to balance:", end=" ")
        try:
            amount = float(input())
            if amount > 0:
                self.current_user.add_balance(amount)
                self.save_data()
            else:
                print("Yo, that amount gotta be more than 0, bruh!")
            print("Balance added successfully!")
        except ValueError:
            print("Yo, gimme a real number, fam!")

    def view_categories(self):
        if not self.categories:
            print("No categories available!")
            return
        print("\nAvailable Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")

    def add_category(self):
        print("\nEnter new category name:", end=" ")
        category = input()
        if category in self.categories:
            print("We already got that category, bruh!")
            return
        self.categories.append(category)
        self.save_data()
        print(f"Category '{category}' added successfully!")

    def remove_category(self):
        self.view_categories()
        if not self.categories:
            return
        print("\nEnter the category number to remove:", end=" ")
        try:
            index = int(input()) - 1
            if 0 <= index < len(self.categories):
                category = self.categories[index]
                for product in self.products:
                    if product.get_category() == category:
                        print(f"Can't remove '{category}' 'cause it's used by '{product.get_name()}', bruh!")
                        return
                self.categories.pop(index)
                self.save_data()
                print(f"Category '{category}' removed successfully!")
            else:
                print("That category number ain't right, homie!")
        except ValueError:
            print("Yo, gimme a real number, fam!")

    def add_product(self):
        if not self.categories:
            print("No categories available! Please add a category first.")
            return
        print("\nEnter product name:", end=" ")
        name = input()
        print("Enter seller name:", end=" ")
        seller = input()
        print("Enter price:", end=" ")
        try:
            price = float(input())
            print("Enter stock quantity:", end=" ")
            stock = int(input())
            print("\nAvailable Categories:")
            for i, category in enumerate(self.categories, 1):
                print(f"{i}. {category}")
            print("Enter category number:", end=" ")
            index = int(input()) - 1
            if 0 <= index < len(self.categories):
                category = self.categories[index]
                self.products.append(Product(name, seller, price, stock, category))
                self.save_data()
                print("Product added successfully!")
            else:
                print("That category number ain't right, bruh!")
        except ValueError:
            print("Yo, gimme real numbers for price, stock, or category, fam!")

    def edit_product(self):
        self.view_all_products()
        if not self.products:
            return
        print("\nEnter the product number to edit:", end=" ")
        try:
            index = int(input()) - 1
            if 0 <= index < len(self.products):
                product = self.products[index]
                print("\nLeave blank to keep current value.")
                print(f"Current name: {product.get_name()}")
                name = input("New name: ") or product.get_name()
                print(f"Current seller: {product.get_seller()}")
                seller = input("New seller: ") or product.get_seller()
                print(f"Current price: {product.get_price()}")
                price_input = input("New price: ")
                price = float(price_input) if price_input else product.get_price()
                print(f"Current stock: {product.get_stock()}")
                stock_input = input("New stock: ")
                stock = int(stock_input) if stock_input else product.get_stock()
                print("\nAvailable Categories:")
                for i, category in enumerate(self.categories, 1):
                    print(f"{i}. {category}")
                print(f"Current category: {product.get_category()}")
                print("Enter new category number (or press Enter to keep current):", end=" ")
                category_input = input()
                if category_input:
                    category_index = int(category_input) - 1
                    if 0 <= category_index < len(self.categories):
                        category = self.categories[category_index]
                    else:
                        print("That category number ain't right, bruh! Keepin' the old one.")
                        category = product.get_category()
                else:
                    category = product.get_category()

                product.set_name(name)
                product.set_seller(seller)
                product.set_price(price)
                product.set_stock(stock)
                product.set_category(category)
                self.save_data()
                print("Product updated successfully!")
            else:
                print("That product number ain't right, homie!")
        except ValueError:
            print("Yo, gimme real numbers, fam!")

    def delete_product(self):
        self.view_all_products()
        if not self.products:
            return
        print("\nEnter the product number to delete:", end=" ")
        try:
            index = int(input()) - 1
            if 0 <= index < len(self.products):
                deleted_product = self.products.pop(index)
                self.save_data()
                print(f"Product '{deleted_product.get_name()}' deleted successfully!")
            else:
                print("That product number ain't right, bruh!")
        except ValueError:
            print("Yo, gimme a real number, fam!")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. View All Products")
            print("2. Add Product")
            print("3. Edit Product")
            print("4. Delete Product")
            print("5. View Categories")
            print("6. Add Category")
            print("7. Remove Category")
            print("8. Logout")
            choice = input(">> ")
            if choice == "1":
                self.view_all_products()
            elif choice == "2":
                self.add_product()
            elif choice == "3":
                self.edit_product()
            elif choice == "4":
                self.delete_product()
            elif choice == "5":
                self.view_categories()
            elif choice == "6":
                self.add_category()
            elif choice == "7":
                self.remove_category()
            elif choice == "8":
                print("Logged out successfully!")
                self.current_user = None
                break

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. View Products")
            print("2. Search Product")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Remove from Cart")
            print("6. Finalize Order")
            print("7. Rate Products")
            print("8. Add Balance")
            print("9. Logout")
            choice = input(">> ")
            if choice == "1":
                self.view_all_products()
            elif choice == "2":
                print("\nSearch by:")
                print("1. Name")
                print("2. Price Range")
                print("3. Category")
                search_choice = input(">> ")
                if search_choice == "1":
                    self.search_by_name()
                elif search_choice == "2":
                    self.search_by_price_range()
                elif search_choice == "3":
                    self.search_by_category()
            elif choice == "3":
                self.add_to_cart()
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.remove_from_cart()
            elif choice == "6":
                self.finalize_order()
            elif choice == "7":
                self.rate_purchased_products()
            elif choice == "8":
                self.add_balance()
            elif choice == "9":
                print("Logged out successfully!")
                self.current_user = None
                break

    def start(self):
        while True:
            print("\nWelcome to the Online Store!")
            print("1. Login")
            print("2. Sign Up")
            print("3. Exit")
            choice = input(">> ")
            if choice == "1":
                if self.login():
                    if self.current_user.get_username() == "admin":
                        self.admin_menu()
                    else:
                        self.main_menu()
            elif choice == "2":
                if self.sign_up():
                    continue
            elif choice == "3":
                print("You have exited the store!")
                break


if __name__ == "__main__":
    store = OnlineStore()
    if "admin" not in store.users:
        store.users["admin"] = User("admin", "adminpass", "What's your favorite color?", "blue")
        store.save_data()
    store.start()
