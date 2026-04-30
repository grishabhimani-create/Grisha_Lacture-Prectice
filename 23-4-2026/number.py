# print number from 1 to 10

for i in range(1,11):

    print(i)

# print enen numbers

for i in range(1,21):
    if i%2 == 0:
        print(i)

# sum of first N natural numbers

n=10
total=0
for i in range(1,n+1):
    total +=i

print("sum:",total)

# while loop
n = 5
fact = 1

while n > 0:
    fact*=n
    n=-1

print("Factorial:",fact)

# pattern programms
# Right triagle.

rows= 5

for i in range(1,rows+1):
    print("*"*i)

# reverced triangles

rows = 5

for i in range (rows,0-1):
    print("*"*i)

# Nested loops

# Multiplication table

for i in range(1,6):
 for j in range(1,11):  
    print(i * j , end=" ")
    print()

# Break and continue statements

for i in range(1,10):
    if i == 5:
        break
    print(i)

for i in range(1,10):
    if i ==5:
        continue
        print(i)

# Reverse a number

num = 1234
rev = 0

while num > 0:

    calc = num % 10
    rev = rev*10+calc
    num//=10

print ("reversed:",rev)

# loop with string

text = "python"

for ch in text:
    print(ch)
