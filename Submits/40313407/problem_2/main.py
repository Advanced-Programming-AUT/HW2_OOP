def spaced_text(text):
    return ' '.join(list(text))

class MenuItem:
    def __init__(self, uid, label):
        self.uid = uid
        self.label = label

    def price(self):
        return 0

    def __add__(self, other):
        return self.price() + other.price()

    def __mul__(self, qty):
        return self.price() * qty

class PizzaItem(MenuItem):
    def __init__(self, size, flavor, toppings):
        self.size = size
        self.flavor = flavor
        self.toppings = toppings

    def price(self):
        base_costs = {"Small": 8, "Medium": 12, "Large": 16}
        topping_costs = {"Extra Cheese": 2, "Extra Sauce": 1.5, "Olives": 1}
        return base_costs.get(self.size, 0) + sum(topping_costs.get(t, 0) for t in self.toppings)

    def describe(self):
        top = f" with {', '.join(self.toppings)}" if self.toppings else ''
        return f"{self.size} {self.flavor} Pizza{top}"

class BurgerItem(MenuItem):
    def __init__(self, stack, style, addons):
        self.stack = stack
        self.style = style
        self.addons = addons

    def price(self):
        layer_prices = {"Single Layer": 6, "Double Layer": 9, "Triple Layer": 9}
        addon_prices = {"Cheese": 1, "Bacon": 2, "Egg": 1.5}
        return layer_prices.get(self.stack, 0) + sum(addon_prices.get(a, 0) for a in self.addons)

    def describe(self):
        add = f" with {', '.join(self.addons)}" if self.addons else ''
        return f"{self.stack} {self.style} Burger{add}"

class BeverageItem(MenuItem):
    def __init__(self, size, drink_type):
        self.size = size
        self.drink_type = drink_type

    def price(self):
        cost_chart = {"300ml": 2, "500ml": 3, "1L": 5}
        return cost_chart.get(self.size, 0)

    def describe(self):
        return f"{self.size} {self.drink_type}"

class Purchase:
    def __init__(self):
        self.cart = {}
        self.current_id = 0
        self.vouchers = {"DISCOUNT10": 0.9}
        self.applied = []
        self.reduction = 1.0

    def insert(self, product, count):
        self.cart[self.current_id] = [product, count]
        self.current_id += 1

    def discard(self, item_id):
        if item_id in self.cart:
            self.cart[item_id][1] = 0

    def total_cost(self):
        return sum(item.price() * qty for item, qty in self.cart.values())

    def use_coupon(self, coupon_code):
        if coupon_code in self.vouchers:
            self.reduction *= self.vouchers[coupon_code]
            self.applied.append(coupon_code)
        return self.total_cost() * self.reduction

    def summary(self):
        for item_id, (product, qty) in self.cart.items():
            if qty > 0:
                print(f"{qty} x {product.describe()} (Item #{item_id}) - ${product.price():.2f} each")
        print(f"Subtotal: ${self.total_cost():.2f}")
        if self.applied:
            joined_codes = ', '.join(self.applied)
            print(f"Discounted ({joined_codes}): ${self.total_cost() * self.reduction:.2f}")

