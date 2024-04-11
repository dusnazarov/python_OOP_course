# ////////////////////////////////////////////////////
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age       
        
#     def show(self):
#         print(f'My name is {self.name}, I am is {self.age} years old')

#     def speak(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age        
        
#     def show(self):
#         print(f'My name is {self.name}, I am is {self.age} years old')

#     def speak(self):
#         print("Brak")

# c = Cat(name='Bob', age=14)
# c.show()
# c.speak()

# d = Dog(name='Bill', age=9)
# d.show()
# d.speak()



# ////////////////////////////////////////////////////
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def show(self):
#         print(f'My name is {self.name}, I am is {self.age}')

 
# class Cat(Pet):
    
#     def speak(self):
#         print("Meow")    
 
# class Dog(Pet):
    
#     def speak(self):
#         print("Brak")

# p = Pet(name='Jone', age=21)
# p.show()


# c = Cat(name='Bob', age=14)
# c.show()
# c.speak()

# d = Dog(name='Bill', age=9)
# d.show()
# d.speak()


# ////////////////////////////////////////////////////
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f'My name is {self.name}, I am is {self.age}')
 
class Cat(Pet):
    def __init__(self, name, age, color):       
        super().__init__(name, age)       
        self.color = color
           
    def show(self):
        print(f'My name is {self.name}, I am is {self.age} years old and  I am {self.color}')
            
    
    def speak(self):
        print("Meow")    
 
class Dog(Pet):        
    def show(self):
        print(f'My name is {self.name}, I am is {self.age} years old.')
    
    def speak(self):
        print("Brak")

# p = Pet(name='Jone', age=21)
# p.show()


c = Cat(name='Bob', age=14, color="black")
c.show()
# c.speak()

d = Dog(name='Bill', age=9)
d.show()
# d.speak()

        