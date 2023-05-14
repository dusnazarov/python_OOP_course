
# 1)  //////////////////////////////////////////
# class Item:
#     def show(self, x, y):
#         return x*y

# item1=Item()
# item1.name='Phone'
# item1.price=100
# item1.quantity=5

# print(item1.show(item1.price, item1.quantity))

# 1)  //////////////////////////////////////////
class Item:

    def __init__(self,name):
        return f"Hello world,{self.name}"
    

item1=Item()
item1.name='Phone'
item1.price=100
item1.quantity=5

item2=Item()
item2.name='Laptop'
item2.price=200
item2.quantity=3




# 1)  //////////////////////////////////////////
# class Item:

#     pass

# item1=Item()
# item1.name='Phone'
# item1.price=100
# item1.quantity=5

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# 2) /////////////////////////////////////
# class Item:
#     def calculate_total_price(self, x, y):
#         return x*y
    

# item1=Item()
# item1.name='Phone'
# item1.price=100
# item1.quantity=5
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2=Item()
# item2.name='Laptop'
# item2.price=1000
# item2.quantity=3
# print(item2.calculate_total_price(item2.price, item2.quantity))

# 3) /////////////////////////////////////
# class Item:
#     def __init__(self):
#         print('I AM CREATED !') 
#     def calculate_total_price(self, x, y):
#         return x*y    

# item1=Item()
# item1.name='Phone'
# item1.price=100
# item1.quantity=5

# item2=Item()
# item2.name='Laptop'
# item2.price=1000
# item2.quantity=3

# 4) /////////////////////////////////////
# class Item:
#     def __init__(self, name):
#         print(f"An instance created : {name}") 
#     def calculate_total_price(self, x, y):
#         return x*y    

# item1=Item('Phone')
# item1.name='Phone'
# item1.price=100
# item1.quantity=5

# item2=Item('Laptop')
# item2.name='Laptop'
# item2.price=1000
# item2.quantity=3

# 5) /////////////////////////////////////
# class Item:
#     def __init__(self, name):
#         self.name=name
        
#     def calculate_total_price(self, x, y):
#         return x*y    

# item1=Item('Phone')
# item1.price=100
# item1.quantity=5

# item2=Item('Laptop')
# item2.price=1000
# item2.quantity=3

# print(item1.name)
# print(item2.name)

# 6) /////////////////////////////////////
# class Item:
#     def __init__(self, name, price):
#         self.name=name
#         self.price=price
        
#     def calculate_total_price(self, x, y):
#         return x*y    

# item1=Item('Phone',100)
# item1.quantity=5

# item2=Item('Laptop',1000)
# item2.quantity=3

# print(item1.price)
# print(item2.price)

# 7) ////////////////////////////////////////////////
# class Item:
#     def __init__(self, name, price, quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
        
#     def calculate_total_price(self, x, y):
#         return x*y    

# item1=Item('Phone', 100, 5)

# item2=Item('Laptop',1000, 3)

# print(item1.name)
# print(item2.price)
# print(item1.quantity)

# print(item2.name)
# print(item1.price)
# print(item2.quantity)

# 8) ////////////////////////////////////////////////
# class Item:
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >=0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self oblect
#         self.name=name
#         self.price=price
#         self.quantity=quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity    

# item1=Item('Phone', 100, 1)

# item2=Item('Laptop',1000, -3)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# 9) ////////////////////////////////////////////////
# class Item:
#     pay_rate=0.8  # The pay rate after 20% discount

#     def __init__(self, name: str, price: float, quantity=0):

#         # Run validations to the received arguments
#         assert price >=0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self oblect
#         self.name=name
#         self.price=price
#         self.quantity=quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity    

# item1=Item('Phone', 100, 2)

# item2=Item('Laptop',1000, 3)

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# 10) ////////////////////////////////////////////////
# class Item:
#     pay_rate=0.8  # The pay rate after 20% discount

#     def __init__(self, name: str, price: float, quantity=0):

#         # Run validations to the received arguments
#         assert price >=0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self oblect
#         self.name=name
#         self.price=price
#         self.quantity=quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity    

# item1=Item('Phone', 100, 2)

# item2=Item('Laptop',1000, 3)

# print(Item.__dict__)  # All Attributes for class level
# print(item1.__dict__)  # All Attributes for instance level

# 11) ////////////////////////////////////////////////
# class Item:
#     pay_rate=0.8  # The pay rate after 20% discount

#     def __init__(self, name: str, price: float, quantity=0):

#         # Run validations to the received arguments
#         assert price >=0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self oblect
#         self.name=name
#         self.price=price
#         self.quantity=quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity    

#     def apply_disount(self):
#         self.price=self.price * Item.pay_rate

# item1=Item('Phone', 100, 2)
# item1.apply_disount()
# print(item1.price)

# item2=Item('Laptop', 1000, 3)
# item2.pay_rate=0.7
# item2.apply_disount()
# print(item2.price)

# 12) ////////////////////////////////////////////////
# class Item:
#     pay_rate=0.8  # The pay rate after 20% discount

#     def __init__(self, name: str, price: float, quantity=0):

#         # Run validations to the received arguments
#         assert price >=0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self oblect
#         self.name=name
#         self.price=price
#         self.quantity=quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity    

#     def apply_disount(self):
#         self.price=self.price * self.pay_rate

# item1=Item('Phone', 100, 2)
# item1.apply_disount()
# print(item1.price)

# item2=Item('Laptop', 1000, 3)
# item2.pay_rate=0.7
# item2.apply_disount()
# print(item2.price)


# 13) ////////////////////////////////////////////////
# class Item:
#     pay_rate=0.8  # The pay rate after 20% discount

#     all=[]

#     def __init__(self, name: str, price: float, quantity=0):

#         # Run validations to the received arguments
#         assert price >=0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self oblect
#         self.name=name
#         self.price=price
#         self.quantity=quantity

#         # Actions to execute
#         Item.all.append(self)
        
#     def calculate_total_price(self):
#         return self.price * self.quantity    

#     def apply_disount(self):
#         self.price=self.price * self.pay_rate


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)


# 14) ////////////////////////////////////////////////
# class Item:
#     pay_rate=0.8  # The pay rate after 20% discount

#     all=[]

#     def __init__(self, name: str, price: float, quantity=0):

#         # Run validations to the received arguments
#         assert price >=0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self oblect
#         self.name=name
#         self.price=price
#         self.quantity=quantity

#         # Actions to execute
#         Item.all.append(self)
        
#     def calculate_total_price(self):
#         return self.price * self.quantity    

#     def apply_disount(self):
#         self.price=self.price * self.pay_rate


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name)


# 15) ////////////////////////////////////////////////
# class Item:
#     pay_rate=0.8  # The pay rate after 20% discount

#     all=[]

#     def __init__(self, name: str, price: float, quantity=0):

#         # Run validations to the received arguments
#         assert price >=0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self oblect
#         self.name=name
#         self.price=price
#         self.quantity=quantity

#         # Actions to execute
#         Item.all.append(self)
        
#     def calculate_total_price(self):
#         return self.price * self.quantity    

#     def apply_disount(self):
#         self.price=self.price * self.pay_rate

#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# # for instance in Item.all:
# #     print(instance.name)
# print(Item.all)


