from sys import argv

def do_the_thing(with_the_stuff):
    print(f"Doin the thing: {with_the_stuff}!")
    result = int(with_the_stuff) * 2
    print(f"Did the thing, and it came out as: {result}!")

script, stuff = argv

print("Doin' it with argv!")
do_the_thing(stuff)

print("Doin' it with input!")
do_the_thing(input("Integer, please! "))