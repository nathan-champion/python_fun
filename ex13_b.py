import sys

script, firstName, middleName, lastName = sys.argv

fmtString = "This script was {}, your complete name is {} {} {}"

outputA = fmtString.format(script, firstName, middleName, lastName)
outputB = fmtString.format(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])

print(f"Output A is {outputA}")
print(f"Output B is {outputB}")