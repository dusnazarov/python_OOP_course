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
            return True
        return False

    def remove_student(self, student):                  
        self.students.remove(student)
        return True 
       

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 80)
s3 = Student("Jill", 19, 75)



course = Course("Science", 2)

# print(course.get_average_grade()) 
          
print(s1.get_grade())       
# print(course.students)
# print(course.add_student(s1))
# print(course.students)
# print(course.add_student(s2))
# print(course.students)
# print(course.add_student(s2))
# print(course.students)
# print(course.remove_student(s2))
# print(course.students)
# print(course.remove_student(s1))
# print(course.students)
