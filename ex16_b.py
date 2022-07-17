# to use cmd line args, we should import it
from sys import argv

#let's store our script name and our script name.  Let's store the r/w mode.  NOPE!!!
script, filename = argv

print(f"{script} is going to do some file operations for you!")
print(f"If you pressed 'w' as your mode, enter some text!")
toWrite = input("> ")

file = open(filename, 'w')
file.write(toWrite)
file.close()


