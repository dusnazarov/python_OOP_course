# /////////////////////////////////////////
# class Point:

#     def __new__(cls, *args, **kwargs):
#         print("Call __new__(cls)  for " + str(cls))

#     def __init__(self, x=0, y=0):
#         print("Call __init__  for " + str(self))
#         self.x = x 
#         self.y = y
        
# pt = Point(1, 2)
# print(pt)

# /////////////////////////////////////////
# class Point:

#     def __new__(cls, *args, **kwargs):
#         print("Call __new__  for " + str(cls))
#         return super().__new__(cls)

#     def __init__(self, x=0, y=0):
#         print("Call __init__  for " + str(self))

#         self.x = x 
#         self.y = y
        
# pt = Point(1, 2)
# print(pt)


# /////////////////////////////////////////

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    def __del__(self):
        DataBase.__instance = None
    
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connection to DateBase: {self.psw}, {self.port} ')

    def close(self):
        print(f'close connection to DateBase')

    def read(self):
        return "Datas from DataBase"
    
    def write(self, data):
        print(f'write to DataBase {data}')

db = DataBase('root', '1234', 80)
db2 =  DataBase('root2', '5678', 40)
print(id(db), id(db2))
 
    




        
        

