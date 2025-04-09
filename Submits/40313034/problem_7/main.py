# from random import randint

# ---------- Main Code ----------

class Product:
    def __init__(self, name, seller, price, number):
        self.__name = name
        self.__seller = seller
        self.__price = price
        self.__number = number
        self.__rating = dict()

    def rate(self, username, rate):
        if username not in self.__rating:
            print(f"{username} has not buy this product yet!")
        else:
            self.__rating[username] = rate
            print(f"{username} rated successfully!")

    def add_user(self, username):
        self.__rating[username] = 0

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    def __str__(self):
        average = 0
        for x in self.__rating.values():
            average += x / len(self.__rating)

        return f"{self.__name} - Seller: {self.__seller} - Price: ${self.__price} - Stock: {self.__number} - Rating: {average}"

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__balance = 0
        self.__cart = list()

        print("Account created successfully!")

    def add_balance(self, money):
        self.__balance += money

        print(f"Added ${money} to {self.__username}\'s balance")

    def buy(self, product):
        self.__cart.append(product)
        print("Added to cart successfully.")

    def show_cart(self):
        print("Cart:")

        index = 0
        for product in self.__cart:
            index += 1
            print(str(index) + '.', product)

    def refresh_cart(self):
        for product in self.__cart:
            if product.number == 0:
                print("*", product, "is out of stock")
                self.__cart.remove(product)

    def remover(self, index):
        self.__cart.pop(index)
        print("Removed from cart successfully!")

    def order(self):
        self.refresh_cart()

        price = 0
        for product in self.__cart:
            price += product.price

        if price > self.__balance:
            print("Not enough money!")
        else:
            self.__balance -= price
            for product in self.__cart:
                product.number -= 1
                product.add_user(self.__username)
            self.__cart = list()

            print("Purchase successful!")

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def cart(self):
        return self.__cart

class System:
    def __init__(self):
        self.__users = dict()
        self.__products = [Product("Laptop", "tech_store", 1000, 5),
                           Product("Gaming Laptop", "game_world", 1500, 3)]
        self.__current_user = None

    def products_size(self):
        return len(self.__products)

    def cart_size(self):
        return len(self.__current_user.cart)

    def sign_up(self):
        username = input("Enter a username: ")
        while username in self.__users:
            username = input("Username was taken, type another: ")

        password = input("Enter a password (min 8 characters): ")
        while len(password) < 8:
            password = input("Enter another password (min 8 characters): ")

        self.__users[username] = User(username, password)

    def log_in(self):
        username = input("Enter a username: ")
        while username not in self.__users:
            username = input("Username is incorrect, type another: ")

        password = input("Enter a password (min 8 characters): ")
        while password != self.__users[username].password:
            password = input("Password is incorrect, try again: ")

        self.__current_user = self.__users[username]
        print("Login successful!")

    def log_out(self):
        self.__current_user = None
        print("Logout successful!")

    def refresh_products(self):
        for product in self.__products:
            if product.number == 0:
                self.__products.remove(product)

    def products(self):
        self.refresh_products()

        print("Products:")

        index = 0
        for product in self.__products:
            index += 1
            print(str(index) + '.', product)

    def search_by_name(self, name):
        self.refresh_products()

        print("Products:")

        index = 0
        for product in self.__products:
            if name in product.name:
                index += 1
                print(str(index) + '.', product)
                
    def search_by_price(self, l, r):
        self.refresh_products()

        print("Products:")

        index = 0
        for product in self.__products:
            if l <= product.price and product.price <= r:
                index += 1
                print(str(index) + '.', product)

    def cart(self):
        self.__current_user.show_cart()

    def rate(self, index, rating):
        index -= 1
        self.__products[index].rate(self.__current_user.username, rating)

    def remover(self, index):
        index -= 1
        self.__current_user.remover(index)

    def buy(self, index):
        index -= 1
        self.__current_user.buy(self.__products[index])

    def add_balance(self, money):
        self.__current_user.add_balance(money)

    def order(self):
        self.__current_user.order()
        self.refresh_products()

class UI:
    def __init__(self):
        self.__system = System()
        while 1:
            print("\nWelcome to Online Store!\n")
            print("1. Login")
            print("2. Sign Up")
            print("3. Exit\n")

            x = input(">> ")
            try:
                x = int(x)
            except:
                print("Invalid command")
                continue

            if x < 1 or x > 3:
                print("Invalid command")
                continue

            match x:
                case 1:
                    self.log_in()
                case 2:
                    self.sign_up()
                case 3:
                    self.exit()

    def main(self):
        while 1:
            print("\nMain Menu:")
            print("1. View Products")
            print("2. Search Products")
            print("3. Add to cart")
            print("4. View Cart")
            print("5. Remove from Cart")
            print("6. Finalize Order")
            print("7. Rate Purchased Products")
            print("8. Add Balance")
            print("9. Logout\n")

            x = input("\n>> ")
            try:
                x = int(x)
            except:
                print("Invalid command")
                continue

            if x < 1 or x > 9:
                print("Invalid command")
                continue

            match x:
                case 1:
                    self.products()
                case 2:
                    self.search()
                case 3:
                    self.buy()
                case 4:
                    self.cart()
                case 5:
                    self.remover()
                case 6:
                    self.order()
                case 7:
                    self.rate()
                case 8:
                    self.add_balance()
                case 9:
                    self.log_out()
                    return

    def log_in(self):
        print()
        self.__system.log_in()
        self.main()

    def sign_up(self):
        print()
        self.__system.sign_up()

    def log_out(self):
        print()
        self.__system.log_out()

    def products(self):
        print()
        self.__system.products()

    def search(self):
        print()
        print("Search by:")
        print("1. Name")
        print("2. Price Range")
        print("3. Category\n")

        while 1:
            x = input("\n>> ")

            try:
                x = int(x)
            except:
                print("Invalid command")
                continue

            if x < 0 or x > 3:
                print("Invalid command")
                continue

            match x:
                case 1:
                    name = input("Enter name: ")
                    self.__system.search_by_name(name)
                case 2:
                    l, r = map(int, input("Enter min and max price range: ").split())
                    self.__system.search_by_price(l, r)
                case 3:
                    category = input("Enter a category: ")
            break

    def buy(self):
        print()
        self.__system.products()

        while 1:
            x = input("\n>> ")

            try:
                x = int(x)
            except:
                print("Invalid command")
                continue

            if x < 0 or x > self.__system.products_size():
                print("Invalid command")
                continue

            if x != 0:
                self.__system.buy(x)
            break

    def cart(self):
        print()
        self.__system.cart()

    def remover(self):
        print()
        self.__system.cart()

        while 1:
            x = input("\n>> ")

            try:
                x = int(x)
            except:
                print("Invalid command")
                continue

            if x < 0 or x > self.__system.cart_size():
                print("Invalid command")
                continue

            if x != 0:
                self.__system.remover(x)
            break

    def order(self):
        print()
        self.__system.order()

    def rate(self):
        print()
        self.__system.products()

        while 1:
            x = input("\n>> ")

            try:
                x = int(x)
            except:
                print("Invalid command")
                continue

            if x < 0 or x > self.__system.products_size():
                print("Invalid command")
                continue

            if x == 0:
                break

            rating = 0
            while 1:
                y = input("Your Rate: ")

                try:
                    y = int(y)
                except:
                    print("Invalid Input!")
                    continue

                if y < 0 or y > 5:
                    print("Invalid Input!")
                    continue

                rating = y
                break

            self.__system.rate(x, rating)
            break

    def add_balance(self):
        print()

        while 1:
            x = input("Your amount: ")

            try:
                x = int(x)
            except:
                print("Invalid Input")
                continue

            self.__system.add_balance(x)
            break
    
    def exit(self):
        exit(0)

if __name__ == '__main__':
    ui = UI()

# ---------- End of Main Code ----------
