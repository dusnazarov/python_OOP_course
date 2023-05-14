


# //////////////////////////////////////
# class Comp:
#     x=5
#     print(x)
# com=Comp()

#////////////////////////////////////////
# class Comp:
#     x=5
#     def show(self):
#         print(self.x)
# com=Comp()
# com.show()

#////////////////////////////////////////
# class Comp:

#     def show(self):
#         x=5        
#         print(x)
# com=Comp()
# com.show()

# /////////////////////////////////////
# class Purse:
#     def __init__(self):
#         self.money=0.00
    
#     def info(self):
#         return self.money

# x=Purse()
# y=Purse()

# x.money=100

# print(y.info())
# print(x.info())


# /////////////////////////////////////
# class Purse:
#     def __init__(self, valuta, name='Unknown'):
#         self.money=0.00
#         self.valuta=valuta
#         self.name=name
    
#     def top_up_balance(self,howmany):
#         self.money = self.money + howmany
    
#     def info(self):
#         print(f"{self.money} {self.valuta} {self.name}")

# x=Purse(valuta='USD',name='Bill')
# y=Purse('EUR')

# y.top_up_balance(200)
# y.info()

# x.top_up_balance(100)
# x.info()


# /////////////////////////////////////
# class Purse:
#     def __init__(self, valuta, name='Unknown'):
#         self.money=0.00
#         self.valuta=valuta
#         self.name=name
    
#     def top_up_balance(self,howmany):
#         self.money = self.money + howmany
    
#     def top_down_balance(self,howmany):
#         if self.money-howmany<0:
#             print('pul yetarli emas')
#             raise ValueError('Pul yetarli emas')
#         self.money=self.money-howmany
    
#     def info(self):
#         print(f"{self.money} {self.valuta} {self.name}" )

# x=Purse('USD','Bill')

# x.top_up_balance(300)
# x.top_down_balance(100)
# x.info()


# /////////////////////////////////////
# class Purse:
#     def __init__(self, valuta, name='Unknown'):
#         self.money=0.00
#         self.valuta=valuta
#         self.name=name
    
#     def top_up_balance(self,howmany):
#         self.money = self.money + howmany
    
#     def top_down_balance(self,howmany):
#         if self.money-howmany<0:
#             print('pul yetarli emas')
#             raise ValueError('Pul yetarli emas')
#         self.money=self.money-howmany
    
#     def info(self):
#         print(f"{self.money} {self.valuta} {self.name}" )

#     def __del__(self):
#         print('Kosholyok uchgan')
        
# x=Purse('USD','Bill')

# x.top_up_balance(300)
# x.top_down_balance(100)
# x.info()
# del x


#///////////////////////////////////////////
# class MyClass:
#     x = 5   

# p1= MyClass()
# p2=MyClass()
# p3=MyClass()
# print(p1.x)
# print(p2.x)
# print(p3.x)

#///////////////
# class MyClass:
#     x = 1; y=2; z=3

# p1=MyClass()
# p1=MyClass()
# p1=MyClass()

# p2=MyClass()
# p2=MyClass()
# p2=MyClass()

# p3=MyClass()
# p3=MyClass()
# p3=MyClass()

# print(p1.x)
# print(p1.y)
# print(p1.z)

# print(p2.x)
# print(p2.y)
# print(p2.z)

# print(p3.x)
# print(p3.y)
# print(p3.z)

# print(p1.x,p2.x,p3.x)
# print(p1.y,p2.y,p3.y)
# print(p1.z,p2.z,p3.z)

# print(p1.x,p1.y,p1.z)
# print(p2.x,p2.y,p2.z)
# print(p3.x,p3.y,p3.z)

# ///////////////////////////////
# class Comp:
#     def config_1(self):
#         print('1')

#     def config_2(self):
#         print('2')

#     def config_3(self):
#         print('3')

# o1=Comp()
# o1.config_1()
# o1.config_2()
# o1.config_3()

# o2=Comp()
# o2.config_1()
# o2.config_2()
# o2.config_3()




#/////////////////////////////////
# biz yangi atribut lar yaratamiz va hotirada.
class Point:
    color='red'
    circle=2

x=Point()
x.name='Elyor'
x.lname='Dusnazarov'

print(type(x)==Point)
print(isinstance(x,Point))


#/////////////////////////////////
# hatolik chiqmadi chunki biz uzi shu klasda o'tiribmiz, self kerak bo'lmaydi.
# class Point:
#     color='red'
#     circle=2

#     def set_color():
#         print('set_color funksiy chaqirildi')

# print(Point.set_color())

#/////////////////////////////////
# bu yerda hatolik bor chunki biz bita exemplar(obekt) yaratdik qaysi obektdan chaqirilayotganini bilish uchun self kerak bo'ladi.
# class Point:
#     color='red'
#     circle=2

#     def set_color():
#         print('set_color funksiy chaqirildi')

# x=Point()
# print(x.set_color())

#/////////////////////////////////
# class Point:
#     color='red'
#     circle=2

#     def set_color(self):        
#         print('set_color funksiy chaqirildi', self)
# x=Point()
# print(x.set_color())


#/////////////////////////////////
# class Point:
#     color='red'
#     circle=2

#     def set_coords(self, x, y):  
#         self.x=x
#         self.y=y
    
    
        
# a=Point()
# a.set_coords(1, 2)
# print(a.__dict__)

# b=Point()
# b.set_coords(10, 30)
# print(b.__dict__)

# //////////////////////////////////////
# class Point:
#     def __init__(self):
#         self.x=0
#         self.y=0

#     def set_coords(self, x, y):  
#         self.x=x
#         self.y=y
    
        
# a=Point()
# print(a.__dict__)


# //////////////////////////////////////
# class Point:
#     def __init__(self, x, y):
#         self.x= x
#         self.y= y

#     def set_coords(self, x, y):  
#         self.x=x
#         self.y=y
            
# a=Point(2, 3)
# print(a.__dict__)

# //////////////////////////////////////
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x= x
#         self.y= y

#     def set_coords(self, x, y):  
#         self.x=x
#         self.y=y
            
# a=Point()
# print(a.__dict__)


# //////////////////////////////////////
# class Point:
#     def __init__(self, x, y):
#         self.x= x
#         self.y= y

    # def set_coords(self, x, y):  
    #     self.x=x
    #     self.y=y
            
# a=Point(2, 4)
# print(a.x)
# b=Point(3,7)
# print(b.y)



