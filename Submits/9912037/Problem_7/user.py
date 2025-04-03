class User:
    def __init__(self, username_for_user, password_for_user, role_of_user):
        self.username_of_this_user = username_for_user
        self.password_of_this_user = password_for_user
        self.role_of_this_user = role_of_user
        self.current_balance = 0.0
        self.users_shopping_cart = []
        self.users_previous_orders = []
        self.products_user_has_rated = []

    def add_to_balance(self, amount):
        self.current_balance += amount

    def add_to_cart(self, product, quantity):
        self.users_shopping_cart.append({'product': product, 'quantity': quantity})

    def remove_from_cart(self, index):
        if 0 <= index < len(self.users_shopping_cart):
            return self.users_shopping_cart.pop(index)
        return None

    def finalize_order(self):
        self.users_previous_orders.extend(self.users_shopping_cart)
        self.users_shopping_cart = []

    def rate_product(self, product, rating):
        if product not in self.products_user_has_rated:
            self.products_user_has_rated.append(product)
            return True
        return False