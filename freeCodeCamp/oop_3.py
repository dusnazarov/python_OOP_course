# # //////////////////////////////
# class Item:
#     pay_rate = 0.8


# item1 = Item()
# item2 = Item()
# item1.pay_rate 
# item2.pay_rate 

# print(item1.pay_rate)
# print(item2.pay_rate)

# # //////////////////////////////
# class Item:
#     pay_rate = 0.8


# item1 = Item()
# item2 = Item()
# item1.pay_rate 
# item2.pay_rate 
# Item.pay_rate = 0.7

# print(item1.pay_rate)
# print(item2.pay_rate)


# # //////////////////////////////
# class Item:
#     pay_rate = 0.8


# item1 = Item()
# item2 = Item()
# item1.pay_rate 
# item2.pay_rate 
# Item.pay_rate = 0.7
# item1.pay_rate = 0.6

# print(item1.pay_rate)
# print(item2.pay_rate)

# # # //////////////////////////////
# class Item:
#     pay_rate = 0.8

#     def __init__(self, x, y):
#         self.x = x
#         self.y =y
        
#     def calc_item(self):
#         # return  self.x * self.y * Item.pay_rate
#         return  self.x * self.y * self.pay_rate
       
        

# item1 = Item(2, 4)
# item2 = Item(3, 2)

# Item.pay_rate = 0.7
# item1.pay_rate = 0.6   

# print(item1.calc_item())
# print(item2.calc_item())


# # # # ////////// hamasiga ////////////////////
# class Item:
#     pay_rate = 0.8

#     def __init__(self, x, y):
#         self.x = x
#         self.y =y
        
#     def calc_item(self):
#         return  self.x * self.y * Item.pay_rate
      
# item1 = Item(2, 4)
# item2 = Item(5, 2)
# item3 = Item(4, 5)

# print(item1.calc_item())
# print(item2.calc_item())
# print(item3.calc_item())


# # #///////////  o'zgarmaydi  ///////////////////
# class Item:
#     pay_rate = 0.8

#     def __init__(self, x, y):
#         self.x = x
#         self.y =y
        
#     def calc_item(self):
#         return  self.x * self.y * Item.pay_rate
      
# item1 = Item(2, 4)
# item1.pay_rate = 0.6
# item2 = Item(5, 2)
# item2.pay_rate = 0.5
# item3 = Item(4, 5)
# item3.pay_rate = 0.4

# print(item1.calc_item())
# print(item2.calc_item())
# print(item3.calc_item())


# # #///////////  o'zgarmaydi  ///////////////////
# class Item:
#     pay_rate = 0.8

#     def __init__(self, x, y):
#         self.x = x
#         self.y =y
        
#     def calc_item(self):
#         return  self.x * self.y * self.pay_rate
      
# item1 = Item(2, 4)
# item1.pay_rate = 0.6
# item2 = Item(5, 2)
# item2.pay_rate = 0.5
# item3 = Item(4, 5)
# item3.pay_rate = 0.4

# print(item1.calc_item())
# print(item2.calc_item())
# print(item3.calc_item())


# # //////////////////////////////
# class Item:
#     pay_rate = 0.8


# item = Item()
# Item.pay_rate = 0.7

# print(item.pay_rate)
# print(Item.pay_rate)

# # //////////////////////////////
# class Item:
#     pay_rate = 0.8

# item = Item()
# # item.pay_rate = 0.4
# # Item.pay_rate = 0.7

# print(item.pay_rate)
# print(Item.pay_rate)



# #////////////////////////////////////////////////
# class Item: 

#     def __init__(self, name):              
#         self.name = name
          
# item1 = Item("MyItem")
# # item1.name = 'OtherItem'
# print(item1.name)

# # #///////////////////  Read-Only Attribute   /////////////////////////
# class Item: 

#     def __init__(self, name):              
#         self._name = name
          
#     @property
#     # property decorator = Read-Only Attribute
#     def name(self):
#         return self._name
        
# item1 = Item("MyItem")
# # item1.name = 'OtherItem'   # it does not work becouse @property decorator = Read-Only Attribute
# print(item1.name)

# # ///////////////////  Setter and Getter  /////////////////////////
class Item: 

    def __init__(self, name):              
        self.__name = name
          
    @property
    # property decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # print(value)
        self.__name = value
        
item1 = Item("MyItem")
item1.name = 'OtherItem'  
print(item1.name)

