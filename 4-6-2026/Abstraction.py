# Abstraction in OOP

# Abstraction is the process of hiding implementation details and showing only essential features to the user.

# Reduce complexity
# Increase security
# Improve code reusability

# An abstract class is a class that cannot be instantiend(object cannot be created directly.)

#1. abc

# Abstract Base Class

# It is built-in python module used to create abstract classes.
'''
class Shape(ABC):

ABC is a helper class used to make a class abstract.
'''
'''
from abc import ABC , abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog Bow Bow")

d = Dog()

d.sound()
'''
# you cannot create an object of an abstract class.

# Abstract class and Methods
'''
from abc import ABC , abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")

# Child Class

class Dog(Animal):

    def sound(self):
        print("Dog Bow Bow")

class Cat(Animal):

    def sound(self):
        print("Cat Meow")
        
d = Dog()

d.sound()
d.sleep()

c = Cat()

c.sound()
c.sleep()

# Abstract Class Shape with area()

from abc import ABC , abstractmethod

# Abstract Class

class Shape(ABC):

    @abstractmethod

    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def are(self):
        return self.length*self.width

class Circle(Shape):

    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(10 , 5)
c = Circle(19)

print("Rectangle area :",r.area())
print("Circle area:",c.area())
'''
# Add Perimeter() Method
'''
from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):

    def __init__(self , radius):
       self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return round(2 * 3.14 * self.radius , 3)

r = Rectangle(10 , 5)
c = Circle(10)

print("Rectangle area :" , r.area())
print("Rectangle perimeter :" , r.perimeter())
print("Circle area :" , c.area())
print("Circle perimeter :" , c.perimeter())
'''
# MLModel Abstract class

from abc import ABC , abstractmethod

class MLModel(ABC):
    @abstractmethod
    def train (self):
        pass

    @abstractmethod
    def predict(self):
        pass

# linearRegressionModel

class LinearRegressionModel(MLModel):

    def train(self):
        print("Training Linear Regressing Model")

    def predict(self):
        print("Predicting using Linear Regression")
class DecisionTreeModel(MLModel):

    def train(self):

        print("Training Decision Tree Model")

    def predict(self):

        print("Predicting using Decision Tree")

l = LinearRegressionModel()
d = DecisionTreeModel()

l.train()
l.predict()

d.train()
d.predict()











        










































    










    




 
