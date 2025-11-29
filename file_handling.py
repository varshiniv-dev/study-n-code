# write a program to open a file in python
import csv
file = open('text.py', "w")

# write a program to write a text file in python
file.write('hello world')
file.write('\nwelcome to python programming!')
file.write('\nthis ia a simple file handling example.\n')
file.close()

# write a program to read entire text file in python
file = open('text.py', "r")
f = file.read()
print(f)

# write a program to read text file line by line in python
file = open('text.py', "r")
f = file.readlines()
for line in f:
    print(line.strip())

# write a program to read a text file as a list in python
file = open('text.py', "r")
f = file.readlines()
print(f)
