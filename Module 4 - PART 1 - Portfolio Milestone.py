Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ItemToPurchase:
...     def __init__(self, item_name="none", item_price=0, item_quantity=0):
...         self.item_name = item_name
...         self.item_price = item_price
...         self.item_quantity = item_quantity
...     def print_item_cost(self):
...         print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}")
... 
...         
>>> class PepsiItem(ItemToPurchase):
...     def __init__(self, item_name="Pepsi", item_price=1.89, item_quantity=1):
...         super().__init__(item_name, item_price, item_quantity)
... 
...         
>>> if __name__ == "__main__":
...     # Create an instance for Pepsi
...     Pepsi = PepsiItem()
...     # Print item cost
...     print("\nTOTAL COST")
...     Pepsi.print_item_cost()
... 
...     

TOTAL COST
Pepsi 1 @ $1.89 = $1.89
