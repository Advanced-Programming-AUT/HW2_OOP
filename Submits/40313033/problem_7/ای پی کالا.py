import pickle


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, password):
        return self.password == password


class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.balance = 0
        self.cart = {}
        self.purchased_products = {}

    def add_balance(self, amount):
        self.balance += amount
        print(
            f"Balance updated successfully! Your new balance: ${self.balance:.2f}")

    def view_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart[product] = quantity
            product.stock -= quantity
            print(f"{quantity} units of {product.name} added to the cart.")
        else:
            print("Not enough stock available!")

    def remove_from_cart(self, product_name):
        for product in list(self.cart.keys()):
            if product.name == product_name:
                product.stock += self.cart[product]
                del self.cart[product]
                print(f"Removed {product_name} from your cart.")
                return
        print("Product not found in your cart.")

    def finalize_order(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        total_cost = sum(product.price * qty for product,
                         qty in self.cart.items())
        if self.balance >= total_cost:
            self.balance -= total_cost
            print("Your order has been successfully placed!")
            for product, qty in self.cart.items():
                if product in self.purchased_products:
                    self.purchased_products[product] += qty
                else:
                    self.purchased_products[product] = qty
            self.cart.clear()
        else:
            print("Insufficient balance!")

    def rate_product(self, product, rating):
        if product not in self.purchased_products and product not in self.cart:
            print("You can only rate products you have purchased or have in your cart.")
            return
        if not (1.0 <= rating <= 5.0):
            print("Rating must be between 1.0 and 5.0.")
            return
        if product.name in product.user_ratings:
            print("You have already rated this product.")
            return
        product.ratings.append(rating)
        product.user_ratings[self.username] = rating
        print("Rating submitted successfully.")


class Seller(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = []

    def add_product(self, name, price, stock):
        product = Product(name, self.username, price, stock)
        self.products.append(product)
        return product

    def update_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                print(f"Updating {product.name}...")
                new_name = input(
                    "Enter new name (leave blank to keep current): ").strip()
                new_price = input(
                    "Enter new price (leave blank to keep current): ").strip()
                new_stock = input(
                    "Enter new stock quantity (leave blank to keep current): ").strip()

                if new_name:
                    product.name = new_name
                if new_price:
                    product.price = float(new_price)
                if new_stock:
                    product.stock = int(new_stock)

                print(f"{product.name} updated successfully!")
                return
        print("Product not found.")


class Product:
    def __init__(self, name, seller, price, stock):
        self.name = name
        self.seller = seller
        self.price = price
        self.stock = stock
        self.ratings = []
        self.user_ratings = {}

    def average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0


class Store:
    def __init__(self):
        self.users = {}
        self.products = []

    def register_user(self, username, password, user_type):
        if username in self.users:
            print("This username is already taken!")
            return None
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return None
        user = Customer(username, password) if user_type == "customer" else Seller(
            username, password)
        self.users[username] = user
        return user

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.authenticate(password):
            return user
        print("Invalid username or password.")
        return None


def save_data(store, filename="store_data.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(store, file)


def load_data(filename="store_data.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return Store()


def customer_menu(user, store):
    while True:
        print("\nWelcome To Customer Menu!")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Finalize Order")
        print("6. View Purchased Products")
        print("7. Rate a Product")
        print("8. Add Balance")
        print("9. View Balance")
        print("10. Logout")
        choice = input(">> ")

        if choice == "1":
            for product in store.products:
                print(
                    f"{product.name} - {product.seller} - ${product.price} - Stock: {product.stock} - Rating: {product.average_rating():.2f}")

        elif choice == "2":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            product = next((p for p in store.products if p.name == name), None)
            if product:
                user.add_to_cart(product, quantity)
            else:
                print("Product not found.")

        elif choice == "3":
            if not user.cart:
                print("Your cart is empty.")
            else:
                for p, qty in user.cart.items():
                    print(f"{p.name} - {qty} units")

        elif choice == "4":
            name = input("Enter product name to remove: ")
            user.remove_from_cart(name)

        elif choice == "5":
            user.finalize_order()

        elif choice == "6":
            if not user.purchased_products:
                print("You haven't purchased anything yet.")
            else:
                print("\nYour Purchased Products:")
                for p, qty in user.purchased_products.items():
                    print(f"{p.name} | {qty} units")

        elif choice == "7":
            name = input("Enter product name: ")
            rating = float(input("Enter rating (1.0,5.0): "))
            product = next((p for p in store.products if p.name == name), None)
            if product:
                user.rate_product(product, rating)
            else:
                print("Product not found.")

        elif choice == "8":
            amount = float(input("Enter amount: "))
            user.add_balance(amount)

        elif choice == "9":
            user.view_balance()

        elif choice == "10":
            break


def seller_menu(user, store):
    while True:
        print("\nWelcome To Seller Menu!")
        print("1. Add Product")
        print("2. View My Products")
        print("3. Update Product Details")
        print("4. Logout")
        choice = input(">> ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter initial stock: "))
            product = user.add_product(name, price, stock)
            store.products.append(product)
            print(f"Product {name} added successfully.")

        elif choice == "2":
            for p in user.products:
                print(
                    f"{p.name} | ${p.price} | Stock: {p.stock} | Rating: {p.average_rating():.2f}")

        elif choice == "3":
            name = input("Enter product name to update: ")
            user.update_product(name)

        elif choice == "4":
            break


def main():
    store = load_data()

    while True:
        print("\n---Welcome To The Online Store---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input(">> ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = store.login(username, password)
            if user:
                if isinstance(user, Customer):
                    customer_menu(user, store)
                else:
                    seller_menu(user, store)

        elif choice == "2":
            username = input("Choose a username: ")
            password = input("Choose a password (at least 8 characters): ")
            user_type = input("Enter 'customer' or 'seller': ")
            user = store.register_user(username, password, user_type)
            if user:
                print("Registration successful!")

        elif choice == "3":
            save_data(store)
            print("Have a nice day!")
            break


if __name__ == "__main__":
    main()
