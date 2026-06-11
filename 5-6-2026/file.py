# text file handaling in python

# what is file handeling?

'''
Text file handeling in Python is the process of creating , Opening , reading , writing , appending and managing temperory text files using python programs.

It allows data to be stared permenetly in files insted of temporary memory.
'''
# Defination of Modes of opening file in Python

'''
file modes are the different ways used to open a file in python for performing operations like reading , writing , appending or binary handeling.
'''
# Defination of I/O operation with files in python

'''
I/O operations in python are used to read data from a file and write data into a file
input operation : Reading data from a file
Output operation  writing data into a file
'''

# syntax
# file = open("File nme","Mode")

'''
mode    meaning

 r       read mode
 w      write mode
 a      append mode(add data at end)
 x      created new file
 rb     read binary file
 wb     write binary file
 rt     read and write
 at     append and read

'''

# 1. Read mode

# use to read data from file.

file = open("demo.txt","r")
content = file.read()
print(content)
file.close()

# 2. writemode

# use to write data into a file.

file = open("demo.txt","w")
file.write("\n Python file handeling !!!!")
file.close()

# 3. append mode()

# adds new Data at end of the file

file = open("demo.txt","a")
file.write("\n Python is easy to learn.")
file.close()

# 4. create new file()

file = open("newfile.txt","x")
file.close()

# I/O Operations

#Read files

file = open("demo.txt","r")
print(file.read())
file.close()

# Read one line at a time.
# Readlines()
# Readline()
file = open("demo.txt","r")
print(file.readlines())
print(file.readline())
file.close()

# Output Opration

# write text into file

file = open ("newfile.txt","w")
file.write("Hello Python !")
file.close()

# writelines()

file = open("newfile.txt","w")

lines=[
    "Line 1 : Python\n",
    "Line 2 : File Handeling\n",
    "Line 3 : Easy Learning\n"
    ]

file.writelines(lines)
file.close()

# Using with statement
# best method for file handeling because file closes automatically.

with open("newfile.txt","r")as file:
    content = file.read()
    print(content)

# Binary file handeling

# Used for images , audio , videos , etc......

file = open("newfile.txt","rb")
content = file.read()
print(content)
file.close()

# Read and write Binary file(rt)

file = open("newfile.txt","rt")
print(file.read())
file.write("python file hendaling")
file.close()

# create and read file

file = open("files.txt","w")
file.write("Hello Python !!!")
file.close()

file = open("files.txt","r")
print(file.read())
file.close()









































































           




























