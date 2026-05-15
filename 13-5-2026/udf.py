# all type of python function
# TNRN
def greet():
    print("welcome python students!!!")

greet()

#TSRN
def add(a,b):
    print("Addition =",a+b)

add(10,20)

#TNRS
def message():
    return"Hello Python!!!"
print(message())

#TSRS
def multiply (x ,y):
    return x * y
print(multiply(5,4))

#Diagram
#argument : TNRN
# return : TNRS , TSRN
# both : TSRS
#return ends function execution

def calc(a,b):
    return a+b,a-b
x,y = calc(10,5)

print(x)
print(y)

# in python , a list is used to store multplevalues in a single variable.

#Example

Marks = [78,52,98,24,100]

print(Marks)

# accessing elements
# using Index

numbers = [1,2,3,4,5,6]

print(numbers[0])
print(numbers[2])

#nagetive indexing

numbers = [1,2,3,4,5,6]

print(numbers[-1])
print(numbers[-2])

# changing list elements

numbers = [1,2,3,4,5,6]
numbers[1] = 20
print(numbers)

# list traversing using loop

numbers = [1,2,3,4,5,6]
for i in numbers:
    print(i)

# using range() with indexing

numbers = [1,2,3,4,5,6,7,8,9,10]
print("lengh of list:",len(numbers))
for i in range (len(numbers)):
    print("index:",i,"value:",numbers[i])

# add element at end of the list.

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.append(11)

print(numbers)

# inset() in list

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.insert(3,30)

print(numbers)

#remove elements

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.remove(10)

print(numbers)

# remove elements at end of the list

numbers =[1,2,3,4,5,6,7,8,9,10]

numbers.pop()

print(numbers)

# searching in list

numbers =[1,2,3,4,5,6,7,8,9,10]

print(numbers [1:4])

# sum of list Elements

numbers = [1,2,3,4,5,6,7,8,9,10]

total = 0

for i in numbers :

    total = i

print(total)
