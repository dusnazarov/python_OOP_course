# 1) ////////////////////////
# class Person:
#     name='Elyor'   
#     print(name)  # name - ordinary variable
# Person


# 1) ////////////////////////
# class Person:
#     name='Elyor'
   
#     def show():
#         print(Person.name)  # Person.name - class variable, class level
 
   
# Person.show()

# 1) ////////////////////////
# class Person:
#     name='Elyor'
   
#     def show(self):
#         print(self.name)  #  self.name - instance variable, instance level
   
# p = Person()
# p.show()


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



# /////////////////
# class Comp:
#     x= 5
#     print(x)   

# print(Comp.x)


# # /////////////////
# class Comp:
#     x= 5
#     print(x)
    
#     def show():
#         Comp.x = 6
#         print(Comp.x)

# Comp.show()

# # /////////////////
# class People:

#     def show():    
#         print(People.first, People.last)
        
# People.first = 'Elyor' 
# People.last = 'Dusnazarov' 
# People.show()

# # /////////////////
# class People:
#     first = 'Elyor' 
#     last = 'Dusnazarov'  

#     def show():    
#         print(People.first, People.last)
        
# People.show()

# # /////////////////
# class People:    

#     def show():
#         People.first = 'Elyor'
#         People.last = 'Dusnazarov'            
#         print(People.first, People.last)
        
# People.show()

# # /////////////////
# class People:    

#     def show(first, last):                 
#         print(first, last)

    
# People.show('Elyor','Dusnazarov')

















