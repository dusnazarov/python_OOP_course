# /////////////   __init__(self) initialazion object /////////////////
# class Point:
#     color = 'red'
#     circle = 2

#     def __init__(self):
#         print('Call method __init__(self) ')
#         self.x = 0
#         self.y = 0

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
        
#     def get_coords(self):
#         return (self.x, self.y)        

# a = Point()
# print(a.__dict__)

# b= Point()
# print(b.__dict__)

# //////////////////////////////
# class Point:
#     color = 'red'
#     circle = 2

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
        
#     def get_coords(self):
#         return (self.x, self.y)        

# a = Point(x=5, y=6)
# print(a.__dict__)


# //////////// __del__(self)  finalization object //////////////////
# class Point:
#     color = 'red'
#     circle = 2

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __del__(self):
#         print("Delete instance :" + str(self))

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
        
#     def get_coords(self):
#         return (self.x, self.y)        

# a = Point(x=5, y=6)
# print(a.__dict__)
# print()






