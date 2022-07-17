from sys import argv

if len(argv) != 2:
    print("Enter your name as a command line argument.")
    quit()

script, player_name = argv

def intro(name):
    print(f"Welcome, {name}!  We can start the game whenever you're ready.")
    print("1. I'm ready.")
    print("2. Give me a moment.")
    return input("> ")

def serve():
    print("Get ready to serve!")
    print("1. Gentle serve.")
    print("2. Hard serve.")
    print("3. Walk away.")
    return input("> ")

def response(adv):
    print("The return is headed your way.  How do you respond?")
    print("1. Gentle response.")
    print("2. Strong response.")
    response = input("> ")
    if response == "1":
        return 0
    elif response == "2":
        return 1
    else:
        print("Your incorrect choice caused you to make a bad response!")
        return -1


def game(service, player):
    advantage = 0
    if service == "1":
        print(f"""A soft serve from {player}.
        It looks like their opponent was expecting this.  
        {player}'s serve is well-returned.""")
    elif service == "2":
        print(f"""Holy cow, what a strong serve from {player}!
        Their opponent has barely enough time to react, but the serve
        is returned!""")
        advantage += 1
    else:
        print(f"""What an upset!  {player} is walking off the court, 
        never to be seen again!""")
        return False

    while advantage <= 2 and advantage > -1:
        advantage += response(advantage)
        
    if advantage > 2:
        print("You won!")
    elif advantage < 0:
        print("You lost!")

    return True

initial_response = "0"

while initial_response != "1":
    initial_response = intro(player_name)

print("Alright then, let's do this like Brutus!")
game_running = True

while game_running:
    game_running = game(serve(), player_name)
    