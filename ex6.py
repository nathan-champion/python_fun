# making an int variable
types_of_people = 10
# making a formatted string with the types_of_people variable
x = f"There are {types_of_people} types of people"

# making some strings
binary = "binary"
do_not = "don't"
# making a string and formatting it with the binary and do_not variables
y = f"Those who know {binary} and those who {do_not}"

# printing x
print(x)
# printing y
print(y)

# formatting a string with x and printing
print(f"I said: {x}")
# formatting a string with y and printing, with '' around it.
print(f"I also said: '{y}'")

# delcaring bool
hilarious = False
# making another string.  Perhaps with an empty {} to add a parameter
joke_evaluation = "Isn't that joke so funny?! {}"
# we're calling a function on the string above and passing hilarious as an argument
print(joke_evaluation.format(hilarious))

# we're making a string
w = "This is the left side of..."
# we're making another string
e = "a string with a right side."

# we're adding w and e together and printing the resulting string
print(w + e)