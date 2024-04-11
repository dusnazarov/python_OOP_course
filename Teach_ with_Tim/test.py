# ////////////////////////////////////////////////////
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
class Cat(Pet):
    def __init__(self, name, age, color):       
        super().__init__(name, age)       
        self.color = color
           
    def show(self):
        print(self.name, self.age, self.color)      
    
   
class Dog(Pet):        
    def show(self):
        print(self.name, self.age)    
    
c = Cat(name='Bob', age=14, color="black")
c.show()

d = Dog(name='Bill', age=9)
d.show()







    
 






    






    







