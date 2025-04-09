class Product(object):
    def __init__(self, name, price, stock, category, seller):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.seller = seller
        self.ratings = []

    def rate(self, score):
        if score >= 1 and score <= 5:
            self.ratings.append(score)

    def average_rating(self):
        if len(self.ratings) == 0:
            return 0
        return round(sum(self.ratings) / len(self.ratings), 1)

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Buyer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.balance = 0
        self.cart = []
        self.rated_products = []

    def add_balance(self, amount):
        self.balance += amount

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append([product, quantity])
            print("Added to cart.")
        else:
            print("Not enough stock.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Cart is empty.")
        else:
            for item in self.cart:
                print(f"{item[0].name} - {item[1]} pcs - Total: {item[0].price * item[1]}")

    def remove_from_cart(self, product_name):
        new_cart = []
        removed = False
        for item in self.cart:
            if item[0].name != product_name:
                new_cart.append(item)
            else:
                removed = True
        self.cart = new_cart
        if removed:
            print("Item removed.")
        else:
            print("Item not found.")

    def finalize_order(self):
        total = 0
        for item in self.cart:
            total += item[0].price * item[1]
        if total > self.balance:
            print("Insufficient balance.")
            return
        for item in self.cart:
            item[0].stock -= item[1]
        self.balance -= total
        print(f"Order complete. Total: {total}")
        self.cart = []

    def rate_product(self, product, score):
        if product.name in self.rated_products:
            print("Already rated.")
            return
        in_cart = False
        for item in self.cart:
            if item[0].name == product.name:
                in_cart = True
        if in_cart:
            product.rate(score)
            self.rated_products.append(product.name)
            print("Rating submitted.")
        else:
            print("You haven't added this product to cart.")

class Seller(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = []

    def add_product(self, product_list, name, price, stock, category):
        p = Product(name, price, stock, category, self.username)
        product_list.append(p)
        self.products.append(p)
        print("Product added.")

class Store(object):
    def __init__(self):
        self.users = []
        self.products = []

    def sign_up(self, role, username, password):
        for user in self.users:
            if user.username == username:
                print("Username already exists.")
                return None
        if len(password) < 8:
            print("Password too short.")
            return None
        if role == "buyer":
            new_user = Buyer(username, password)
        else:
            new_user = Seller(username, password)
        self.users.append(new_user)
        print(f"{role.capitalize()} registered.")
        return new_user

    def login(self, username, password):
        for user in self.users:
            if (user.username == username and
                user.password == password):
                print("Login successful.")
                return user
        print("Login failed.")
        return None

    def search_by_name(self, name):
        results = []
        for p in self.products:
            if name.lower() in p.name.lower():
                results.append(p)
        return results

    def search_by_category(self, category):
        result = []
        for p in self.products:
            if p.category.lower() == category.lower():
                result.append(p)
        return result

    def search_by_price(self, min_price, max_price):
        result = []
        for p in self.products:
            if min_price <= p.price <= max_price:
                result.append(p)
        return result

    def show_products(self, product_list):
        if not product_list:
            print("No products found.")
        for p in product_list:
            print(f"{p.name} - {p.price} - Stock: {p.stock} - Category: {p.category} - Rating: {p.average_rating()} - Seller: {p.seller}")
