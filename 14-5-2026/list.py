# write  a program to find the length of a 1D array without using built-in functions.

arr =[]

size=int(input("Enter array size:"))

for i in range(size):

    value=int(input(f"[{i}]="))

    arr.append(value)

count=0

for i in arr:
    count += 1

print("length of Array:",count)
print("original Array:",arr)

# write a program to find average of a 1D array without using built-in functions.

arr=[]

size = int(input("Enter array size:"))

for i in range(size):
    value=int(input(f"a[{i}]="))
    arr.append(value)

sum=0
count=0

for i in arr:
    sum += i
    count += 1

average = sum/count

print("Average of Array:",average)

# write program to perform addition operation of two 1D array and store it in another array.

arr1 = []
arr2 = []
result = []

size = int(input("Enter array size:"))

print("Enter arr1 Elements:")

for i in range(size):
    value = int(input(f"a[{i}]="))
    arr1.append(value)

print("Enter arr2 Elements:")

for i in range(size):
        value = int(input(f"a[{i}]="))
        arr2.append(value)

for i in range(size):
    result.append(arr1[i]+arr2[i])

print("Array Result:",result)

# create an array of numbers from 1 to 10

arr = []

#for i in range(1,11):
    
arr.append(i)

for i in arr:
    print(i * 2)

# take user input for a numbers.

arr = [10,20,30,40,50,60]

num = int(input("Enter number to search:"))

found = False

for i in range(len(arr)):
    if arr[i] == num:
        print("Element Index:",i)
        found = true
        break

if found == False:
    print("Not found Element:")

a =[]

n = int(input("Enter array size:"))
arr = []

for i in range(n):
    num = int(input("Enter element:"))
    a.append(num)

print("Even numbers are:")
for i in a:
    if i %2 == 0:
        print(i)

print("Odd numbers are:")
for i in a:
    if i % 2 != 0:
        print(i)

a=[]

n = int(input("Enter array size:"))
arr = []

for i in range(n):
    num = int(input("Enter numbers are:"))
    a.append(num)
    
print("First five elements:")
for i in range(5):
    print(a[i])

print("Alternate elements:")
for i in range(0, n, 2):
    print(a[i])

a=[]

n = int(input("Enter array size:"))
arr = []

for i in range(n):
    num = int(input("Enter numbers are:"))
    a.append(num)
    
print("First element:",a[0])

print("Last element:",a[n-1])

middle = n // 2
print("Middle element:",a[middle])


        
        
