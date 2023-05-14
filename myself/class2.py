# class User:
#     pass

# User.first_name='Qodir'
# User.last_name='Bahodirov'

# print(User.first_name)
# print(User.__dict__)


# user1=User()
# user1.first_name='Elyor'
# user1.last_name='Dusnazarov'

# print(user1.first_name)
# print(user1.__dict__)

# user2=User()
# user2.first_name='Mohinur'
# user2.last_name='Qodirova'

# print(user2.first_name)
# print(user2.__dict__)

# ///////////////////////////////////////
# OUTER and INNER classes 
# class Person:
#     name='Elyor'
#     lname='Dusnazarov'
#     age=21
    
#     def show(self):        
#         print(self.name, self.lname, self.age)
        
#     class User:
#         name='Shuhrat'
#         lname='Dusnazarov'
#         age=23
        
#         def show(self):
#             print(self.name, self.lname, self.age)
            
# p=Person.User()   
# u=Person()
 
# p.show()
# u.show()

# ///////////////////////////////////////
# OUTER and INNER classes 
# class Person:    
#     def show(self):        
#         print(self.name, self.lname, self.age)

        
#     class User:        
#         def show(self):
#             print(self.name, self.lname, self.age)
            
# u=Person.User() 
# u.name='Shuhrat'
# u.lname='Dusnazarov'
# u.age=18  
# u.show()

# p=Person()
# p.name='Elyor'
# p.lname='Dusnazarov'
# p.age=24 
# p.show()


# /////////////////////////////////////////
# class Person:
#     def __init__(self):
#         self.name='Elyor'
#         self.lname='Dusnazarov'
#         self.age=21
                    
#     class User:
#         def __init__(self):            
#             self.name='Shuhrat'
#             self.lname='Dusnazarov'
#             self.age=20
            
# u_name = Person.User().name    
# u_lname = Person.User().lname    
# u_age = Person.User().age    

# p_name = Person().name
# p_lname = Person().lname
# p_age = Person().age

# print(u_name, u_lname, u_age)
# print(p_name, p_lname, p_age)


# ///////////////////////////////////////
# class Person:
    
#     def __init__(self, name, lname, age):
#         self.name=name
#         self.lname=lname
#         self.age=age
        
#     def show(self):
#         print(self.name, self.lname, self.age)        
    
#     class User:
#         def __init__(self, name, lname, age):
#             self.name=name
#             self.lname=lname
#             self.age=age
            
#         def show(self):
#             print(self.name, self.lname, self.age)
            

# p=Person(name='Elyor',lname='Dusnazarov',age=24)
# p.show()

# u=Person.User(name='Shuhrat',lname='Dusnazarov',age=21)
# u.show()


# /////////////////////////////////
# class Person: 
#     name='Elyor'
#     lname='Dusnazarov'
#     age=23 
    
#     def show(self):                     
#         print(self.name, self.lname, self.age)

# class Student(Person):
#     pass
# o=Student()
# o.show()

# //////////////////
class Person:
    def __init__(self):
        self.name='Elyor'
        self.lname='Dusnazarov'
        self.age=20

class Student(Person):
    pass

o=Student()
print(o.name, o.lname, o.age)






