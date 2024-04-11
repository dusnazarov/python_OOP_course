# # /////////////////////////
# class Item:
#    def calculate_total_price(self, x , y):
#        return x * y
   
   
# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))


# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))



# ///////////////////////////////////////////////
# class Item:
#     def __init__(self, name, price, quantity=0):
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity        
   
   
# item1 = Item('Phone', 100, 3)
# item2 = Item('Laptop', 1000, 5)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# /////////////////////////
# class Item:
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validation to the recieved arguments
#         assert price >= 0,  f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
#         # Assign to self object
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity        
   
   
# item1 = Item('Phone', 100.25, 4)
# item2 = Item('Laptop', 10.4, 5)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())


# /////////////////////////
# class Item:
#     pay_rate = 0.8  # The pay rate after 20% discount
    
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validation to the recieved arguments
#         assert price >= 0,  f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
#         # Assign to self object
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         self.price = self.price * Item.pay_rate        
   
   
# item1 = Item('Phone', 100, 3)
# item2 = Item('Laptop', 200, 5)

# # print(Item.pay_rate)
# # print(item1.pay_rate)
# # print(item2.pay_rate)


# # print(Item.__dict__)    # All the attributes for class level 
# # print(item1.__dict__)   # All the attributes for instance level



# ///////////////////////////////////////////////////
# class Item:
#     pay_rate = 0.8    # The pay rate after 20% discount
    
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validation to the recieved arguments
#         assert price >= 0,  f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
#         # Assign to self object
#         self.name = name 
#         self.price = price
#         self.quantity = quantity
        
#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         # self.price = self.price * Item.pay_rate
#         self.price = self.price * self.pay_rate      
   
   
# item1 = Item('Phone', 100, 3)
# item1.apply_discount()
# print(item1.price)

# item2 = Item('Laptop', 1000, 5)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)



# ///////////////////////////////////////////////////
class Item:
    pay_rate = 0.8    # The pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the recieved arguments
        assert price >= 0,  f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        self.name = name 
        self.price = price
        self.quantity = quantity

        # Action to exicute 
        Item.all.append(self)
        
        
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate      
   

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# print(Item.all)

for instance in Item.all:
    print(instance.name, instance.price, instance.quantity)

# # # //////////////////// @classmethod///////////////////////////////
# import csv

# class Item:
#     pay_rate = 0.8 # The pay rate after 20% discount
#     all = []
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # Actions to execute
#         Item.all.append(self)

#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         self.price = self.price * self.pay_rate

#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('items.csv', 'r') as f:
#             reader = csv.DictReader(f)          
#             items = list(reader)
            

#         for item in items:
#             Item(
#                 name=item.get('name'),
#                 price=float(item.get('price')),
#                 quantity=int(item.get('quantity')),
#             )

#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"

# Item.instantiate_from_csv()
# print(Item.all)

# # # //////////////////////  @staticmethod  /////////////////////////////
# import csv


# class Item:
#     pay_rate = 0.8 # The pay rate after 20% discount
#     all = []
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # Actions to execute
#         Item.all.append(self)

#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         self.price = self.price * self.pay_rate

#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('items.csv', 'r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)

#         for item in items:
#             Item(
#                 name=item.get('name'),
#                 price=float(item.get('price')),
#                 quantity=int(item.get('quantity')),
#             )

#     @staticmethod
#     def is_integer(num):
#         # We will count out the floats that are point zero
#         # For i.e: 5.0, 10.0
#         if isinstance(num, float):
#             # Count out the floats that are point zero
#             return num.is_integer()
#         elif isinstance(num, int):
#             return True
#         else:
#             return False

#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"

# # print(Item.is_integer(7))




# # ////////////////////// __init__()   /////////////////////////////
# from parent_class import Item 

# class Phone(Item):
#     all = []
#     def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
#         # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
#         assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.broken_phones = broken_phones

#         # Actions to execute
#         Phone.all.append(self)

# phone1 = Phone("JscPhonev10", 500, 5, 1)
# print(phone1.calculate_total_price())
# phone2 = Phone("JscPhonev20", 700, 5, 1)
# print(Item.all)
# print(Phone.all)

# # //////////////////////  super().__init__() /////////////////////////////

# from parent_class import Item 
# class Phone(Item):   
#     def __init__(self, name: str, price: float, quantity=0, broken_phones=0):       
#         super().__init__(name, price, quantity)        
      
#         assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"
             
#         self.broken_phones = broken_phones

   

# phone1 = Phone("JscPhonev10", 500, 5, 1)
# print(phone1.calculate_total_price())
# phone2 = Phone("JscPhonev20", 700, 5, 1)

# print(Item.all)
# print(Phone.all)

        
    



