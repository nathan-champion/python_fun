from sys import argv
script, first, second, third = argv

print(f"The script is called {script}")
print("The first variable is:", first)
st = "The second variable is: {}"
st = st.format(second)
print(st)
print("Your third variable is:", third)