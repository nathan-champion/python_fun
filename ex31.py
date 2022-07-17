bleeding = False

def bear_part():
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        if bleeding:
            print("However, you still bleed out.  Good job!")
        else:
            print("Bear runs away")



print("""You enter a dark room with two dorrs.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    bear_part()
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
    
else:
    print("You stumble around and fall on a knife.  What do you do?")
    print("1. Staunch the bleeding.")
    print("2. Go back to the bear part. ")
    knife = input("> ")

    if knife == "1":
        print("You use a nearby rock to staunch the wound.  It works!")
        print("You live to a ripe old age with a rock band-aid.  Good job!")
    elif knife == "2":
        bleeding = True
        bear_part()
    else:
        bleeding = True
        print("Your indecision allows you to bleed out.  Good job!")