import pickle
from abc import ABC, abstractclassmethod
dict_of_all_kala = {'electronic': [], 'books_and_stationery': [], 'clothing': [], 'helth_and_beauty': [],'home_and_sofa': [],'sport': []}
list_of_all_kala = []
list_of_all_user = []
list_of_all_seller = []
class Info(ABC):
    @abstractclassmethod
    def get_user_name(self):
        pass
    @abstractclassmethod
    def get_password(self):
        pass
    
class User(Info):
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password
        self.__balance = 0
        self.__kala_rating = []
        list_of_all_user.append(self)
        self.__sabad_kharid = []
        self.__finalize_sabad_kharid = []
        print("Account created successfully!")
    def get_user_name(self):
        return self.__user_name
    def get_password(self):
        return self.__password
    def get_balance(self):
        return self.__balance
    def add_balance(self, amount_money):
        self.__balance += int(amount_money)
    def decrease_balance(self, amount_money):
        self.__balance -= int(amount_money)
    def delet_kala(self):
        name_kala = input("Enter your Name of Kala: ")
        for kala_and_stock in self.__sabad_kharid:
            if name_kala == kala_and_stock[0].get_name():
                self.__sabad_kharid.remove(kala_and_stock)
                kala_and_stock[0].add_stock(kala_and_stock[1])
                print("The Kala Has Been Delete From Sabad\n")
                break
        
    def add_to_sabad(self):
        name_kala = input("Enter your Name of Kala: ") 
        count = 0
        for kala in list_of_all_kala:
            if kala.get_name() == name_kala:
                count = 1
                count_stock = int(input("Enter Count of Stock: "))
                if int(count_stock) > kala.get_stock():
                    print("The Stock Was Not Enough!\n")
                else:
                    self.__sabad_kharid.append([kala, count_stock])
                    kala.decrease_stock(count_stock)
                    print(f"The Kala Add to Sabad Per {count_stock}\n")
        if count == 0:
            print("Your Kala not Exist!\n")
        
    def view_sabad_kharid(self):
        for kala_and_stock in self.__sabad_kharid:
            kala = kala_and_stock[0]
            stock = kala_and_stock[1]
            print(kala.show_details() + f" / Stock: {stock}")
    def finalize_sabad(self):
        sum_of_price = 0
        for kala_stock in user.__sabad_kharid:
            sum_of_price += kala_stock[0].get_price() * int(kala_stock[1])
        if sum_of_price <= int(user.get_balance()):
            for kala in self.__sabad_kharid:
                self.__finalize_sabad_kharid.append(kala)
            self.__sabad_kharid.clear()
            self.__balance -= int(sum_of_price)
            print("The Sabad Kharid Has Been Finalized\n")
        else:
            print("The Balance Not Enough for Finalize Sabad Kharid\n")
    
    def scoring(self):
        name = input("Enter Your Name of Kala: ")
        count = 0
        self.__list_all_kala_for_user = []
        for kala in user.__sabad_kharid:
            self.__list_all_kala_for_user.append(kala)
        for kala in user.__finalize_sabad_kharid:
            self.__list_all_kala_for_user.append(kala)
        for kala in user.__list_all_kala_for_user:
            if kala[0].get_name() == name:
                count = 1
                kala = kala[0]
                break
        if count:
            score = int(input("Enter Your Rate Between 0 To 5: "))
            if score == 0 or score == 1 or score == 2 or score == 3 or score == 4 or score == 5:
                rate = score
                if kala not in self.__kala_rating:
                    self.__kala_rating.append(kala)
                    kala.rating(rate)
                else:
                    print("Just Once Rating\n")
            else:
                print("Please Enter Between 0 TO 5")
        else:
            print("Rating Just For Kalas in Sabad Kharid!\n")
        
class Kala:
    def __init__(self, name, price, seller, stock, type):
        self.__name = name
        self.__price = int(price)
        self.__seller = seller
        self.__stock = int(stock)
        self.__type = type
        list_of_all_kala.append(self)
        self.__count_scoring = 0
        self.__sum_of_score = 0
        self.__score = 0
    def get_name(self):
        return self.__name
    def add_stock(self, amount):
        self.__stock += int(amount)
    def decrease_stock(self, amount):
        self.__stock -= int(amount)
    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock
    def get_type(self):
        return self.__type
    def add_to_all_kala(self):
        dict_of_all_kala[self.type].append(self)
        list_of_all_kala.append(self)
    def show_details(self):
        return f"- Name: {self.__name} / Type: {self.__type} / Name of Seller: {self.__seller.get_user_name()} / Price: {self.__price}$ / Rating: {self.__score}"
    def rating(self, rate): 
        self.__sum_of_score += int(rate)
        self.__count_scoring += 1
        self.__score = self.__sum_of_score / self.__count_scoring
        print("Thanks For Rating!")
        
class Seller(Info):
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password
        list_of_all_seller.append(self)
        self.__list_of_seller_kala = []
    def add_kala(self, kala):
        self.__list_of_seller_kala.append(kala)
    def increase_stock(self):
        flag = 1
        name_of_kala = input("Your Name of Kala: ")
        count_increase = int(input("Count Increasing: "))
        for kala in self.__list_of_seller_kala:
            if kala.get_name() == name_of_kala:
                kala.add_stock(count_increase) 
                flag = 0
                print("Increasing stock has been successfully!\n")
        if flag:
            print("The Kala Not Found\n")
    def get_user_name(self):
        return self.__user_name
    def get_password(self):
        return self.__password

try:
  with open("list of all information.pkl", "rb") as file:
    list_of_all_kala, dict_of_all_kala, list_of_all_user, list_of_all_seller = pickle.load(file)    
except :
    with open("list of all information.pkl", "wb") as file:
        pickle.dump((list_of_all_kala, dict_of_all_kala, list_of_all_user, list_of_all_seller), file)
        
print("Welcome to the Online Store!")
order = ""
while order != '+3':
    print("\n1. Login\n2. Sign Up\n+3. Exit\n")
    order = input()
    if order == "1":
        print("Seller > 1\nUser > 2")
        order = input()
        if order == "1":
            condition = 0
            count = 0
            while condition != 1:
                if count == 0:
                    user_name = input("Enter your User Name:")
                    password = input("Enter your Password:")
                if count > 0:
                    print("The User Name or Password is Wrong")
                    user_name = input("Enter your User Name:")
                    password = input("Enter your Password:")
                for seller in list_of_all_seller :
                    if seller.get_user_name() == user_name and seller.get_password() == password:
                        seller = seller 
                        condition = 1
                        break
                count += 1
            print("Login Successfully!\n")
            order = ""
            print("1. > Add Kala")
            print("2. > Increace Stock")
            print("3. > Logout\n")
            while order != "3":
                order = input()
                if order == "1":
                    name = input("Name of Kala: ")
                    type = input("Type of Kala: ")
                    price = input("Price of Kala: ")
                    stock = input("Stock of Kala: ")
                    kala = Kala(name, price, seller, stock, type)
                    seller.add_kala(kala)
                    print("Kala added successfully!\n")
                    print("1. > Add Kala")
                    print("2. > Increace Stock")
                    print("3. > Logout\n")
                if order == "2":
                    seller.increase_stock()
                    print("1. > Add Kala")
                    print("2. > Increace Stock")
                    print("3. > Logout\n")   
        if order == "2":
              condition = 0
              count = 0
              while condition != 1:
                if count == 0:
                    user_name = input("Enter your User Name:")
                    password = input("Enter your Password:")
                if count > 0:
                    print("The User Name or Password is Wrong")
                    user_name = input("Enter your User Name:")
                    password = input("Enter your Password:")
                for user in list_of_all_user :
                    if user.get_user_name() == user_name and user.get_password() == password:
                        user = user 
                        condition = 1
                        break
                count += 1
              print("Login Successfully!\n")
              print("1. > View Product")
              print("2. > Search Product")
              print("3. > Add to Sabad Kharid")
              print("4. > View Sabad Kharid")
              print("5. > Remove from Sabad Kharid")
              print("6. > Finalize Sabad-Kharid")
              print("7. > Rate Purchased Product")
              print("8. > Add Balance")
              print("9. > Logout")   
              order = ""
              while order != "9":
                  order = input()
                  if order == "1":
                      for kala in list_of_all_kala:
                          print(kala.show_details() + f' / Stock: {kala.get_stock()}')
                           
                  if order == "2":
                      print("Searching By:")
                      print("1 > Name\n2 > Price Range\n3 > Category ")
                      order = input()
                      if order == "1":
                          name = input("Enter Name: \n")
                          print("Results: ")
                          for kala in list_of_all_kala:
                              if kala.get_name() == name:
                                  print(kala.show_details() + f' / Stock: {kala.get_stock()}')
                      if order == "2":
                          start_range, end_range = map(int,input("Enter your price range: ").split()) 
                          print("Results: ")
                          for kala in list_of_all_kala:
                              if kala.get_price() >= start_range and kala.get_price() <= end_range:
                                  print(kala.show_details() + f' / Stock: {kala.get_stock()}')
                      if order == "3":
                          type = input("Enter your Category: \n")
                          order = ""
                          print("Results: ")
                          for kala in list_of_all_kala:
                              if kala.get_type() == type:
                                  print(kala.show_details() + f' / Stock: {kala.get_stock()}')
                          order = ""     
                  if order == "3":
                      user.add_to_sabad()
                  if order == "4":
                      print("Sabad Kharid: ")
                      user.view_sabad_kharid()
                  if order == "5":
                      user.delet_kala()
                  if order == "6":
                      user.finalize_sabad()
                       
                  if order == "7":
                      user.scoring()
                          
                  if order == "8":
                       balance = int(input("Enter Your Balance: "))
                       user.add_balance(balance)
                       print("Add to Balance Successfully!\n")
                     
    if order =="2":
        print("1. > Seller\n2. > User")
        order = input()
        if  order == '2':
            print("Enter a User Name:")
            user_name = input()
            print("Enter a Password (min 8 characters):")
            password = input()
            while len(password) < 8:
                print("Please Enter More Than 8 Characters:")
                password = input()
            user = User(user_name, password)
        if order == "1":
            print("Enter a User Name:")
            user_name = input()
            print("Enter a Password (min 8 characters):")
            password = input()
            while len(password) < 8:
                print("Please Enter More Than 8 Characters:")
                password = input()
            seller = Seller(user_name, password)
            
    if order == "+3":
        break


with open("list of all information.pkl", "wb") as file:
    pickle.dump((list_of_all_kala, dict_of_all_kala, list_of_all_user, list_of_all_seller), file)

