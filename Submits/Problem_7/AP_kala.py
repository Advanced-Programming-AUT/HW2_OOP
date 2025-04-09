from abc import ABC, abstractmethod
import pickle
import re


class User(ABC):
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password

    @property
    def name(self):
        return self.__user_name

    @name.setter
    def name(self, name):
        self.__user_name = name


class Client(User):
    def __init__(self, user_name, password):
        super().__init__(user_name, password)
        self._balance = 0
        self._shopping_card = []
        self._history = []

    def add_shopping_card(self, product, quantity):
        if product.stock >= quantity:
            self._shopping_card.append((product, quantity))
            product.stock -= quantity
            print(f"{quantity} number of {product.name} added to shopping card\n")
        else:
            print(f"there is not {quantity} number of {product.name}\n")

    def view_shopping_card(self):
        print("\nYour shopping card:" if self._shopping_card else "\nYour shopping card is empty\n")
        for card in self._shopping_card:
            print(f"{card[1]}X {card[0].name}\n")

    def remove_from_shopping_card(self):
        self.view_shopping_card()
        print(f"enter the product ID to remove\n")
        try:
            id_to_remove = int(input(">> "))
            for card in self._shopping_card:
                if card[0].id == id_to_remove:
                    card[0].stock += card[1]
                    self._shopping_card.remove(card)
                    print(f"{card[0].name} deleted\n")
                    return
        except ValueError:
            print("invalid input\n")
            return
        print("No such product found\n")

    def finalize_shopping_card(self):
        self.view_shopping_card()
        total_price = 0
        for card in self._shopping_card:
            total_price = card[0].price * card[1]
        response = input(f"Total price: {total_price}\nYour balance{self._balance}\n"
                         f"Do you want to continue? [y/any thing]")
        if response.lower() == 'y':
            if self._balance < total_price:
                response = input("not enough money\nDo you want to add balance? [y/any thing]")
                if response.lower() == 'y':
                    self.add_balance()
                    self.finalize_shopping_card()
                else:
                    return
            else:
                confirm = input("confirm the buying [y/any thing]")
                if confirm.lower() == 'y':
                    self._balance -= total_price
                    self._history.append(self._shopping_card)
                    self._shopping_card.clear()

                else:
                    return
        else:
            return

    def add_balance(self):
        amount = input("enter the amount\n")
        self._balance += int(amount)

    def return_product(self, id_product):
        for card in self._shopping_card:
            if card[0].id == id_product:
                return card[0]
        print("No such product found in your shopping card\n")
        return None


class Seller(User):
    def __init__(self, user_name, password):
        super().__init__(user_name, password)
        self._products = []

    def add_product(self):
        print("too add product fill asked parts\n")
        name = input("enter product name: \n")
        try:
            price = int(input("enter product price: \n"))
        except ValueError:
            print("invalid input\n")
            return
        try:
            stock = int(input("enter product quantity: \n"))
        except ValueError:
            print("invalid input\n")
            return
        category = input("enter product category: \n")
        product = Product(name, self.name, price, stock, category)
        products.append(product)
        self._products.append(product)

    def view_products(self):
        print("\nAll products:\n" if self._products else "\nThere is no product yet\n")
        number = 0
        for product in self._products:
            print(f"{number}. ", end="")
            product.show_details()
            number += 1

    def delete_product(self):
        self.view_products()
        print(f"enter the product ID to remove\n")
        try:
            id_to_remove = int(input(">> "))
            for product in self._products:
                if product.id == id_to_remove:
                    self._products.remove(product)
                    print(f"\n{product.name} deleted\n")
                    return
        except ValueError:
            print("\ninvalid input\n")
            return
        print("\nNo such product found\n")

    def add_stock(self):
        self.view_products()
        print(f"enter the product ID to change stock\n")
        try:
            id_to_add = int(input(">> "))
            for product in self._products:
                if product.id == id_to_add:
                    try:
                        print("\nenter product new stock: \n")
                        amount = int(input(">> "))
                        product.stock = amount
                        print(f"\n{product.name} new stock is {product.stock}\n")
                        return
                    except ValueError:
                        print("\ninvalid input\n")
                        return
        except ValueError:
            print("\ninvalid input\n")
            return
        print("\nNo such product found\n")


class Product:
    ids = 1000

    def __init__(self, name, seller, price, stock, category):
        self.name = name
        self.seller = seller
        self.price = price
        self.stock = stock
        self.category = category
        self.rating = None
        self.id = Product.ids
        Product.ids += 1
        self.users_rated = {}

    def set_rating(self, user):
        if user.name in self.users_rated:
            print(f"you have already rated {self.name}\n")
        else:
            rating = None
            while True:
                print(f"Enter your rating for {self.name} (0-5)\n")
                rating = int(input(">> "))
                if 0 <= rating <= 5:
                    break
                else:
                    print("Invalid rating value\n")
            self.users_rated[user.name] = rating
            rates = 0
            for rate in self.users_rated.values():
                rates += rate
            self.rating = rates / len(self.users_rated)

    def show_details(self):
        print(
            f'{self.name} - Seller: {self.seller} - Price: ${self.price} - Stock: {self.stock}'
            f' - Rating: {self.rating if self.rating else "there is no rating for this product yet"} - ID: {self.id}')


def list_based_on_name(name):
    number = 1
    for product in products:
        if product.name == name:
            print(f"{number}. ", end="")
            product.show_details()
            number += 1


def list_based_on_price(price_range):
    number = 1
    for product in products:
        if price_range[0] <= product.price <= price_range[1]:
            print(f"{number}. ", end="")
            product.show_details()
            number += 1


def list_based_on_category(category):
    number = 1
    for product in products:
        if category == product.category:
            print(f"{number}. ", end="")
            product.show_details()
            number += 1


def login_main():
    user_name = input('\nEnter your username: ')
    password = input('Enter your password: ')
    if user_name not in user_name_password_dict:
        print("account does not exist\n")
        return False
    if password == user_name_password_dict[user_name][0]:
        is_seller = user_name_password_dict[user_name][1]
        if is_seller:
            for seller in sellers:
                if seller.name == user_name:
                    main_user['user'] = seller
                    seller_menu()
                    return False
            main_user['user'] = Seller(user_name, password)
            seller_menu()
            return False
        else:
            for client in clients:
                if client.name == user_name:
                    main_user['client'] = client
                    return True
            main_user['user'] = Client(user_name, password)
            return True

    print("password is not correct\n")
    return False


def sign_up_main():
    print("sign up as 1.Customer 2.Seller:\n")
    selection = input(">> ")
    is_seller = selection == '2'
    while selection not in ['1', '2']:
        print("Invalid input\n")
        selection = input(">> ")
        is_seller = selection == '2'
    user_name = input('\nEnter a username: ')
    password = input('Enter a password (min 8 characters): ')
    while not re.match(r'^[a-zA-Z0-9_]', user_name) or len(password) < 8:
        try_again = input('user name must contain [a-z,A-Z,0-9,_] or Password must be at least 8 characters.\n'
                          '1. try again\n2. cancel\n\n>>')
        if try_again == '1':
            user_name = input('\nEnter a username: ')
            password = input('Enter a password (min 8 characters): ')
        elif try_again == '2':
            return
    if user_name not in user_name_password_dict:
        user_name_password_dict[user_name] = (password, is_seller)
        print("Account created successfully!\n")
        return
    print("Account already exists\n")


def seller_menu():
    command = 1
    while command != 5:
        print(
            "\nMain Menu:\n1. Add New Product\n2. View Your Products\n3. Remove Product\n4. Edit product Stock\n5. Logout\n")
        command = input(">> ")
        match command:
            case '1':
                main_user['user'].add_product()
            case '2':
                main_user['user'].view_products()
            case '3':
                main_user['user'].delete_product()
            case '4':
                main_user['user'].add_stock()
            case '5':
                for seller in sellers:
                    if main_user['user'].name == seller.name:
                        sellers.remove(seller)
                sellers.append(main_user['user'])
                break


def view_products():
    number = 1
    for product in products:
        print(f"{number}. ", end="")
        product.show_details()
        number += 1


def main_menu():
    command = 1
    while command != 9:
        print("\nMain Menu:\n1. View Products\n2. Search Product\n3. Add to Cart\n"
              "4. View Cart\n""5. Remove from Cart\n6. Finalize Order\n"
              "7. Rate Purchased Products\n8. Add Balance\n9. Logout\n")
        command = input(">> ")
        match command:
            case '1':
                view_products()
            case '2':
                print("Search by:\n1. Name\n2. Price Range\n3. Category(s)\n")
                search_by = input(">> ")
                match search_by:
                    case '1':
                        name = input("Enter product name: ")
                        list_based_on_name(name)
                    case '2':
                        price_range = map(int, input("Enter price range (e.g. 10 20): ").split())
                        list_based_on_price(list(price_range))
                    case '3':
                        category = input("Enter category: ")
                        list_based_on_category(category)
            case '3':
                view_products()
                print("Enter the product ID\n")
                try:
                    product_id = int(input(">> "))
                    print("Enter the number of item you want\n")
                    try:
                        quantity = int(input(">> "))
                        for product in products:
                            if product.id == product_id:
                                main_user['user'].add_shopping_card(product, quantity)
                    except ValueError:
                        print("Invalid input\n")
                except ValueError:
                    print("Invalid input\n")
            case '4':
                main_user['user'].view_shopping_card()
            case '5':
                main_user['user'].remove_from_shopping_card()
            case '6':
                main_user['user'].finalize_shopping_card()
            case '7':
                view_products()
                main_user['user'].view_shopping_card()
                print("Enter product ID you want to rate\n ")
                try:
                    id_product = int(input(">> "))
                    product = main_user['user'].return_product(id_product)
                    if product:
                        product.set_rating(main_user['user'])
                except ValueError:
                    print("Invalid input\n")

            case '8':
                main_user['user'].add_balance()
            case '9':
                for client in clients:
                    if main_user['user'].name == client.name:
                        clients.remove(client)
                clients.append(main_user['user'])
                return


main_user = {}  # user:class object
products = []
user_name_password_dict = {}
clients = []
sellers = []

try:
    with open('information_database.txt', 'rb') as database_file:
        database = pickle.load(database_file)
        user_name_password_dict = database['user_name_password_dict']
        products = database['products']
        clients = database['clients']
        sellers = database['sellers']
        Product.ids = database['product_ids']
except FileNotFoundError:
    user_name_password_dict = {}
    products = []
    clients = []
    sellers = []


def main():
    command = 1
    while command != 3:
        print("Welcome to the Online Store!\n")
        print("1. Login\n2. Sign Up\n3. Exit\n")
        try:
            command = int(input(">> "))
        except ValueError:
            print("Invalid input\n")
        if command == 1:
            if login_main():
                main_menu()

        elif command == 2:
            sign_up_main()


if __name__ == '__main__':
    main()

with open('information_database.txt', 'wb') as database_file:
    database = {'user_name_password_dict': user_name_password_dict, 'products': products, 'clients': clients,
                'sellers': sellers, 'product_ids': Product.ids}
    pickle.dump(database, database_file)
