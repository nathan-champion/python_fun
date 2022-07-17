from sys import argv

script, iters, inc = argv

stuff = ["a", 'b', "c", 'd']

iters = int(iters)
inc = int(inc)

def loop(max, incr):
    i = 0 
    numbers = []

    

    for i in range(0, max, incr):
        print(f"At the top of i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

loop(iters, inc)
print("Done")