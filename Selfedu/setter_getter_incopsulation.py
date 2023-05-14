# ////////////////////////////////
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y        

# pt = Point(1, 2)
# pt.x = 200
# pt.y = "coord_y"
# print(pt.x, pt.y)


# ////////////////////////////////
# class Point:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y        

# pt = Point(1, 2)
# print(pt._x, pt._y)

# /////////////// it does not work /////////////////
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y        

# pt = Point(1, 2)
# print(pt.__x, pt.__y)

# /////////////// it does not work /////////////////
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
        
#     def set_coord(self, x, y):
#         self.__x = x
#         self.__y = y

#     def get_coord(self):
#         return self.__x, self.__y
                

# pt = Point(1, 2)
# pt.set_coord(10, 20)
# print(pt.get_coord())

# /////////////// it does not work /////////////////
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        
    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coordinate must be number")

    def get_coord(self):
        return self.__x, self.__y 
                

pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())



        
        