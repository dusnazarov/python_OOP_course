# # #////////////////////////////////////////
# class Employee: 
      
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
     
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
 

# emp_1 = Employee('Elyor','Dusnazarov')

# emp_1.first = 'Shuhrat'
# print(emp_1.fullname())


# #////////////////////////////////////////
# class Employee: 
      
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last        
    
                
#     @property 
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    

# emp_1 = Employee('Elyor','Dusnazarov')
# # emp_1.fullname = 'Shuhrat Dusnazarov'   # it does not work  becouse   @property decorators = read only -method
# print(emp_1.fullname)

# #////////////////////////////////////////
# class Employee:
          
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
        

#     @property 
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     @fullname.setter
#     def fullname(self, name):
#         # print(name)
#         first, last = name.split(' ')
#         # print(first, last)
      
#         self.first = first
#         self.last = last
    
# emp_1 = Employee('Elyor','Dusnazarov')
# emp_1.fullname = 'Shuhrat Dusnazarov'

# print(emp_1.fullname)

# #////////////////////////////////////////
# class Employee: 
      
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
        
    
#     @property 
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last

#     @fullname.deleter
#     def fullname(self):
#         print('Delete Name!')
#         self.first = None
#         self.last = None
    
# emp_1 = Employee('Elyor','Dusnazarov')

# emp_1.fullname = 'Elyor Dusnazarov'


# print(emp_1.fullname)

# del emp_1.fullname
# print(emp_1.fullname)


# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
        
# @property
# def fulname(self, amount):  
#     first, last = amount.split(' ')
    
#     self.first = first
#     self.last = last
#     print(self.last, self.first)


# emp1 = Employee('Elyor', 'Dusnazarov')

# emp1.fulname = 'Shuhrat Dusnazarov'

# print(emp1.fulname)


        
# /////////////////////////////
# def fulname(name):  
#     first, last = name.split(' ')
   
#     print(first, last)   

# fulname('Elyordus, Dusnazarov')


# /////////////////////////////
# class Post:

    
#     def fulname(name):  
#         first, last = name.split(' ')
   
#         print(first, last)   

# Post.fulname('Elyordus, Dusnazarov')

    

