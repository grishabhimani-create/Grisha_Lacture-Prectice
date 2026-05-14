# set with Delete Keyword
'''
variable
objected
entire set
'''
'''
colors = {"red","blue","pink"}

print(colors)

del colors

print(colors)
'''
numbers = {1,2,3,4}

print(numbers)

# remove()

numbers.remove(2)

print(numbers)

# pop()

numbers.pop()

print(numbers)

#convert two list into dictonary using zip()
keys = ["name","Age","city"]

values = ["Alice","25","ahmedabad"]

data = dict(zip(keys,values))

print(data)

# python : functions , Recursion , lambda function , global keyword and multiple return values

# function

# function are reusable block of code used to perform a specific task.

# Reusability , cleaner code , better organization , Reducerepetion
def greet():

    print("Welcome python students!")

greet()

# function with parameter

def add(a , b):
    print(a + b)

add(10,20)
add(20,20)

#Recursion

# A function calling itself

#Factorial,tree structure , problem solving

#Base case , Recursive call

#Factorial

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# sun of numbers

def total(n):
    if n==0:
        return 0
    return n+total(n-1)
print(total(2))
#Anonymous/Lambda Function
#Lambda Function:
#small anonymous function
#written in one line
#no function name

#syntax

#lambda argument : expression

square = lambda x : x * x

print(square(5))

add = lambda a,b : a+b

print(add(10,20))

#list with lambda & map()

nums = [1,2,3,4,5]

result = list(map(lambda x : x * 2 , nums))

print(result)

# List with lambda & filter()

nums = [1,2,3,4,5,6]

odd = list(filter(lambda x: x % 2 != 0 , nums))

print(odd)

# global keyword

# variable created outside function are called global variables

x = 10

def show():
    print(x)

show()

count = 0

def increment ():
    global count
    count += 1

increment()
increment()
increment()

print(count)

# return multiple values

#python function can return : single value , multiple values

# multiple value are returned as tuple.

def calc(a , b):
    return a + b , a-b
result = calc(10 , 5)

print(result)

def students():
    name="krishna"
    marks = 90
    return name , marks

result1 , result2 = students()

print(result1)
print(result2)

count = 10

def write(str):
    global count
    count  +=1
    return str , count

print(write("Hello python !!!"))
