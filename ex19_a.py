def add_and_print(n1, n2):
    result = n1 + n2
    print(f"The sum of {n1} and {n2} is {result}")

def subtract_and_print(n1, n2):
    result = n1 - n2
    print(f"The difference between {n1} and {n2} is {result}")


n1 = 3
n2 = 7

add_and_print(5, 5)
add_and_print(5 + 5, 5+5)
add_and_print(n1, n2)
add_and_print(n1-5, n1-3)
add_and_print(n1+n1, n2+n2)
add_and_print(n2, n1)
add_and_print(int(input("N1: ")), int(input("N2: ")))