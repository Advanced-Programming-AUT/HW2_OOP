class User:
    def __init__(self, username, password, is_seller=False):
        self.username = username
        self.password = password
        self.is_seller = is_seller
        self.balance = 0
        self.cart = {}
        self.orders = []
        self.rated_products = set()

users = {}
products = {}

def signup():
    username = input("username : ")
    if username in users:
        print("   this username already exists!")
        return
    password = input(" password ( 8 characters at least ): ")
    if len(password) < 8:
        print(" password must not be less than 8 characters!")
        return
    is_seller = input("are you seller  ؟ (y/n): ") == "y"
    users[username] = User(username, password, is_seller)
    print(" registered succesfully!")

def login():
    username = input("username : ")
    password = input("password : ")
    user = users.get(username)
    if user and user.password == password:
        print(" loggin succesfully!")
        return user
    print(" invalid password or username!")
    return None

def add_product():
    name = input("products name : ")
    price = float(input("price: "))
    stock = int(input("stock: "))
    category = input("category: ")
    products[name] = {'price': price, 'stock': stock, 'category': category, 'ratings': []}
    print("product is added !")

def search_products():
    print("1. search based on name :  | 2.  range of price | 3. category")
    choice = input("> ")
    if choice == "1":
        name = input("name of product : ")
        results = {k: v for k, v in products.items() if name.lower() in k.lower()}
    elif choice == "2":
        min_price = float(input("min price : "))
        max_price = float(input("max price : "))
        results = {k: v for k, v in products.items() if min_price <= v['price'] <= max_price}
    elif choice == "3":
        category = input("category: ")
        results = {k: v for k, v in products.items() if v['category'].lower() == category.lower()}
    else:
        print("invalid input !")
        return
    show_products(results)

def show_products(products):
    for name, info in products.items():
        rating = sum(info['ratings']) / len(info['ratings']) if info['ratings'] else 0
        print(f"{name} - price: {info['price']} - stock: {info['stock']} - rate: {rating:.1f}")

def add_to_cart(user):
    name = input(" name of product: ")
    if name in products and products[name]['stock'] > 0:
        quantity = int(input("count: "))
        if quantity <= products[name]['stock']:
            user.cart[name] = user.cart.get(name, 0) + quantity
            products[name]['stock'] -= quantity
            print(" the product is added to your basket !")
        else:
            print("  there is no enough amount!")
    else:
        print("the product is not found !")

def checkout(user):
    if not user.cart:
        print("   your basket is empty!")
        return
    user.orders.append(user.cart.copy())
    user.cart.clear()
    print("  your shopping is final!")

def rate_product(user):
    if not user.orders:
        print("you havent registered any requests yet!")
        return
    name = input(" please enter the name of the product which you want to rate to : ")
    if name in user.orders[-1] and name not in user.rated_products:
        rating = int(input("rate (1 to 5): "))
        if 1 <= rating <= 5:
            products[name]['ratings'].append(rating)
            user.rated_products.add(name)
            print("your rate is registered!")
        else:
            print(" invalid rate!")
    else:
        print("you only can rate the products you have bought!")

def main():
    current_user = None
    while True:
        if not current_user:
            action = input("1. register | 2. loggin | 3. exit\n> ")
            if action == "1":
                signup()
            elif action == "2":
                current_user = login()
            elif action == "3":
                break
        else:
            if current_user.is_seller:
                action = input("1.  adding the product | 2. log out  \n> ")
                if action == "1":
                    add_product()
                elif action == "2":
                    current_user = None
            else:
                action = input("1.search products | 2.add to the basket | 3.show the basket | 4.removing from the basket | 5.final | 6.rating | 7.log out")
                if action == "1":
                    search_products()
                elif action == "2":
                    add_to_cart(current_user)
                elif action == "3":
                    print(current_user.cart)
                elif action == "4":
                    item = input("name of product : ")
                    if item in current_user.cart:
                        del current_user.cart[item]
                        print("  the product is deleted!")
                elif action == "5":
                    checkout(current_user)
                elif action == "6":
                    rate_product(current_user)
                elif action == "7":
                    current_user = None

if __name__ == "__main__":
    main()