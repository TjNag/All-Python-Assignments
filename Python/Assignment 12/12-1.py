class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    
class Teacher(Person):
    def __init__(self, n, a, e, r):
        self.name = n
        self.age = a
        self.exp = e
        self.res = r
    def display_data(self):
        print("Name of Teacher: ",self.name)
        print("Age of Teacher: ",self.age)
        print("Experience of Teacher: ",self.exp)
        print("Research Area of Teacher: ",self.res)

class Student(Person):
    def __init__(self, n, a, c, m):
        self.name = n
        self.age = a
        self.course = c
        self.marks = m
    def display_data(self):
        print("Name of Student: ",self.name)
        print("Age of Student: ",self.age)
        print("Course of Student: ",self.course)
        print("Marks of Student: ",self.marks)

name=input("Enter the name of Teacher: ")
age=int(input("Age of Teacher: "))
exp=int(input("Experience of Teacher: "))
res=input("Research Area of Teacher: ")
teach = Teacher(name, age, exp, res)
name=input("Enter the name of Student: ")
age=int(input("Age of Student: "))
course=input("Course of Student: ")
marks=int(input("Marks of Student: "))
stu = Student(name, age, course, marks)
teach.display_data()
stu.display_data()