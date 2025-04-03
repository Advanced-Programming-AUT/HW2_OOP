from store_manager import StoreManager

store = StoreManager()

while True:
    is_logged_in = store.user_currently_logged_in is not None
    is_seller = is_logged_in and store.user_currently_logged_in.role_of_this_user == 'seller'

    print("\nWelcome to the Online Store!")
    if not is_logged_in:
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
    else:
        print("Main Menu:")
        if is_seller:
            print("1. View Products")
            print("2. Add Product")
            print("3. Restock Product")
            print("4. Logout")
        else:
            print("1. View Products")
            print("2. Search Product")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Remove from Cart")
            print("6. Finalize Order")
            print("7. Rate Purchased Products")
            print("8. Add Balance")
            print("9. Logout")

    choice = input(">> ")

    if not is_logged_in:
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if store.login(username, password):
                print("Login successful!")
            else:
                print("Invalid credentials!")
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password (min 8 chars): ")
            role = input("Enter role (customer/seller): ")
            if store.create_user(username, password, role):
                print("Account created!")
            else:
                print("Failed to create account!")
        elif choice == '3':
            store.save_all_data()
            break
        else:
            print("Invalid choice!")
    else:
        if is_seller:
            if choice == '1':
                products = store.get_products_by_seller(store.user_currently_logged_in.username_of_this_user)
                for idx, p in enumerate(products, 1):
                    print(
                        f"{idx}. {p.name_of_this_product} - ${p.price_of_this_product} - Stock: {p.stock_of_this_product}")
            elif choice == '2':
                name = input("Product name: ")
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                category = input("Category: ")
                if store.add_product(name, price, stock, category):
                    print("Product added!")
                else:
                    print("Failed to add product!")
            elif choice == '3':
                products = store.get_products_by_seller(store.user_currently_logged_in.username_of_this_user)
                for idx, p in enumerate(products, 1):
                    print(f"{idx}. {p.name_of_this_product} - Stock: {p.stock_of_this_product}")
                try:
                    idx = int(input("Select product: ")) - 1
                    qty = int(input("Quantity to add: "))
                    if 0 <= idx < len(products):
                        products[idx].restock(qty)
                        store.save_all_data()
                        print("Stock updated!")
                    else:
                        print("Invalid selection!")
                except ValueError:
                    print("Invalid input!")
            elif choice == '4':
                store.logout()
                print("Logged out!")
            else:
                print("Invalid choice!")
        else:
            if choice == '1':
                for idx, p in enumerate(store.list_of_all_products, 1):
                    print(
                        f"{idx}. {p.name_of_this_product} - ${p.price_of_this_product} - Stock: {p.stock_of_this_product} - Rating: {p.average_rating_of_this_product:.1f}")
            elif choice == '2':
                print("Search by:\n1. Name\n2. Category")
                search_choice = input(">> ")
                if search_choice == '1':
                    term = input("Enter product name: ")
                    results = store.search_products('name', term)
                elif search_choice == '2':
                    term = input("Enter category: ")
                    results = store.search_products('category', term)
                else:
                    results = []

                for idx, p in enumerate(results, 1):
                    print(
                        f"{idx}. {p.name_of_this_product} - ${p.price_of_this_product} - Stock: {p.stock_of_this_product} - Rating: {p.average_rating_of_this_product:.1f}")
            elif choice == '3':
                for idx, p in enumerate(store.list_of_all_products, 1):
                    print(f"{idx}. {p.name_of_this_product} - ${p.price_of_this_product}")
                try:
                    idx = int(input("Select product: ")) - 1
                    qty = int(input("Quantity: "))
                    if 0 <= idx < len(store.list_of_all_products):
                        if store.list_of_all_products[idx].reduce_stock(qty):
                            store.user_currently_logged_in.add_to_cart(store.list_of_all_products[idx], qty)
                            store.save_all_data()
                            print("Added to cart!")
                        else:
                            print("Not enough stock!")
                    else:
                        print("Invalid selection!")
                except ValueError:
                    print("Invalid input!")
            elif choice == '4':
                cart = store.user_currently_logged_in.users_shopping_cart
                if not cart:
                    print("Cart is empty!")
                else:
                    total = 0
                    for idx, item in enumerate(cart, 1):
                        cost = item['product'].price_of_this_product * item['quantity']
                        total += cost
                        print(f"{idx}. {item['product'].name_of_this_product} x {item['quantity']} = ${cost}")
                    print(f"Total: ${total}")
            elif choice == '5':
                cart = store.user_currently_logged_in.users_shopping_cart
                if not cart:
                    print("Cart is empty!")
                else:
                    for idx, item in enumerate(cart, 1):
                        print(f"{idx}. {item['product'].name_of_this_product} x {item['quantity']}")
                    try:
                        idx = int(input("Select item to remove: ")) - 1
                        if 0 <= idx < len(cart):
                            removed = store.user_currently_logged_in.remove_from_cart(idx)
                            if removed:
                                removed['product'].restock(removed['quantity'])
                                store.save_all_data()
                                print("Item removed!")
                        else:
                            print("Invalid selection!")
                    except ValueError:
                        print("Invalid input!")
            elif choice == '6':
                cart = store.user_currently_logged_in.users_shopping_cart
                if not cart:
                    print("Cart is empty!")
                else:
                    total = sum(item['product'].price_of_this_product * item['quantity'] for item in cart)
                    if store.user_currently_logged_in.current_balance >= total:
                        store.user_currently_logged_in.finalize_order()
                        store.save_all_data()
                        print("Order completed!")
                    else:
                        print("Insufficient balance!")
            elif choice == '7':
                orders = store.user_currently_logged_in.users_previous_orders
                if not orders:
                    print("No purchased products!")
                else:
                    for idx, item in enumerate(orders, 1):
                        print(f"{idx}. {item['product'].name_of_this_product}")
                    try:
                        idx = int(input("Select product to rate: ")) - 1
                        if 0 <= idx < len(orders):
                            rating = float(input("Rating (1-5): "))
                            if 1 <= rating <= 5:
                                product = orders[idx]['product']
                                if store.user_currently_logged_in.rate_product(product, rating):
                                    product.add_rating(rating)
                                    store.save_all_data()
                                    print("Rating submitted!")
                                else:
                                    print("Already rated this product!")
                            else:
                                print("Rating must be 1-5!")
                        else:
                            print("Invalid selection!")
                    except ValueError:
                        print("Invalid input!")
            elif choice == '8':
                try:
                    amount = float(input("Amount to add: "))
                    store.user_currently_logged_in.add_to_balance(amount)
                    store.save_all_data()
                    print(f"New balance: ${store.user_currently_logged_in.current_balance}")
                except ValueError:
                    print("Invalid amount!")
            elif choice == '9':
                store.logout()
                print("Logged out!")
            else:
                print("Invalid choice!")