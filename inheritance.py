# Hierarchical Inheritance

# Hierarchical Inheritance mean multipal child classes inherit from one parent class.

class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class cat(Animal):
    def meow(self):
        print("cat meow")

d=Dog()
c=cat()

d.eat()
d.bark()
c.eat()
c.meow()

# Hybrid Inheritance

# Hybrid Inheritance is a combination of multiple and diffent multilevel inheritance.

class A:
    def show(self):
        print("class A")

class B(A):
    def show(self):
        print("class B")

class C(A):
    def show(self):
        print("class C")
        
class D(C , B):
    def display(self):
        super().show()

obj=D()

obj.display()

# super() follow MRO(Method Resolution order)

# in class D(B,C),Python first check class B.

# type() function

# the type() function rturn the datatype of a variable or object.

a=10
b=5.5
c="Python"

print(type(a))
print(type(b))
print(type(c))

# dir() function

# the dir() function list all attributes and methods of a class or object.

class student:
    def __init__(self):
        self.name="krishna"

    def show(self):
        print("student Name:",self.name)

obj=student()

print(dir(obj))

# isinstance() function

# the isinstance function checks weather an object belong to a class.

class person:
    pass

obj = person()

print(isinstance(obj,person))

# help() function

# the help() function display the documentation string of a class or function.

class Demo():
    """This is a demo class"""

    def show(self):
        """This is method display message"""

help(Demo)
