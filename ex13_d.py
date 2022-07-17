from sys import argv

script, a, b, c = argv

print(f"My script is {script}")
message = "my variables are {}, {}, and {}."
outputA = message.format(a, b, c)
outputB = message.format("guns", "hugs", "a whole lot of love")
print(message)
print(outputA)
print(outputB)