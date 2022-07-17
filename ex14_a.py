from sys import argv

script, a, b = argv

print(f"""
Just to make sure, we're going to practice using some \"\"\".
We haven't been using it very much, so {script} is going to be
where we're using it.
""")

prompt = '> '
print("Can you enter some text?", end=' ')
finalInput = input(prompt)

print(f"""
Your first argument was {a}, and your second was {b}.  
You entered {finalInput} at the prompt.
""")