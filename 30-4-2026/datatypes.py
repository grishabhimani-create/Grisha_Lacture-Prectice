# python collecton
print("========python collacton datatypes=======")

# --------list---------

print("List Examples")

my_list = [10,20,30,40]

print("original list:",my_list)

# Mutability

my_list[0]=100

print("After Mutability list:",my_list)

# append()

my_list.append(50)

print("After use built-in function list:",my_list)

# max() and min()

print("max:",max(my_list))
print("min:",min(my_list))

# Remove duplicates meanully

unique = []
for i in my_list:
    if i not in unique:
        unique.append(i)
print("Unique list:",unique)

#-------Tuple------

print("Tuple Examples")

my_tuple = (1,2,3,4)

print("Tuple:",my_tuple)

# Immutable

# count occurrence

print("count of 3:",my_tuple.count(4))

# Swapping using tuple

a,b = 10,20
a,b = b,a

print("variable:",a,b)

#------set------

print("set Examples")

dataset = [1,2,3,4,5,6]

setdata = set(dataset)

print("set values:",setdata)

# set operator

a = {"1,2,3"}
b = {"3,4,5"}

print("Union:",a|b)

#------dictionary--------

print("Dict Examples")

student = {
    "name":"ved",
    "Marks":85
    }
print("student:",student)

student["marks"] = 90

print("Updated student:",student)

# thought loop create dictionary

for key,value in student.items():

    print(key,":",value)

# find topper

students = {"A":80,"B":95,"c":70,"D":45}

topper = max(students, key = students.get)

print("Topper :",topper)

print("Marks:", students[topper])

#-------list comprehension---------

print("list comprehension examples:")

numbers = [i for i in range(5)]

print("numbers:",numbers)

even = [i for i in range(10) if i % 2 == 0]

even = ("even number :",even)

#-------type casting example:----------

print("type casting Example:")

t = (1,2,3)

list_1 = list(t)

print(list_1)

print("list : ",list_1)

l = [1,2,3]

t_1 = tuple(l)

print("Tuple:",t_1)
