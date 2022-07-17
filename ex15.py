from sys import argv
#importing argv fromthe sys module
from sys  import argv
# we're storing the script name and the filename we just entered
script, filename = argv

# now, we're calling open using the passed-in filename and storing the resulting file
# to the txt variable
txt = open(filename)

# we're outputting the filename to the screen
print(f"Here's your file {filename}:")
#now we're printing out the entire contents of the file.
print(txt.read())
txt.close()

# we're prompting for user input
print("Type the filename again:")
# storing the user's input into a variable
file_again = input('> ')

# we're going to use the variable to open the file all again and store it in a different file var
txt_again = open(file_again)
# and we'll print out the contents like before.
print(txt_again.read())
txt_again.close()