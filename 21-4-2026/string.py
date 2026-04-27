#python String Manipulation

S1 = 'Hello'
S2 = "Wold"
S3 = '''Multiline
String'''
S4 = r"Raw\n String"

print(S1)
print(S2)
print(S3)
print(S4)

# common String Method

S = "Hello,World!"

print(S.upper())
print(S.lower())
print(S.split())
print(S.endswith("!"))
print(S.startswith("H"))
print(S.find("Hello"))
print(S.count("l"))

# String Formatting

Name = "Alice"
age = 30

# f-string

print(f"Name:{Name},Age:{age}")

# .formal()

print("Name:{},Age:{}".format(Name,age))

# slicing

S="Hello,Python!!"

print(S[0])
print(S[9])
print(S[0:5])
print(S[::-1])

# Joining and Splitting in Python

words = ["python","is","awesome"]

print(" ".join(words))
print("_".join(words))

Splits = "a,b,c"

print(Splits.split(","))
