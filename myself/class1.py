# 1) ////////////////////////
# class Person:
#     name='Elyor'
#     lname='Dusnazarov'
#     age=25
#     print(name, lname, age) 
# Person

# 2) ////////////////////////////////////////
# class Person:
#     name="Elyor"
#     lname="Dusnazarov"
#     age=21
    
# o=Person()
# print(o.name, o.lname, o.age)

# 3) ///////////////////////////////////////////////////
# class Comp:
    
#     def config(self):
#         # print(self.name, self.lname, self.age)
#         print(o.name, o.lname, o.age)

# o = Comp()
# o.name = "Elyor"
# o.lname="Dusnazarov"
# o.age="23"
# o.config()

# 4)  //////////////////////////////////////////
# class Person:
#     def __init__(self):
#         self.name="Elyor"
#         self.lname="Dusnazarov"
#         self.age=25

#     def config(self):
#         print(self.name, self.lname, self.age)
# o=Person()
# o.config()


# 5) ///////////////////////////////////////////////////
class Comp:
    def __init__(self, name, lname, age):
        self.name=name
        self.lname=lname
        self.age=age

    def config(self):
        print(self.name, self.lname, self.age)

o = Comp('Elyor', 'Dusnazarov', 23)
o.config()















