# List and tuple in python (Basic & Multility)

# List - Mutable

my_list=[10,20,30]

print("List:",my_list)

my_list[1]=99

print("List:",my_list)

my_list[3]=101

print("List:",my_list)

# Tuple-Immutable

my_list=(10,20,30)

print("Tuple:",my_tuple)

# string Formating

# Indexing and slicing

text = "python"

print("First letter :",text[0])
print("First Letter:",text[-2])

# slicing

print("First 3 Latter:", text[:3])
print("First Latter:", text[::3])

# Using List with Slicing and Formating

students=["Grisha","Isha","Kevanshi","Khevna","ved","shwet"]

print("First two students:",students[::2])

# string formating using list

for students in students:

    print(f"welcome,{students}")
