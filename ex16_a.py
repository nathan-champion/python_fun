from sys import argv

script, filename = argv

file = open(filename, mode='w')

file.write(input("Line1: "))
file.write(input("Line2: "))
file.close();

file = open(filename, mode='r')
print(file.read())
file.close()