class Product:
    def __init__(self, name_of_product, seller_of_product, price_of_product, stock_of_product, category_of_product):
        self.name_of_this_product = name_of_product
        self.seller_of_this_product = seller_of_product
        self.price_of_this_product = price_of_product
        self.stock_of_this_product = stock_of_product
        self.category_of_this_product = category_of_product
        self.list_of_ratings_for_this_product = []
        self.average_rating_of_this_product = 0.0

    def add_rating(self, rating):
        self.list_of_ratings_for_this_product.append(rating)
        self.calculate_average_rating()

    def calculate_average_rating(self):
        if self.list_of_ratings_for_this_product:
            self.average_rating_of_this_product = sum(self.list_of_ratings_for_this_product) / len(self.list_of_ratings_for_this_product)

    def reduce_stock(self, quantity):
        if quantity <= self.stock_of_this_product:
            self.stock_of_this_product -= quantity
            return True
        return False

    def restock(self, quantity):
        self.stock_of_this_product += quantity