from sys import argv

script, filename = argv

outContents = input("Enter what you want to write to the file: ")
file = open(filename, 'w')
file.write(outContents)
file.close()

print(f"""
{script} wrote {outContents} 
to file {filename}!  Great job, one and all!
""")