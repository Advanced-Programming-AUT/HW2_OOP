
class User:
    def __init__(self, username, password, is_seller=False):
        self.username = username
        self.password = password
        self.is_seller = is_seller
        self.balance = 0 if not is_seller else None
        self.cart = Cart() if not is_seller else None

    def add_balance(self, amount):
        if not self.is_seller:
            self.balance += amount


class Product:
    def __init__(self, name, price, stock, category, seller):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.seller = seller
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)


class Cart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity):
        if product.name in self.items:
            self.items[product.name] += quantity
        else:
            self.items[product.name] = quantity

    def remove_from_cart(self, product_name):
        if product_name in self.items:
            del self.items[product_name]


class Store:
    def __init__(self):
        self.users = {}
        self.products = []

    def signup(self, username, password, is_seller):
        if username in self.users:
            return "Username already exists!"
        if len(password) < 8:
            return "Password must be at least 8 characters long."
        self.users[username] = User(username, password, is_seller)
        return "Account created successfully!"

    def login(self, username, password):
        if username not in self.users:
            return None, "Username does not exist."
        user = self.users[username]
        if user.password != password:
            return None, "Incorrect password."
        return user, "Login successful!"

    def add_product(self, seller, name, price, stock, category):
        product = Product(name, price, stock, category, seller)
        self.products.append(product)

    def search_products(self, name=None, price_range=None, category=None):
        results = self.products
        if name:
            results = [p for p in results if name.lower() in p.name.lower()]
        if price_range:
            results = [p for p in results if price_range[0] <= p.price <= price_range[1]]
        if category:
            results = [p for p in results if category.lower() in p.category.lower()]
        return results

    def finalize_order(self, user):
        total_cost = 0
        for product_name, quantity in user.cart.items.items():
            product = next((p for p in self.products if p.name == product_name), None)
            if product and quantity <= product.stock:
                total_cost += product.price * quantity
                product.stock -= quantity
            else:
                return f"Error: Not enough stock for {product_name}."
        if user.balance < total_cost:
            return "Insufficient balance."
        user.balance -= total_cost
        user.cart.items.clear()
        return "Order finalized successfully!"



# شی گراییشو پیاده سازی کردم