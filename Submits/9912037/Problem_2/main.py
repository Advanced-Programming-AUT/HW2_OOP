from pizza import PizzaClassChild
from burger import BurgerClassChild
from drink import DrinkClassChild
from order import OrderManagementClass

order_system_instance = OrderManagementClass()

pizza_item = PizzaClassChild("Large", "Pepperoni", ["Cheese", "Extra Sauce"])
burger_item = BurgerClassChild("Double", "Brioche", ["Bacon", "Cheese"])
drink_item = DrinkClassChild("560ml", "Soda")

order_system_instance.add_item_to_order_method(pizza_item, 2)
order_system_instance.add_item_to_order_method(burger_item, 1)
order_system_instance.add_item_to_order_method(drink_item, 3)

print(order_system_instance.display_order_details_method())

total_after_discount = order_system_instance.apply_discount_code_method("DISCOUNT10")
print(f"Total price after DISCOUNT10: ${total_after_discount:.2f}")