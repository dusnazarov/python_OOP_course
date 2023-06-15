# /////////////////////////
# class  Person:
#     number_of_people = 0

#     def __init__(self, name):
#         self.name = name

# p1 = Person("Tim")
# p2 = Person("Jone")

# print(p1.number_of_people)
# print(Person.number_of_people)


# #/////////////////////////////////
# class  Person:
#     number_of_people = 0
#     GRAVITY = -9.8

#     def __init__(self, name):
#         self.name = name
#         Person.number_of_people += 1


# p1 = Person("Tim")
# print(Person.number_of_people)
# p2 = Person("Jone")
# print(Person.number_of_people)
# p3 = Person('Joush')
# print(Person.number_of_people)
# p4 = Person('Jems')
# print(Person.number_of_people)

# print(Person.GRAVITY)

#/////////////////////////////////
class  Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()      
        
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people +=1 
        


p1 = Person("Tim")
print(Person.number_of_people_())
p2 = Person("Mike")
print(Person.number_of_people_())
p3 = Person("Sou")
print(Person.number_of_people_())
p4 = Person("Jems")
print(Person.number_of_people_())




