# Python oop student logic

# Topic covered:

# Class and object

class car:
    comp_name=None
    model=None
    color=None
    year=None

car1=car()
car2=car()

car1.comp_name="BMW"
car1.model="X5"
car1.color="Black"
car1.year=2024

car2.comp_name="BMW"
car2.model="M5"
car2.color="black"
car2.year=2026

print("Car 1 Details")

print("car1.comp_name")
print("car1.model")
print("car1.color")
print("car1.year")

# Student

class StudentData:
    std_name=None
    std_id=None
    std_age=None
    std_course=None

Student1=StudentData()
Student2=StudentData()

Student1.std_name="Krishna"
Student1.std_id="7045"
Student1.std_age=18
Student1.std_course="AI/ML"

print("Student 1 Details:")

print("Student1.std_name")
print("Student1.std_id")
print("Student1.std_age")
print("Student1.std_course")

class Student:
    def StudentData(self):
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        course=input("Enter course:")

        print("\n Student Details")
        print("Name:",name)
        print("Age:",age)
        print("course:",course)

S1=Student()
S2=Student()

S1.StudentData()
S2.StudentData()

# concept
# class blueprint/template
# object real instance
# student() object creation
# self Keyword
# self refers to current object

class Student:
    def setData(self,name,marks):

        self.name=name
        self.marks=marks

    def display(self):

        print("Name:",self.name)
        print("Marks:",self.marks)

S1=Student()

S1,setData("Krishna",45)
S1.display()

# Delete keyword

# Used for:

# delete variable
# delete object
# delete property

class Student:
    def show(self):
        print("Student object")

S1=Student()

S1.show()

del S1

class Student:
    def setData(self):
        self.name="Krishna"

S1=Student()

S1.SetData()

print(S1.name)

del S1.name

# Encapsulation

# Hiding Data from direct access

# Security

# data protection

class Student:

    def __init__(self):

        self.__marks=90

    def showMarks(self):
        print("Marks:",self.__marks)

S1=Student()

S1.showMarks()

# print(S1.__marks)
