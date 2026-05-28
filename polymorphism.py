#super() function

# super() is used to call method or constructor of the parent class from the child class

class Employee:

    def __init__(self,name):
        self.name=name
        print("Employee constructor called.")

class Manager(Employee):
    def __init__(self,name,department):

        # calling parent constuctor

        super().__init__(name)

        self.department=department

        print("Managment constuctor called.")

    def display(self):
        print("name:",self.name)
        print("Department:",self.department)

m=Manager("Krishna","RK")

m.display()

# Manager inherits from employee
# super().__init__(name) calls the parent constructor.

#Parent class data is reused in child class.

#Polymorphism in class inheritance

class shape:
    def area(self):
        print("Area calculation")

class circle(shape):
    def __init__(self,redius):
        self.redius=redius

    def area(self):
        print("Area of circle:",3.14*self.redius*self.redius)

class Rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("area of Rectangle:",self.length*self.width)

c=circle(10)
r=Rectangle(5,10)

c.area()
r.area()

# Polymorphism with built-in function len()

#string

text="Python"

# list

numbers=[10,20,30,40,50]

#dictionary

student={"name":"zeel","age":20}

print("length of string:",len(text))
print("length of list:",len(numbers))
print("length of dict:",len(student))

# polymorphism using transport Interface

class Transport:
    def travel(self):
        print("Travel Method")

class Train(Transport):
    def travel(self):
        print("Train travels on tracks.")

class plane(Transport):
    def travel(self):
        print("Plane travels in air.")

t=Train()
p=Plane()

t.travel()
p.travel()

