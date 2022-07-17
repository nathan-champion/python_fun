from sys import argv

script, cereal, vegetable, meat = argv

faveCereal = "my favorite cereal is {}".format(cereal)
drink = input("What's your favorite drink: ")
print(f"My favorite vegetable is {vegetable}.")
print("My favorite meat is", meat)
print(faveCereal)
print(f"I also like to drink {drink}.")