Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #Step 1
>>> 
>>> class ItemToPurchase:
...     def set_Snickers_details(self, item_name="none" , item_price=0, item_quantity=0):
...         self.item_name = item_name
...         self.item_price = item _ price
...         
SyntaxError: invalid syntax
>>> #Step 1
... 
... class ItemToPurchase:
...     def set_Snickers_details(self, item_name="none" , item_price=0, item_quantity=0):
...         self.item_name = item_name
...         self.item_price = item_price
...         self.item_quantity = item_quantity
... 
...         
>>>     def print_item_cost(self) :
...         
SyntaxError: unexpected indent
>>> class ItemToPurchase:
...     def set_Snickers_details(self, item_name="none" , item_price=0, item_quantity=0):
...         self.item_name = item_name
...         self.item_price = item_price
...         self.item_quantity = item_quantity
... 
...         
... def print_item_cost(self):
...     
SyntaxError: invalid syntax
>>> class ItemToPurchase:
...     def set_Snickers_details(self, item_name="none" , item_price=0, item_quantity=0):
...         self.item_name = item_name
...         self.item_price = item_price
...         self.item_quantity = item_quantity
... 
...         
>>> def print_item_cost(self):
...     print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
... 
...     
>>> if __name__ == "__main__":
...     #Get user input for Snickers
...     print("Snickers")
...     Snickers = ItemToPurchase()
...     Snickers.set_item_details(
...         input("Milk Chocolate:\n"),
...         float(input("$3.00:\n")),
...         int(input("Enter the Pepsi quantity:\n")))
... 
...     
Snickers
Traceback (most recent call last):
  File "<pyshell#26>", line 5, in <module>
    Snickers.set_item_details(
AttributeError: 'ItemToPurchase' object has no attribute 'set_item_details'. Did you mean: 'set_Snickers_details'?
>>> class ItemToPurchase:
...     def set_Snickers_details(self, item_name="none" , item_price=0, item_quantity=0):
...         self.item_name = item_name
...         self.item_price = item_price
...         self.item_quantity = item_quantity
... 
...         
... def print_item_cost(self):
...     print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    
if __name__ == "__main__":
    #Get user input for Snickers
    print("Snickers")
    Snickers = ItemToPurchase()
    Snickers.set_Snickers_details(
        
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax

class ItemToPurchase:
    def set_Snickers_details(self, item_name="none" , item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        
def print_item_cost(self):
    print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    
if __name__ == "__main__":
    #Get user input for Snickers
    print("Snickers")
    Snickers = ItemToPurchase()
    Snickers.set_Snickers_details(
        
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax

class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        
SyntaxError: duplicate argument 'item_price' in function definition
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        
SyntaxError: duplicate argument 'item_price' in function definition
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        
    def print_item_cost(self):
        
SyntaxError: unexpected indent
lass ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            
SyntaxError: invalid syntax
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            

    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            

    
SyntaxError: invalid syntax

class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
            if __name__ == "__main__":
            print("Item 1")
            
SyntaxError: expected an indented block after 'if' statement on line 9


class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            

    print("Item 1")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))

    
Item 1
Enter the snickers name:

Enter the snickers price:

Traceback (most recent call last):
  File "<pyshell#62>", line 5, in <module>
    snickers.item_price = float(input("Enter the snickers price:\n"))
ValueError: could not convert string to float: ''

class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            

    print("Item 1")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    
SyntaxError: invalid syntax

class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")

    
Item
Enter the snickers name:
Milk Chocolate Snickers
Enter the snickers price:
3
Enter the snickers quantity:
2

Item 2
Enter the pepsi flavor:
Cherry Pepsi
Traceback (most recent call last):
  File "<pyshell#84>", line 10, in <module>
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
NameError: name 'flat' is not defined. Did you mean: 'float'?

class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")
    
SyntaxError: invalid syntax

class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")
    
SyntaxError: invalid syntax
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            if __name__ == "__main__":
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")
    
SyntaxError: expected an indented block after 'if' statement on line 10
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
           
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")
    
SyntaxError: invalid syntax
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")
    
SyntaxError: invalid syntax
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")


    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers name:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")
    
SyntaxError: invalid syntax
class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers flavor:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")

    
Item
Enter the snickers flavor:
Snicker Butterscotch
Enter the snickers price:
3
Enter the snickers quantity:
2

Item 2
Enter the pepsi flavor:
Cherry Pepsi
Traceback (most recent call last):
  File "<pyshell#97>", line 10, in <module>
    pepsi.item_price = flat(input("Enter the pepsi price:\n"))
NameError: name 'flat' is not defined. Did you mean: 'float'?
NameError: name 'flat' is not defined. Did you mean: 'float'?
SyntaxError: invalid syntax

class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers flavor:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = float(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")

    
Item
Enter the snickers flavor:
Snicker Butterscotch
Enter the snickers price:
3
Enter the snickers quantity:
2

Item 2
Enter the pepsi flavor:
Cherry Pepsi
Enter the pepsi price:
1.50
Enter the pepsi quantity:
1

TOTAL COST
Traceback (most recent call last):
  File "<pyshell#104>", line 13, in <module>
    snickers.print_item_cost()
AttributeError: 'ItemToPurchase' object has no attribute 'print_item_cost'

class ItemToPurchase:
    def __init__(self, item_name="none" , item_price="none", item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    def print_item_cost(self):
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

            
    print("Item")
    snickers = ItemToPurchase()
    snickers.item_name = input("Enter the snickers flavor:\n")
    snickers.item_price = float(input("Enter the snickers price:\n"))
    snickers.item_quantity = int(input("Enter the snickers quantity:\n"))
    print("\nItem 2")
    pepsi = ItemToPurchase()
    pepsi.item_name = input("Enter the pepsi flavor:\n")
    pepsi.item_price = float(input("Enter the pepsi price:\n"))
    pepsi.item_quantity = int(input("Enter the pepsi quantity:\n"))
    print("\nTOTAL COST")
    snickers.print_item_cost()
    pepsi.print_item_cost()
    total_cost = (snickers.item_quantity * snickers.item_price) + (pepsi.item_quantity * pepsi.item_price)
    print(f"\nTotal:${total_cost}")

    
Item
Enter the snickers flavor:
Snicker Butterscotch
Enter the snickers price:
3.00
Enter the snickers quantity:
2

Item 2
Enter the pepsi flavor:
Cherry Pepsi
Enter the pepsi price:
1.89
Enter the pepsi quantity:
1

TOTAL COST
Snicker Butterscotch 2 @ $3.0 = $6.0
Cherry Pepsi 1 @ $1.89 = $1.89

Total:$7.89
