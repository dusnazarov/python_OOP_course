# # #////////////////////////////////////////
# class Employee:  
#     raise_amt = 1.04  
      
#     def __init__(self,first,last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.'+ last + '@company.com'        
    
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last) 
    
#     def apply_raise(self):        
#         self.pay = int(self.pay * self.raise_amt)  

# class Developer(Employee):
#     pass  
        
# dev_1 = Employee('Corey','Schafer', 5000)
# dev_2 = Employee('Test','User', 6000)

# dev_1 = Developer('Corey','Schafer', 5000)
# dev_2 = Developer('Test','User', 6000)


# print(dev_1.email)
# print(dev_2.email)

# #////////////////////////////////////////
class Employee:  
    raise_amt = 1.04
      
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'        
    
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 
    
    def apply_raise(self):        
        self.pay = int(self.pay * self.raise_amt)  
        return self.pay
       
class Developer(Employee):
    raise_amt = 1.04   
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)      
        self.prog_lang = prog_lang

class Manager(Employee):   
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        
        if employees is None:
            self.employees = []
                  
        else:
            self.employees = employees           

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
         

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
                                    

       
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        
dev_1 = Developer('Elyor','Dusnazarov', 5000, 'python')
dev_2 = Developer('Test','User', 6000, 'java')
dev_3 = Developer('Shahnoza','Ulasova', 9000, 'javascript')
dev_4 = Developer('Mohinur','Qodirova', 10000, 'C++')

# mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])
mgr_1 = Manager('Sue', 'Smith', 9000)

# print(dev_1.fullname())
# print(dev_1.apply_raise())
# print(dev_1.prog_lang)
# print(mgr_1.email)

print(mgr_1.add_emp(dev_1))
print(mgr_1.employees)

print(mgr_1.add_emp(dev_2))
print(mgr_1.employees)

print(mgr_1.add_emp(dev_3))
print(mgr_1.employees)

print(mgr_1.add_emp(dev_4))
print(mgr_1.employees)

mgr_1.remove_emp(dev_3)
print(mgr_1.employees)

mgr_1.print_emps()


# #////////////////////////////////////////
# class Employee:  
#     raise_amt = 1.04
      
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.'+ last + '@company.com'        
    
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last) 
    
#     def apply_raise(self):        
#         self.pay = int(self.pay * self.raise_amt)  
#         return self.pay
       
# class Developer(Employee):
#     raise_amt = 1.04   
    
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)      
#         self.prog_lang = prog_lang

# class Manager(Employee):   
    
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
        
#         if employees is None:
#             self.employees = []
                  
#         else:
#             self.employees = employees
           

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
         

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
         
#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())
        
# dev_1 = Developer('Elyor','Dusnazarov', 5000, 'python')
# dev_2 = Developer('Test','User', 6000, 'java')
# dev_3 = Developer('Shahnoza','Ulasova', 9000, 'javascript')
# dev_4 = Developer('Mohinur','Qodirova', 10000, 'C++')

# mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])

# print(isinstance(dev_1, Developer ))
# print(isinstance(mgr_1, Developer ))

# print(issubclass(Developer, Employee))
# print(issubclass(Manager,Developer))






