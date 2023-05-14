
#////////////////////////////////////////////
# class User:
#     def __init__ (self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
    
#     def show_details(self):
#         print("Personal Details")
#         print("")
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Gender: ", self.gender)

# q=User("John",24,"male")
# q.show_details()

#////////////////////////////////////////////
# Parent Class
# class User:
#     def __init__ (self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
    
#     def show_details(self):
#         print("Personal Details")
#         print("")
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Gender: ", self.gender)

# # Chaild Class
# class Bank(User):
#     def __init__(self,name, age, gender):
#         super().__init__(name,age,gender)

# q=Bank("Adam",32,"male")
# q.show_details()

#///////////////////////////////////////////
# Parent Class
# class User:
#     def __init__ (self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
    
#     def show_details(self):
#         print("Personal Details")
#         print("")
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Gender: ", self.gender)

# Chaild Class
# class Bank(User):
#     def __init__(self,name, age, gender):
#         super().__init__(name, age, gender)

# q=Bank("Adam",22,"male")
# q.show_details()


#///////////////////////////////////////////
# Parent Class
class User:
    def __init__ (self, name, lname, age, gender, phone):
        self.name=name
        self.lname=lname
        self.age=age        
        self.gender=gender
        self.phone=phone
    
    def show_details(self):       
        print("------------------------")
        print("Your Personal Details")
        print("Name :", self.name)
        print("Last Name :",  self.lname)
        print("Age :", self.age)
        print("Gender: ", self.gender)
        print("Phone: ", self.phone)


# Chaild Class
class Bank(User):
    def __init__(self, name, lname, age, gender, phone):
        super().__init__(name, lname, age, gender, phone)
        self.balance=0

    def deposit (self, amount):
        self.amount=amount
        self.balance=self.balance + self.amount
        print(f"{self.name} {self.lname},  Your Account balance has been updated : $", self.balance)

    def withdraw(self, amount):
        self.amount=amount
        if self.amount > self.balance:
            print(f"{self.name}  {self.lname},  Your Insufficient Funds I balance Available : $", self.balance)
        else:
            self.balance=self.balance-self.amount
            print(f"{self.name} {self.lname}, Your Account balance has been updated : $", self.balance)

def view_balance(self):
    self.show_details()
    print("Account balance : $", self.balance)

    
name = input('Enter Name: ')
lname = input('Enter Last Name: ')
gender = input('Enter Gender: ')
age = int(input('Enter Age: '))
phone = int(input('Enter Phone: '))

q=Bank(name, lname, gender, age,  phone)
q.show_details()

deposit = int(input("Enter Deposit: "))
q.deposit(deposit)
withdraw = int(input('Enter withdraw: '))
q.withdraw(withdraw)