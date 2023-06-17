# //////////////////////////
# class Point:
#     color = 'red'
#     circle = 2

# o1 = Point()
# o2 = Point()

# o1.color = 'black'
# o2.color = 'white'
# Point.color = 'green'

# print(Point.__dict__)
# print(o1.__dict__)
# print(o2.__dict__)


# # /////////// without self for Class ///////////////
# class Point: 

#     def get_print():
#         print('Hllo world')

# Point.get_print()

# # /////////// without self for Class ///////////////
# class Point: 

#     def get_print(first, last):
#         print(f'{first} {last}')

# Point.get_print('Elyor', 'Dusnazarov')


# # ///////// with self for object   ////////////////
# class Point: 

#     def get_print(self):
#         print(f'Hllo world {self}')

# a = Point()
# a.get_print()

# /////////////////////////////////////////
# class Point: 

#     def get_print(self):
#         print(f'Hllo world {self}')

# a = Point()
# Point.get_print(a)


# /////////////////////////////////////////
# class Point:
#     color = 'red'
#     circle = 2 

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
        
#     def get_coords(self):
#         return (self.x, self.y)        

# a = Point()
# a.set_coords(1, 2)
# print(a.get_coords())
# print(a.__dict__)
# f = getattr(a, 'get_coords')
# print(f())

# print('////////////////////////////')

# b = Point()
# b.set_coords(2, 3)
# print(b.get_coords())
# print(b.__dict__)
# f = getattr(b, 'get_coords')
# print(f())

