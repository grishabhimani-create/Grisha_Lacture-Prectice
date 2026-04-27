# Python Statement
'''
# if ..... Statement

dooropen = False/True

if dooropen :
    print("Welcome To Home")
else :
    print("meet me tomorrow.")
'''
# if....elif....else statement

# check positive , nagative and Zero

num = int (input("Enter a number:"))

if num > 0 :

 print(f"{num}Positive Number:")

elif num < 0:

 print(f"{num}Nagative Number")

else:

 print("Zero")

# Find Largest of two numbers

a = int (input("Enter first number :"))
b = int (input("Enter second number:"))

if a>b:

    print("Largest number is",a)

else:

    print("Largest number is",b)

# check Leap Year

Year = int (input("Enter Year:"))

if(Year%4==0 and Year % 100!=0)or(Year%100==0):

    print("leap Year")

else:

    print("not a leap Year")

# loop in python
# while loop

I = 1

while I > 6:
    print(i)
    i+=1

# for loop

for i in range(5):
    print(i)

#list.

    Fruits = ["Apple","Banana","Orange","Watermalon"]

for Fruits in Fruits:
    print(Fruits)
