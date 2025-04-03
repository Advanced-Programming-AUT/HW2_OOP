class User:
    def __init__(self, username, password, is_seller=False):
        self._username = username
        self._password = password
        self._is_seller = is_seller
        self._balance = 0.0
        self._rated_products = set()

    @property
    def username(self):
        return self._username

    @property
    def is_seller(self):
        return self._is_seller

    @property
    def balance(self):
        return self._balance

    def check_password(self, password):
        return self._password == password

    def add_balance(self, amount):
        self._balance += amount

    def deduct_balance(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def has_rated(self, product_name):
        return product_name in self._rated_products

    def add_rated_product(self, product_name):
        self._rated_products.add(product_name)

class Product:
    def __init__(self, name, seller, price, stock, category):
        self._name = name
        self._seller = seller
        self._price = price
        self._stock = stock
        self._category = category
        self._ratings = []  # list of ratings

    @property
    def name(self):
        return self._name

    @property
    def seller(self):
        return self._seller

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    @property
    def category(self):
        return self._category

    @property
    def rating(self):
        return sum(self._ratings) / len(self._ratings) if self._ratings else 0.0

    def add_rating(self, rating):
        self._ratings.append(rating)

    def reduce_stock(self, quantity):
        if self._stock >= quantity:
            self._stock -= quantity
            return True
        return False

    def increase_stock(self, quantity):
        self._stock += quantity

class Store:
    def __init__(self):
        self.users = []
        self.products = []
        self.cart = []  # list of {product, quantity}
        self.current_user = None

    def signup(self):
        username = input("Enter a username: ")
        if any(user.username == username for user in self.users):
            print("Username already exists!")
            return
        password = input("Enter a password (min 8 characters): ")
        if len(password) < 8:
            print("Password must be at least 8 characters!")
            return
        is_seller = input("Are you a seller? (yes/no): ").lower() == "yes"
        self.users.append(User(username, password, is_seller))
        print("Account created successfully!")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for user in self.users:
            if user.username == username and user.check_password(password):
                self.current_user = user
                print("Login successful!")
                return True
        print("Wrong username or password!")
        return False

    def logout(self):
        self.current_user = None
        self.cart.clear()
        print("Logged out!")

    def view_products(self):
        if not self.products:
            print("No products available.")
        for product in self.products:
            print(f"{product.name} - Seller: {product.seller} - Price: ${product.price} - Stock: {product.stock} - Rating: {product.rating:.1f}")

    def search_product(self):
        print("Search by:")
        print("1. Name  2. Price Range  3. Category")
        choice = input(">> ")
        if choice == "1":
            name = input("Enter product name: ")
            results = [product for product in self.products if product.name.lower() == name.lower()] #filter by name
        elif choice == "2":
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            results = [product for product in self.products if min_price <= product.price <= max_price]#filter by price
        elif choice == "3":
            category = input("Enter category: ")
            results = [product for product in self.products if product.category.lower() == category.lower()]#filter by category
        else:
            print("Invalid choice!")
            return
        if not results:
            print("No products found.")
        for i, product in enumerate(results, 1):
            print(f"{i}. {product.name} - Seller: {product.seller} - Price: ${product.price} - Stock: {product.stock} - Rating: {product.rating:.1f}")
        return results

    def add_to_cart(self):
        results = self.search_product()
        if not results:
            return
        product_idx = int(input("Enter product number to add to cart: ")) - 1
        if 0 <= product_idx < len(results):
            product = results[product_idx]
            quantity = int(input("Enter quantity: "))
            if quantity > product.stock:
                print("Error: Quantity exceeds available stock!")
            else:
                self.cart.append({"product": product, "quantity": quantity})
                print("Added to cart!")
        else:
            print("Invalid product number!")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for i, item in enumerate(self.cart, 1):
                product = item["product"]
                print(f"{i}. {product.name}: {item['quantity']} - Price: ${product.price * item['quantity']}")

    def remove_from_cart(self):
        self.view_cart()
        if not self.cart:
            return
        idx = int(input("Enter item number to remove (1-based): ")) - 1
        if 0 <= idx < len(self.cart):
            del self.cart[idx]
            print("Item removed from cart!")
        else:
            print("Invalid item number!")

    def finalize_order(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        total = sum(item["product"].price * item["quantity"] for item in self.cart)
        if self.current_user.deduct_balance(total):
            for item in self.cart:
                item["product"].reduce_stock(item["quantity"])
            self.cart.clear()
            print(f"Order finalized! New balance: ${self.current_user.balance:.2f}")
        else:
            print("Insufficient balance!")

    def rate_products(self):
        if not self.cart:
            print("Your cart is empty. Add products to rate them.")
            return
        for item in self.cart:
            product = item["product"]
            if not self.current_user.has_rated(product.name):# Check if the current user has not rated this product
                rating = float(input(f"Rate {product.name} (0-5): "))
                if 0 <= rating <= 5:
                    product.add_rating(rating)
                    self.current_user.add_rated_product(product.name)
                    print(f"Rated {product.name} successfully!")
                else:
                    print("Rating must be between 0 and 5!")
            else:
                print(f"You have already rated {product.name}.")

    def add_balance(self):
        amount = float(input("Enter amount to add: "))
        self.current_user.add_balance(amount)
        print(f"Added ${amount:.2f}. New balance: ${self.current_user.balance:.2f}")

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        category = input("Enter category: ")
        self.products.append(Product(name, self.current_user.username, price, stock, category))
        print("Product added!")

    def update_stock(self):
        name = input("Enter product name: ")
        product = next((product for product in self.products if product.name == name and product.seller == self.current_user.username), None)
        if product:#if name was found
            quantity = int(input("Enter stock to add: "))
            product.increase_stock(quantity)
            print("Stock updated!")
        else:
            print("Product not found or you don’t own it!")


def main():
    store = Store()
    while True:
        print("\nWelcome to the Online Store!")
        print("1. Login  2. Sign Up  3. Exit")
        choice = input(">> ")
        if choice == "1":
            if store.login():
                if store.current_user.is_seller:
                    seller_menu(store)
                else:
                    buyer_menu(store)
        elif choice == "2":
            store.signup()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

def buyer_menu(store):
    while True:
        print("\nMain Menu:")
        print("1. View Products  2. Search Product  3. Add to Cart  4. View Cart")
        print("5. Remove from Cart  6. Finalize Order  7. Rate Purchased Products")
        print("8. Add Balance  9. Logout")
        choice = input(">> ")
        if choice == "1":
            store.view_products()
        elif choice == "2":
            store.search_product()
        elif choice == "3":
            store.add_to_cart()
        elif choice == "4":
            store.view_cart()
        elif choice == "5":
            store.remove_from_cart()
        elif choice == "6":
            store.finalize_order()
        elif choice == "7":
            store.rate_products()
        elif choice == "8":
            store.add_balance()
        elif choice == "9":
            store.logout()
            break
        else:
            print("Invalid choice!")

def seller_menu(store):
    while True:
        print("\nSeller Menu:")
        print("1. Add Product  2. Logout")
        choice = input(">> ")
        if choice == "1":
            store.add_product()
        elif choice == "2":
            store.logout()
            break
        else:
            print("Invalid choice!")

main()

