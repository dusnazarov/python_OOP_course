# class Employee:
#     pass

# emp_1 = Employee()
# emp_2 = Employee()

# # print(emp_1)
# # print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 5000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'test.User@company.com'
# emp_2.pay = 6000

# print(emp_1.email)
# print(emp_2.email)

#////////////////////////////////////////
# class Employee:    
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.'+ last + '@gmail.com'        
  
# emp_1 = Employee('elyor','dusnazarov', 5000)
# emp_2 = Employee('Test','User',6000)

# # print(emp_1)
# # print(emp_2)

# print(emp_1.email)
# print(emp_2.email)


#////////////////////////////////////////
class Employee:    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def user_email(self):
        return '{}'.format(self.email)          
       

emp_1 = Employee('elyor', 'dusnazarov', 5000)
emp_2 = Employee('Test', 'User', 6000)

print(emp_1.fullname())
print(emp_1.user_email())
print(emp_2.fullname())
print(emp_2.user_email())
















