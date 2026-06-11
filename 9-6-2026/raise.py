# raise keyword
'''
the raise keyword is used to manually trigger an excetion in Python.
It allows developers to stop program execution when an error condition occurs.
'''
# syntax

# raise Exception Type("Error message")

age = -5

if age < 0:
    raise ValueError("Age cannot be nagative")

# assert keyword in used for debugging and testing conditions.

'''
the accert keyword in used for debugging and testing conditions.
It check weather a condition is true.
If the condition is true->program continue.
If the condition is false->assertion is raised.
'''
# syntax
# assert condition ,"Error Message"
'''
num = -10

assert num > 0 , "Number must be positive"

print("valid number")
'''
# custom exception with try - except
'''
class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1000

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance.")
    print("withdrawal successfull.")

except InsufficientBalanceError as e:
    print("Error :" , e)

'''
# 1. check even number using Type Error and Value Error

def check_even():

    num = input("Enter an integer:")

if "." in num:
    raise TypeError("Input must be an integer")

if num % 2 != 0:
    raise ValueError("Number is odd")
print("Number is even.")

try:

    check_even()

except Exception as e:
    print("Error : " , e)

# student grade validation
'''
class invalidgradeerror(Exception):
    pass

try:
    grade=input(Enter grade:)

    assert grade ! = "","Grade input cannot be empty."

    if grade < 0 or grade > 100:
        raise valueError("Grade must be between 0 to 100")

    if grade < 40:

        raise InvalideGradeError("Student has failed.")

        print("student passed.")

except Assertion Error as e:
    print("Assertion Error:",e)

except Value Error as e:
    print("Value Error:",e)

except InvalideGradeError as e:
    print("InvalideGradeError:",e)

'''

# Tempreture convortor validation
'''
class HighTempretureError(Exception):
    pass

try:

    temp = float(input("Enter tempreture in celsius:"))

    if not isinstance(temp(int,float)):
        raise TypeError("Tempreture must be a number")

except -273 <= temp <= 10000 ("Tempreture out of valid range."):

if temp > 1000:
    raise HighTempretureError("Tempreture excced 1000C")

    print("Valid Tempreture:",temp,"C")

except TypeError as e:
    print("TypeError:",e)
    
except AssertionError as e:
    print("AssertionError:",e)

except HighTempretureError as e:
    print("HighTempretureError:",e)
'''











    
































        
        



















    


















    
