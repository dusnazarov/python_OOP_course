# /////////////////////////////////////

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []


    def add_student(self, student):
        if len(self.students) < self.max_students:            
            self.students.append(student)   
                     
            return self.students
        return False
    
    def remove_student(self, student):                  
        self.students.remove(student)
        return self.students 

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
    

# create students
stu_1 = Student('Elyor', 25, 80)
stu_2 = Student('Mohinur', 22, 70)
stu_3 = Student('Lobar', 21, 90)
stu_4 = Student('Tohir', 20, 60)

# create a course
course_1 = Course('Maths', 4)


# add student to course
print(course_1.add_student(stu_1))
print(course_1.add_student(stu_2))
# print(course_1.add_student(stu_3))
# print(course_1.add_student(stu_4))

# remove student from the course
# print(course_1.remove_student(stu_1))
# print(course_1.revove_student(stu_2))
# print(course_1.remove_student(stu_3))
# print(course_1.remove_student(stu_4))

# get average grade of students
print(course_1.get_average_grade())


# # //////////////////////////////////////

# class Student:

#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
       
    
#     def get_grade(self):
#         return self.grade
    
    
# class Course:

#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []


#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return self.students
#         return False
    
#     def remove_student(self, student):
#         return self.students.remove(student)
    
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
    
# s1 = Student('Eyor', 24, 70 )
# s2 = Student('Mohinur', 21, 80 )
# s3 = Student('Tohir', 28, 60 )
# s4 = Student('Zohid', 18, 50 )

# c = Course('Physics', 5)

# c.add_student(s1)
# c.add_student(s2)
# c.add_student(s3)
# c.add_student(s4)

# # print(c.students)

# print(c.get_average_grade())


# # Iterate 
# # new_students = []
# # for instance in c.students:
# #     new_students.append(instance)

# # print(new_students)

# # we get name
# # new_students = []
# # for instance in c.students:
# #     new_students.append(instance.name)

# # print(new_students)