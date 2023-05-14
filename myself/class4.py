# //////////////////////////////////////////////
# class A:
#     def __init__(self):
#         print('A in init')
# class B:
#     def __init__(self):
#         print('B in init')

# a=A()
# b=B()

# /////////////////////////////////////////////////////
# 2)  Agar voris classni  __init__(self) funksiyasini ishlatsek,  parent classni __init__(self) funksiyasi ishlamaydi.
# class A:
#     def __init__(self):
#         print('A in init')
# class B(A):
#     def __init__(self):
#         print('B in init')

# b=B()

# /////////////////////////////////////////////////
# 3) agar voris classni __init__() funksiyasi bo'lmasa parent class ham ishlovradi. 
# class A:
#     def __init__(self):
#         print('A in init')
# class B(A):
#     def show(self):
#        print('B')

# b=B()
# b.show()

#////////////////////////////////////////
# 4) A class ni hosalarini A().__init__() funksiyadan foydalanib B voris class ga o'tkazdik.
# class A:
#     def __init__(self):
#         print('A1 in init')
# class B(A):
#     A().__init__()
#     def __init__(self):
#         print('B1 in init')
# b1=B()

#//////////////////////////////////////////////////
# 5) 
class A:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(self.name)

class B(A):
    def __init__(self, lab):
        A.__init__(self,lab)

b1=B('aple')
b1.show()

