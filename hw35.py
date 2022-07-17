import random
from sys import argv
from sys import exit

inventory = []
flags = []

def game_over(message):
    print(message)
    print("It looks like it's game over for you!")
    exit()

def collect_input(choices):
    while True:
        index = 1
        print("What will you do?")
        for item in choices:
            print(f"{index}. {item}")
            index += 1

        chosen = input("> ")
        if chosen in choices:
            return chosen
        else:
            try:
                index = int(chosen)
                if index >= 1 and index <= (len(choices)):
                    chosen = choices[index-1]
                    return chosen
            except:
                pass
            print(f"{chosen} is an unrecognized choice.")

def check_torch():
    if not "torch" in inventory:
        game_over("The room is pitch black.  You fumble until you trip and fall from a precipice to your death!")

def sword_room():
    check_torch()
    room_items = ["sword", "crown"]
    options = ["Go west"]

    if "sword" in inventory:
        room_items.remove("sword")
    if "crown" in inventory:
        room_items.remove("crown")

    print("You find yourself in a room with what appears to be a")
    print("shallow underground river.  There is a waterfall that")
    print("feeds the river from a source above your sight.  The")
    print("waterfall and cliff around it is too slippery to climb.\n")

    print("In the waterfall basin, you see a stone pedestal.")
    if "sword" in room_items:
        print("A sharp-looking sword rests embedded in the pedestal.")
        options.append("Take sword")
    if "crown" in room_items:
        print("A jeweled crown lies half submerged close to the pedestal.")
        options.append("Take crown")

    pick = collect_input(options)
    if pick == "Go west":
        start_room()
    elif pick == "Take crown":
        if not "sword" in inventory:
            game_over("As you bend down to pick up the crown, you nudge the sword.  It cuts you deeply and you bleed to death!")
        else:
            print("You pick up the jeweled crown and place it into your pack.")
            inventory.append("crown")
            sword_room()
    elif pick == "Take sword":
        print("You pull the sword from the pedestal and grip it tightly in your hand.")
        inventory.append("sword")
        sword_room()

def read_inscription():
    print("\n\nHere lies the chieftain Thain")
    print("Who first crossed the azure sea")
    print("To settle the verdant lands")
    print("And raised his ivory castle")
    print("In the midst of cerulean lake waters")
    print("And ruled wisely till the vermillion sun")
    print("Set on his long reign")
    print("And sent him to the ebon world below.\n\n")

def gems_pressed_correctly(pressed_gems):
    correct_gems = ["blue", "green", "white", "blue", "green", "red"]
    is_correct = False

    if len(pressed_gems) == len(correct_gems):
        print("They're the same size.")
        is_correct = True
        for i in range(0, len(pressed_gems)):
            if correct_gems[i] != pressed_gems[i]:
                print(f"But {correct_gems[i]} is not {pressed_gems[i]}")
                is_correct = False
                break
    else:
        print(f"{len(correct_gems)} is not the same length as {len(pressed_gems)}")
    return is_correct

def closeup_sarcophagus():
    options = ["Back away", "Read inscription"]
    print("You approach the sarcophagus in order to get a closer look at it.")
    print("There is an inscription at the foot of the tomb that reads:")
    read_inscription()

    if "opened" not in flags:
        print("Below the inscription there are five gems")
        print("Colored red, green, blue, white, and black.")
        print("The gems seem to be buttons that you can press.")
    else:
        print("The sarcophagus is opened, and there is a skeleton inside.")
        if "shield" not in inventory:
            print("It is holding a silver kite shield.")

    gems_pressed = []
    if "opened" not in flags:
        options.append("Press the red gem")
        options.append("Press the green gem")
        options.append("Press the blue gem")
        options.append("Press the white gem")
        options.append("Press the black gem")
    elif "shield" not in inventory:
        options.append("Take the shield.")

    pick = ""
    while pick != "Back away":
        pick = collect_input(options)

        if "red gem" in pick:
            print("You press the red gem.")
            gems_pressed.append("red")
        elif "green gem" in pick:
            print("You press the green gem.")
            gems_pressed.append("green")
        elif "blue gem" in pick:
            print("You press the blue gem.")
            gems_pressed.append("blue")
        elif "white gem" in pick:
            print("You press the white gem.")
            gems_pressed.append("white")
        elif "black gem" in pick:
            print("You press the black gem.")
            print("You hear a loud series of CLICK sounds as some mechanism")
            print("inside the sarcophagus resets itself.")
            
            if gems_pressed_correctly(gems_pressed):
                flags.append("opened")
                print("The sarcophagus opens.  Inside is a withered skeleton")
                print("Bearing a silver kite shield.")
                options.append("Take shield")
                options.remove("Press the red gem")
                options.remove("Press the green gem")
                options.remove("Press the blue gem")
                options.remove("Press the white gem")
                options.remove("Press the black gem")
            gems_pressed.clear()
        elif "inscription" in pick:
            read_inscription()
        elif "Take the shield" in pick:
            print("You take the shield.")
            options.remove("Take the shield.")
            inventory.append("shield")

    if pick == "Back away":
        gems_pressed.clear()
        ancient_tomb()
        


def ancient_tomb():
    check_torch()
    options = ["Go east", "Examine sarcophagus"]
    print("You are in a marble room.")
    print("Smooth pillars create a simulated hallway leading")
    print("To a beautiful polished sarcophagus at the far end")
    print("of this room.")
    pick = collect_input(options)
    if "east" in pick:
        goblin_room()
    elif "sarco" in pick:
        closeup_sarcophagus()



def final_room():
    options = ["Go south."]
    dragon_hp = 3
    shield_hp = 5
    print("You find yourself in an immense cavern.")
    print("The floor is practically covered in gold coins and precious gems.")
    print("Beyond the shadows you hear a loud snarl and two glowing eyes")
    print("appear in the distance.")  
    print("Deafening footsteps and the sound of the treasure shifting and flowing")
    print("echo throughout the cavern as the eyes emerge from the shadows to reveal") 
    print("that they belong to a huge red dragon!")
    print("With a roar that shakes the cavern, it lowers its gaze to you and adopts")
    print("a threatening posture.")
    
    if "shield" in inventory:
        options.append("Raise your shield.")
    if "sword" in inventory:
        options.append("Attack with your sword.")
    if "crown" in inventory:
        options.append("Offer the jeweled crown.")
    
    while True:
        pick = collect_input(options)
        if "south" in pick:
            print("As you turn to flee, the dragon roars and exhales a jet of white hot fire!")
            game_over("You burn to cinders immediately!")
        elif "Offer" in pick:
            print("You drop the crown from your pack in an effort to placate the")
            print("menacing dragon.  The dragon looks at it scornfully before")
            print("stepping on you.")
            game_over("You are crushed beneath its foot.")
        elif "Raise" in pick:
            flags.append("raised")
            options.remove("Raise your shield.")
        elif "Attack" in pick:
            print("You swing the sword in an effort to slice into the dragon!")
            if random.randrange(0, 2) == 0:
                print("Your sword arcs true and cuts the dragon!")
                dragon_hp -= 1
                if dragon_hp == 0:
                    print("You have slain the dragon!")
                    if "crown" in inventory:
                        print("You even managed to keep the crown!")
                    game_over("The treasure is all yours!")
        
        print("The dragon attacks!")
        if "raised" not in flags:
            print("The dragon's claws rend you apart!")
            game_over("Thankfully, you die quickly.")
        else:
            print("Your shield protects you from the attack!")
            shield_hp -= 1
            if shield_hp == 0:
                print("Your shield melts, and you barely throw it off before it takes")
                print("your arm as well!")
                flags.remove("raised")
            

def leaving_while_goblin_alive(pick):
    return "Go" in pick and "goblin" not in flags    

def goblin_room():
    check_torch()
    room_enemies = ["goblin"]
    options = ["Go north", "Go west", "Go south"]
    print("You are in an ivy-covered room.")
    print("To the west lies another offshoot passage")
    print("Beyond to the north goes deeper into the dungeon.")
    
    if not "goblin" in flags:
        print("A ferocious goblin armed with a club guards this room!")
        print("It approaches menacingly, looking for a fight!")
        options.append("Fight goblin")
    else:
        print("The goblin's corpse lies in the room center where you dispatched it.")

    pick = collect_input(options)
    if leaving_while_goblin_alive(pick):
        game_over("As you try to leave, the goblin attacks!  You have a deep gash and bleed to death!")
    else:
        if "south" in pick:
            start_room()
        elif "west" in pick:
            ancient_tomb()
        elif "north" in pick:
            final_room()
    if "Fight" in pick:
        if "sword" in inventory:
            print("You take the initiative and slash at the goblin!")  
            print("Luck is with you!  You chop off its head!  Its body")
            print("crumples to the floor and the threat is gone!")
            flags.append("goblin")
            goblin_room()
        else:
            print("You slowly approach the goblin, your lack of weapon")
            print ("in hand making you more timid.")
            game_over("The goblin quickly slashes at you!  You have a deep gash and bleed to death!")
    

def start_room():
    options = ["Go north", "Go east"]
    if "torch" in inventory:
        torch_phrase = """The walls are bare.  Aside from the torch you hold, 
the room is lit by the faint rays of the sun coming from the stairs
behind you."""
    else:
        torch_phrase = """There is a torch on the wall that lights 
the room, its orange light contrasting the white light 
from the sun shining down from the stairs behind you."""
        options.append("Take torch")
    
    print("You find yourself in the entrance to the dungeon.") 
    print("Behind you, the stairs lead up outside.  There is ")
    print("a passageway leading north and a passage leading") 
    print("east.\n")
    print(torch_phrase)
    pick = collect_input(options)
    if pick == "Go east":
        sword_room()
    elif pick == "Go north":
        goblin_room()
    elif pick == "Take torch":
        inventory.append("torch")
        start_room()


if len(argv) > 1:
    for i in range(1, len(argv)):
        inventory.append(argv[i])

print("You reach the bottom of the stairs and enter the dungeon.")
print("The air is cold and damp.  You are ready to begin your ")
print("adventure!\n")
random.seed()
start_room()
