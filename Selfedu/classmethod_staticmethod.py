# # /////////////////////////////////////////
# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 10

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD

#     def get_coord(self):
#         return self.x, self.y

# v = Vector(1, 2)
# print(Vector.get_coord(v))
# print(Vector.validate(5))        


# /////////////////////////////////////////
# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 10

#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD

#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
         

#     def get_coord(self):
#         return self.x, self.y

# v = Vector(1, 20)
# print(Vector.get_coord(v))

# print(Vector.validate(6))


# /////////////////////////////////////////
# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 10

#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD

#     def __init__(self, x, y): 
#         self.x = x
#         self.y = y
         

#     def get_coord(self):
#         return self.x, self.y

#     @staticmethod
#     def norm2(x, y):
#         return x*x + y*y

# v = Vector(1, 200)
# print(Vector.get_coord(v))

# print(Vector.norm2(2, 6))
