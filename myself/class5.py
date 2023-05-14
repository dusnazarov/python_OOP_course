
#////////////////////////
# class Person:
#   def __init__(self):
#     print('aple')

# class Student(Person):
#   def __init__(self, name, lname):
#     super().__init__()
#     self.name=name
#     self.lname=lname
    
#   def show_stu(self):
#     print(self.name,self.lname)
# x = Student("Mike",'jons')
# x.show_stu()

 
# //////////////////////////////////  
# class Person:
#   def __init__(self, name, lname, age):
#     self.name = name
#     self.lname=lname
#     self.age = age

#   def show_per(self):
#     print(self.name, self.lname)

# class Student(Person):
#   def __init__(self, name, lname, age, year):
#     super().__init__(name, lname, age) 

#     self.year = year
  
#   def show_stud(self):
#       print(self.name,self.lname, self.age, self.year)

# stud= Student("Elyor",'Dusnazarov', 23, 2015)
# stud.show_per()
# stud.show_stud()


#/////////////////////////////////////
# class Person:
#    def show_per(self):
#     print('aple1')

# class Student(Person):
#   def __init__(self, name, lname):
#       self.name=name
#       self.lname=lname
#   def show_stu(self):
#     print(self.name,self.lname)
# x = Student("Mike",'jons')
# x.show_stu()
# x.show_per()

# ///////////////////////////////////////////////
# class Person:
#    def __init__(self):
#     self.year=2019
#     self.age=6

# class Student(Person):
#   def __init__(self, name,lname):
#       super().__init__()
#       self.name=name
#       self.lname=lname
#   def show_stu(self):
#     print(self.name,self.lname)
# x = Student("Mike",'jons')
# x.show_stu()
# print(x.year,x.age)

#/////////////////////////////
# 6) 
# class Person:
#    def __init__(self):
#     self.year=2019
#     self.age=6

# class Student(Person):
#   def __init__(self):
#       super().__init__()

#   def show_stu(self):
#     print(self.name,self.lname)

    
# x = Student()
# x.name='Tom'
# x.lname='jons'
# x.show_stu()
# print(x.year, x.age)

# class Person:
#     def __init__(self, name, lname):
#         self.name=name
#         self.lname=lname
#     def show_per(self):
#         print(self.name, self.lname)
# class Student(Person):
#     def __init__(self, name, lname, year, age):
#         super().__init__(name, lname)
#         self.year=year
#         self.age=age
#     def show_stu(self):
#         print(self.year, self.age)
# b=Student('mike','jons', 2019, 5)
# b.show_per()
# b.show_stu()