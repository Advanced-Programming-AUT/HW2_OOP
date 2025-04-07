import pickle

class Product:
    def __init__(self,name,price,category,seller,in_stock,rate=0):
        self.category=category
        self.name=name
        self.price=price
        self.rate=rate
        self.ratings=list()
        self.seller=seller
        self.in_stock=in_stock
        self.customers=set()
        all_products.append(self)
    def buy_product(self,customer,number):
        self.in_stock -= number
        price = self.price * number
        self.customers.add(customer)
        customer.cash -= price

    def rate_this_product(self,customer,rate):
        if customer in self.customers:
            if customer in self.ratings:
                print('Can not rate this product twice')
            else:
                self.rate = (self.rate * self.ratings + rate)/ (int(len(self.ratings))+1)
                self.ratings.append(customer)
                customer.all_participated_ratings.append(self)
                print(f'{customer.name}rated :{rate} and new overall rating is {self.rate}')
    @staticmethod
    def view_all_products():
        for i in range(len(all_products)):
            print(f'{i}- name:{all_products[i].name},price:{all_products[i].price},category:{all_products[i].category},stock:{all_products[i].in_stock}')

    @staticmethod
    def search_for_product_category(category):
        show = []
        for item in all_products:
            if item.category == category:
                show.append(item)
        z = 1
        for it in show:
            print(f'{z}- {it.name},seller:{it.seller.name},stock:{it.in_stock},rating:{it.rate}')
            z += 1

    @staticmethod
    def search_for_product_price(min_pr, max_pr):
        show = []
        for t in all_products:
            if min_pr <= t.price <= max_pr:
                show.append(t)
        z = 1
        for it in show:
            print(f'{z}- {it.name},seller:{it.seller.name},stock:{it.in_stock},rating:{it.rate}')
            z += 1

    @staticmethod
    def search_for_product_name(name):
        show = []
        for item in all_products:
            if item.name == name:
                show.append(item)
        z = 1
        for it in show:
            print(f'{z}- {it.name},seller:{it.seller.name},stock:{it.in_stock},rating:{it.rate}')
            z += 1


class Customer:
    def __init__(self,name,username,password,cash):
        self.name=name
        self.cash=cash
        self.username=username
        self.password=password
        self.purchased_products=[]
        self.cart=[]
        self.all_participated_ratings=[]
        all_customers.append(self)
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,ur_name):
        f=0
        for item in all_customers:
            if item.username == ur_name:
                f=1
        for item in all_sellers:
            if item.username == ur_name:
                f=1
        if f == 1:
            print('invalid username, already exists')
        else:
            self._username = ur_name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,ur_name):
        if len(ur_name) < 8:
            print('this username has less than 8 characters!')
        else:
            self._name=ur_name

    def add_balance(self,amount):
        self.cash += amount
        print(f"added {amount} to customer {self.name}'s balance")
    def view_balance(self):
        print(f"there is {self.cash} Toomans in customer {self.name}'s card")

    def order_product(self,product:Product,number):
        if self.cash < product.price * number:
            print('Warning:not enough money to buy this item right now,please increase balance when finalizing order')
        flag = 0
        for item in self.cart:
            if item[0] == product:
                flag = 1
                z=item
                break
        if product.in_stock < number:
            print(f'there are only {product.in_stock} left in stock, would you like to add them all to your cart? 1-yes 2-no')
            x=input()
            if x=='1' or x=='yes':
                if flag ==0:
                    self.cart.append((product,product.in_stock))
                    product.customers.add(self)
                    print('added to cart successfully')
                elif flag == 1:
                    z[1] += number
                    self.cart.remove(z)
                    self.cart.append((z[0],z[1]))
                    print('added to cart successfully')
        else:
            if flag == 0:
                self.cart.append((product,number))
                product.customers.add(self)
                print('added to cart successfully')
            elif flag ==1:
                z[1] += number #adding to number of the product instead of registering same product twice
                self.cart.remove(z)
                self.cart.append((z[0], z[1]))
                print('added to cart successfully')
    def remove_from_cart(self,product:Product,number):
        for item in self.cart:
            if item[0] == product:
                item[1] -= number
            if item[1] <= 0:
                self.cart.remove((product,0))
    def view_cart(self):
        overall_price = 0
        c=1
        for item in self.cart:
            print(f'{c}- name:{item[0].name}, price:{item[0].price}')
            overall_price += item[0].price
        print(f'cart overall={overall_price}')
    def finalize_orders(self):
        overall=0
        for item in self.cart:
            overall += item[0].price * item[1]
        if overall > self.cash:
            print(f'not enough money, sum={overall}')
        else:
            for item in self.cart:
                item[0].buy_product(self,int(item[1]))
                self.purchased_products.append(item[0])
            print('finalized successfully')
    def rate_products(self,product:Product,rate):
            flag=0
            for item in self.cart:
                if item[0] == product:
                    flag=1
            if flag == 1 or (product in self.purchased_products):
                product.rate_this_product(self,rate)
            else:
                print('can not rate a product which is neither in cart nor purchased')
    def all_purchased(self):
        for item in self.purchased_products:
            print(f'name:{item.name}, price:{item.price}')


class Seller:
    def __init__(self,name,user_name,password):
        self.name=name
        self.username=user_name
        self.password=password
        self.related_products=list()
        all_sellers.append(self)
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,ur_name):
        f=0
        for item in all_customers:
            if item.username == ur_name:
                f=1
        for item in all_sellers:
            if item.username == ur_name:
                f=1
        if f == 1:
            print('invalid username, already exists')
        else:
            self._username = ur_name
    def add_new_product(self,prod_name,prod_price,prod_category,prod_stock):
                x = Product(prod_name,prod_price,prod_category,self,prod_stock)
                self.related_products.append(x)
    def refill_stock_old_product(self,prod_name,prod_price,prod_category,number):
        for item in self.related_products:
            if item.name==prod_name and item.category==prod_category and item.price == prod_price and item.seller == self:
                print('this product is indeed an old product/has been in stock before')
                item.in_stock += number
                print(f'{item.name} has {item.in_stock} items in stock now')
    def all_products(self):
        for i in range(len(self.related_products)):
            print(f'{i}- name:{self.related_products[i].name}, price:{self.related_products[i].price}')
def start():
        print(f'1-Login\n'
            f'2-Sign up\n'
            f'3-Exit\n')
        e = int(input())
        match e:
            case 1:
                u= input('user name')
                v= input('password')
                authentication_user(u,v)
            case 2:
                name=input('name:')
                print('for customer account enter 1 and for seller account enter 2')
                z = int(input())
                match z:
                    case 1:
                        ur_name=input('username')
                        password=input('password')
                        cash =int(input('cash:'))
                        Customer(name,ur_name,password,cash)
                        start()
                    case 2:
                        ur_name = input('username')
                        password = input('password')
                        Seller(name,ur_name,password)
                        start()
usr:Customer
def authentication_user(user_name,password):
        for item in all_customers:
            if item.username == user_name and item.password ==password:
                print(f'signed in as customer!, main menu:')
                customer_main_menu(item)
        for item in all_sellers:
            if item.username == user_name and item.password == password:
                print(f'signed in as seller!, main menu:')
                seller_main_menu(item)
def seller_main_menu(seller):
    print(f'1-add new product \n'
          f'2-Log out \n'
          f'3-show all products of this seller'
          f'4-Increase number of an product in stock')
    x=int(input())
    while(x != 2):
        match x:
            case 1:
                product_n=input('name of product')
                product_pr=input('price of product')
                product_cat=input('category of product')
                stock=input('in stock products of this kind')
                seller.add_new_product(product_n,product_pr,product_cat,stock)

            case 3:
                seller.all_products()
            case 4:
                product_n = input('name of product')
                product_pr = input('price of product')
                product_cat = input('category of product')
                number = input('number of products of this kind')
                seller.refill_stock_old_product(product_n,product_pr,product_cat,number)
        print(f'1-add product \n'
              f'2-Log out \n'
              f'3-show all products of this seller')
        x=int(input())
    if x ==2:
        start()

def customer_main_menu(customer):
        print(f'1-view products \n'
                f'2-add to cart \n'
                f'3-view cart \n'
                f'4-add balance \n'
                f'5-search products \n'
                f'6-remove from cart \n'
                f'7-finalize order \n'
                f'8-rate products \n'
                f'9-view all purchase history \n'
                f'10-Logout \n')
        x=int(input())
        while(x != 10):
            match(x):
                    case 1:
                        Product.view_all_products()
                    case 2:
                        Product.view_all_products()
                        print('which of the following products?/how many?')
                        y=input().split('/')
                        for i in range(len(all_products)):
                            if int(y[0]) == i:
                                customer.order_product(all_products[i],int(y[1]))
                                break
                    case 3:
                        customer.view_cart()
                        print('press 0 to go back to main menu')
                    case 4:
                        print('enter amount:')
                        y=int(input())
                        customer.add_balance(y)
                    case 5:
                        print(f'search by :1-name 2-category 3-price')
                        y=int(input())
                        match y:
                            case 1:
                                z = input('enter name:')
                                Product.search_for_product_name(z)
                            case 2:
                                z = input('enter category:')
                                Product.search_for_product_category(z)
                            case 3:
                                z1 = int(input('enter price max:'))
                                z2 = int(input('enter price min:'))
                                Product.search_for_product_price(z1,z2)

                    case 6:
                        Product.view_all_products()
                        z = int(input('enter product index'))
                        w=int(input('how many of those products are to be removed?'))
                        customer.remove_from_cart(all_products[z],w)

                    case 7:
                        customer.finalize_orders()

                    case 8:
                        Product.view_all_products()
                        z = int(input('enter product index'))
                        r = int(input('rate:'))
                        customer.rate_products(all_products[z],r)

                    case 9:
                        customer.all_purchased()
            x=int(input())
        if x == 10:
                    start()

def save_data(datas):

    with open('data.pkl','wb') as file:
        pickle.dump(datas,file)
    print('saved')
def load_data():
    try:
        with open('data.pkl','rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        all_sellers=[]
        all_customers=[]
        all_products=[]
        return None
all_customers=[]
all_products=[]
all_sellers=[]
x4=load_data()
for item in x4[0]:
    all_products.append(item)
for j in x4[1]:
    all_sellers.append(j)
for k in x4[2]:
    all_sellers.append(k)
start()
data=[all_products,all_customers,all_sellers]
save_data(data)