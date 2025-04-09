import pickle
import os
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.orders = []
    
    @abstractmethod
    def get_menu(self):
        pass

class Product:
    def __init__(self, name, category, price, stock, seller):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.seller = seller
        self.ratings = []
        self.rating_average = 0.0
    def add_rating(self, rating, username):
        for r in self.ratings:
            if r['username'] == username:
                return False
        
        self.ratings.append({'username': username, 'rating': rating})
        self._update_average()
        return True
    
    def _update_average(self):
        if not self.ratings:
            self.rating_average = 0.0
            return
        
        total = sum(r['rating'] for r in self.ratings)
        self.rating_average = total / len(self.ratings)




class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.cart = []
    
    def get_menu(self):
        return [
            "View Products",
            "Search Product",
            "Add to Cart",
            "View Cart",
            "Remove from Cart",
            "Finalize Order",
            "Rate Purchased Products",
            "Add Balance",
            "Logout"
        ]
    
    def add_to_cart(self, product, quantity):
        if quantity <= product.stock:
            self.cart.append({'product': product, 'quantity': quantity})
            return True
        return False
    
    def remove_from_cart(self, index):
        if 0 <= index < len(self.cart):
            self.cart.pop(index)
            return True
        return False
    
    def finalize_order(self):
        total_cost = sum(item['product'].price * item['quantity'] for item in self.cart)
        
        if self.balance < total_cost:
            return False, "Insufficient balance"
        

        for item in self.cart:
            if item['quantity'] > item['product'].stock:
                return False, f"Not enough stock for {item['product'].name}"
        
        self.balance -= total_cost
        order_items = []
        
        for item in self.cart:
            product = item['product']
            quantity = item['quantity']
            
            product.stock -= quantity
            
            order_items.append({
                'product_name': product.name,
                'quantity': quantity,
                'price': product.price,
                'seller': product.seller
            })
        
        self.orders.append({'items': order_items, 'total': total_cost})
        self.cart = []
        return True, "Order finalized successfully"





class Seller(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.products = []
    
    def get_menu(self):
        return [
            "Add Product",
            "Update Product Stock",
            "View My Products",
            "Add Balance",
            "Logout"
        ]
    
    def add_product(self, name, category, price, initial_stock):
        product = Product(name, category, price, initial_stock, self.username)
        self.products.append(product)
        return product
    
    def update_product_stock(self, product_name, additional_stock):
        for product in self.products:
            if product.name == product_name:
                product.stock += additional_stock
                return True
        return False




class OnlineStore:
    def __init__(self):
        self.users = {}
        self.products = []
        self.categories = set()
        self.current_user = None
        self.load_data()
    
    def load_data(self):
        if os.path.exists('store_data.pkl'):
            with open('store_data.pkl', 'rb') as f:
                data = pickle.load(f)
                self.users = data.get('users', {})
                self.products = data.get('products', [])
                self.categories = data.get('categories', set())
    
    def save_data(self):
        data = {
            'users': self.users,
            'products': self.products,
            'categories': self.categories
        }
        with open('store_data.pkl', 'wb') as f:
            pickle.dump(data, f)
    
    def signup(self, username, password, is_seller=False):
        if username in self.users:
            return False, "Username already exists"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        
        user_class = Seller if is_seller else RegularUser
        self.users[username] = user_class(username, password)
        self.save_data()
        return True, "Account created successfully"
    
    def login(self, username, password):
        if username not in self.users:
            return False, "Username not found"
        
        if self.users[username].password != password:
            return False, "Incorrect password"
        
        self.current_user = self.users[username]
        return True, "Login successful"
    
    def logout(self):
        self.current_user = None
        return True, "Logged out successfully"
    
    def add_product(self, name, category, price, initial_stock):
        if not isinstance(self.current_user, Seller):
            return False, "Only sellers can add products"
        
        product = self.current_user.add_product(name, category, price, initial_stock)
        self.products.append(product)
        self.categories.add(category)
        self.save_data()
        return True, "Product added successfully"
    
    def update_product_stock(self, product_name, additional_stock):
        if not isinstance(self.current_user, Seller):
            return False, "Only sellers can update stock"
        
        success = self.current_user.update_product_stock(product_name, additional_stock)
        if success:
            self.save_data()
            return True, "Stock updated successfully"
        return False, "Product not found"
    def search_products(self, search_type, query):
        results = []
        
        if search_type == "name":
            for p in self.products:
                if query.lower() in p.name.lower():
                    results.append(p)
        elif search_type == "category":
            for p in self.products:
                if p.category.lower() == query.lower():
                    results.append(p)
        elif search_type == "price_range":
            min_price, max_price = map(float, query.split('-'))
            for p in self.products:
                if min_price <= p.price <= max_price:
                    results.append(p)
        
        return results
    
    def add_to_cart(self, product, quantity):
        if not isinstance(self.current_user, RegularUser):
            return False, "Only regular users can add to cart"
        
        success = self.current_user.add_to_cart(product, quantity)
        if success:
            return True, "Product added to cart"
        return False, "Quantity exceeds available stock"
    
    def remove_from_cart(self, index):
        if not isinstance(self.current_user, RegularUser):
            return False, "Only regular users can modify cart"
        
        success = self.current_user.remove_from_cart(index)
        if success:
            return True, "Product removed from cart"
        return False, "Invalid cart index"
    
    def finalize_order(self):
        if not isinstance(self.current_user, RegularUser):
            return False, "Only regular users can finalize orders"
        
        success, message = self.current_user.finalize_order()
        if success:
            self.save_data()
        return success, message
    
    def rate_product(self, product_name, rating):
        if not isinstance(self.current_user, RegularUser):
            return False, "Only regular users can rate products"
        
        product_found = False
        for order in self.current_user.orders:
            for item in order['items']:
                if item['product_name'] == product_name:
                    product_found = True
                    break
            if product_found:
                break
        
        if not product_found:
            return False, "You haven't purchased this product"
        
        for product in self.products:
            if product.name == product_name:
                success = product.add_rating(rating, self.current_user.username)
                if success:
                    self.save_data()
                    return True, "Rating added successfully"
                return False, "You've already rated this product"
        
        return False, "Product not found"
    
    def add_balance(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False, "Invalid amount"
        
        self.current_user.balance += amount
        self.save_data()
        return True, f"Balance updated. New balance: {self.current_user.balance}"

def display_menu(options):
    print("\n" + "="*30)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("="*30)

store = OnlineStore()

while True:
    if store.current_user is None:
        print("\nWelcome to the Online Store!")
        display_menu(["Login", "Sign Up", "Exit"])
        
        choice = input(">> ").strip()
        
        if choice == "1":  # Login
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            success, message = store.login(username, password)
            print(message)
        
        elif choice == "2":  # Sign Up
            print("\nSign Up:")
            username = input("Enter a username: ").strip()
            password = input("Enter a password (min 8 characters): ").strip()
            user_type = input("Are you a seller? (y/n): ").strip().lower()
            is_seller = user_type == 'y'
            
            success, message = store.signup(username, password, is_seller)
            print(message)
        
        elif choice == "3":  # Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    else:
        # User is logged in
        print(f"\nWelcome, {store.current_user.username}!")
        print(f"Your balance: ${store.current_user.balance:.2f}")
        
        if isinstance(store.current_user, RegularUser):
            # Regular user menu
            display_menu(store.current_user.get_menu())
            
            choice = input(">> ").strip()
            
            if choice == "1":  # View Products
                print("\nAvailable Products:")
                for i, product in enumerate(store.products, 1):
                    print(f"{i}. {product.name} - Seller: {product.seller} - Price: ${product.price:.2f} - Stock: {product.stock} - Rating: {product.rating_average:.1f}")
            
            elif choice == "2":  # Search Product
                print("\nSearch by:")
                display_menu(["Name", "Price Range", "Category"])
                
                search_choice = input(">> ").strip()
                
                if search_choice == "1":  # Name
                    query = input("Enter product name: ").strip()
                    results = store.search_products("name", query)
                
                elif search_choice == "2":  # Price Range
                    query = input("Enter price range (min-max): ").strip()
                    results = store.search_products("price_range", query)
                
                elif search_choice == "3":  # Category
                    print("Available categories:", ", ".join(store.categories))
                    query = input("Enter category: ").strip()
                    results = store.search_products("category", query)
                
                else:
                    print("Invalid choice")
                    continue
                
                if not results:
                    print("No products found")
                else:
                    print("\nSearch Results:")
                    for i, product in enumerate(results, 1):
                        print(f"{i}. {product.name} - Seller: {product.seller} - Price: ${product.price:.2f} - Stock: {product.stock} - Rating: {product.rating_average:.1f}")
            
            elif choice == "3":  # Add to Cart
                product_name = input("Enter product name: ").strip()
                quantity = int(input("Enter quantity: ").strip())
                
                # Find product
                product = None
                for p in store.products:
                    if p.name.lower() == product_name.lower():
                        product = p
                        break
                
                if product:
                    success, message = store.add_to_cart(product, quantity)
                    print(message)
                else:
                    print("Product not found")
            
            elif choice == "4":  # View Cart
                if not store.current_user.cart:
                    print("Your cart is empty")
                else:
                    print("\nYour Cart:")
                    total = 0
                    for i, item in enumerate(store.current_user.cart, 1):
                        product = item['product']
                        quantity = item['quantity']
                        item_total = product.price * quantity
                        total += item_total
                        print(f"{i}. {product.name} - Quantity: {quantity} - Price: ${product.price:.2f} - Total: ${item_total:.2f}")
                    print(f"\nCart Total: ${total:.2f}")
            
            elif choice == "5":  # Remove from Cart
                if not store.current_user.cart:
                    print("Your cart is empty")
                else:
                    index = int(input("Enter item number to remove: ").strip()) - 1
                    success, message = store.remove_from_cart(index)
                    print(message)
            
            elif choice == "6":  # Finalize Order
                if not store.current_user.cart:
                    print("Your cart is empty")
                else:
                    success, message = store.finalize_order()
                    print(message)
            
            elif choice == "7":  # Rate Purchased Products
                if not store.current_user.orders:
                    print("You haven't made any purchases yet")
                else:
                    product_name = input("Enter product name to rate: ").strip()
                    rating = float(input("Enter your rating (1-5): ").strip())
                    
                    if 1 <= rating <= 5:
                        success, message = store.rate_product(product_name, rating)
                        print(message)
                    else:
                        print("Rating must be between 1 and 5")
            
            elif choice == "8":  # Add Balance
                amount = float(input("Enter amount to add: ").strip())
                success, message = store.add_balance(amount)
                print(message)
            
            elif choice == "9":  # Logout
                success, message = store.logout()
                print(message)
            
            else:
                print("Invalid choice. Please try again.")
        
        elif isinstance(store.current_user, Seller):
            # Seller menu
            display_menu(store.current_user.get_menu())
            
            choice = input(">> ").strip()
            
            if choice == "1":  # Add Product
                name = input("Enter product name: ").strip()
                category = input("Enter product category: ").strip()
                price = float(input("Enter product price: ").strip())
                stock = int(input("Enter initial stock: ").strip())
                
                success, message = store.add_product(name, category, price, stock)
                print(message)
            
            elif choice == "2":  # Update Product Stock
                product_name = input("Enter product name: ").strip()
                additional_stock = int(input("Enter additional stock: ").strip())
                
                success, message = store.update_product_stock(product_name, additional_stock)
                print(message)
            
            elif choice == "3":  # View My Products
                print("\nYour Products:")
                for i, product in enumerate(store.current_user.products, 1):
                    print(f"{i}. {product.name} - Category: {product.category} - Price: ${product.price:.2f} - Stock: {product.stock} - Rating: {product.rating_average:.1f}")
            
            elif choice == "4":  # Add Balance
                amount = float(input("Enter amount to add: ").strip())
                success, message = store.add_balance(amount)
                print(message)
            
            elif choice == "5":  # Logout
                success, message = store.logout()
                print(message)
            
            else:
                print("Invalid choice. Please try again.")