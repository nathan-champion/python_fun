#print a string
print("Mary had a little lamb.")
#print a string, you can call .format on the hard-coded string and pass in a string.
print("Its fleece was white as {}.".format('snow'))
#print another string
print("And everywhere that Mary went.")
#you can multiply a string to print it several times
print("." * 10) # what'd that do?

#now we're assigning a character to a lot of strings.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#we're printing out every character in an extended string.
#watch end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8+ end9 + end10 + end11 + end12)