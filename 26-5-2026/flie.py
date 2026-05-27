# Polymorphism in python

# Polymorphism mean"many forms"in object-oriented programming(OOP)

# polymorphism allow the same method name to perform different task depending on the object or argument used.

#method of overloading
#method of overriding

#It also provide built in functions

#issublass()
#super()

#1.Method overloading

# Method overloading mean creating multiple methods with the same name but with different parameter.

class calculator:
    def multiply(self,a,b,c=1):
        return a*b*c

#object

calc=calculator()

print("multiplication of 2 numbers:",calc.multiply(2,4))

print("multiplication3 numbers:",calc.multiply(2,4,3))

# if only 2 ardument are passed,c takes default value 1.

# if 3 arguments are passed all value are multipled.

# same method name multiply() perform diffrent operations.

# 2.method of overriding

# method overriding occurs when a child class provides a specific implementation ofa method already defined in the parent class.

class animal:
    def speack(self):
        print("Animal makes a sound")

class Dog(animal):
    def speack(self):
        print("Dog barks")

class cat(animal):
    def speack(self):
        print("cat meow")

# object

a=animal()
d=Dog()
c=cat()

a.speack()
d.speack()
c.speack()

# Dog and Cat inherite from inherite from Animal.

#Both child classes override the speak() method.

#issubclass() function

# issubclass() is a built-in python used to check weather one function class is derived from another class.

#syntax issubclass(child_class,parent_class)

#It's return

#true-->if inheritance exists
#flase-->otherwise

class person:
    pass

class student(person):
    pass

#student inherites from person

#plymorphism in function

print(issubclass(student,person))

def add(a,b):
    return a+b

print("Addition of integers:",add(10,20))

print("concatenation of string:",add("Hello"," World"))


