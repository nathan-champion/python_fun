from glob import escape


def get_input(num_options):
    option = 0
    while option <= 0 or option > num_options:
        try:
            option = int(input("> "))
        except:
            print("""I couldn't understand the input.  Please limit it to the 
            numbers for choices""")
    
    return option

class Scene(object):
    def __init__(self, name):
        self.name = name

    

    def enter(self, game):
        pass



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        self.death_message = ""
        self.flags = []
    
    def play(self):
        next_scene = "CentralCorridor"
        while next_scene != "GameOver":
            current_scene = self.scene_map.scenes[next_scene]
            print("\n")
            next_scene = current_scene.enter(self)

        print("Game over!")

    def set_death_msg(self, msg):
        self.death_message = msg
            


class Death(Scene):
    
    def __init__(self):
        super(Death, self).__init__("Death")

    def enter(self, game):
        print(game.death_message)
        return "GameOver"

class CentralCorridor(Scene):

    def __init__(self):
        super(CentralCorridor, self).__init__("CentralCorridor")

    def enter(self, game):
        print("You enter the central corridor")
        print("Here are the things to do:")
        print("1. Go to bridge")
        print("2. Go to armory")
        print("3. Go to escape pod")
        choice = get_input(3)


        if choice == 1:
            if "Bridge" in game.flags:
                return "TheBridge"
            else:
                print("The bridge is locked!  You can't get in!")
                return "CentralCorridor"
        elif choice == 2:
            return "LaserArmory"
        elif choice == 3:
            return "EscapePod"



class LaserArmory(Scene):
    def __init__(self):
        super(LaserArmory, self).__init__("LaserArmory")

    def enter(self, game):
        print("You are in the laser armory")
        print("Here are the things to do:")
        print("1. Pick up the laser bomb")
        print("2. Disable the bridge lock")
        print("3. Go to the central corridor")
        choice = get_input(3)

        if choice == 1:
            game.set_death_msg("""You pick up the laser bomb and accidentally 
                trigger it.  BOOM!!""")
            return "Death"
        elif choice == 2: 
            if "Bridge" not in game.flags:
                print("You disable the bridge lock.")
                game.flags.append("Bridge")
                return "LaserArmory"
            else:
                print("You have already disabled the bridge lock!")
                return "LaserArmory"
        elif choice == 3:
            print("You leave the armory.")
            return "CentralCorridor"
        

class TheBridge(Scene):

    def __init__(self):
        super(TheBridge, self).__init__("TheBridge")

    def enter(self, game):
        print("You are currently on the bridge")
        print("Here are the things to do:")
        print("1. Get a coffee")
        print("2. Activate the self destruct sequence.")
        print("3. Go back to the central corridor")
        choice = get_input(3)

        if choice == 1:
            print("You make yourself a cup of coffee.")
            return "TheBridge"
        elif choice == 2:
            if "Destruct" in game.flags:
                print("You press the destruct button again.")
                game.set_death_msg("""The computer interprets this as you 
                    wanting to blow up the ship right now.  BOOM!!""")
                return "Death"
            else:
                print("""You press the self destruct button.  You have a 
                limited time left to escape the ship!""")
                game.flags.append("Destruct")
                return "TheBridge"
        else:
            print("You exit the bridge")
            return "CentralCorridor"

class EscapePod(Scene):

    def __init__(self):
        super(EscapePod, self).__init__("EscapePod")

    def enter(self, game):
        print("You are in the escape pod.")
        print("Here are the things to do:")
        print("1. Escape the ship.")
        print("2. Go back to the central corridor.")
        choice = get_input(2)

        if choice == 1:
            if "Destruct" in game.flags:
                print("""You flee the ship in the escape pod.  Moments later,
                 the ship explodes!""")
                game.set_death_msg("You win!!")
                return "Death"
            else:
                print("You flee the ship in the escape pod.")
                game.set_death_msg("""The ship senses that you've left and 
                opens fire on you as you try to flee!  BOOM!!""")
                return "Death"
        else:
            print("You leave the escape pod")
            return "CentralCorridor"

class Map(object):

    def __init__(self):
        self.scenes = dict()

    def next_scene(self, scene_name):
        pass

    def add_scene(self, scene):
        self.scenes[scene.name] = scene

    def opening_scene(self):
        pass

death = Death()
starting_scene = CentralCorridor()
armory = LaserArmory()
bridge = TheBridge()
pod = EscapePod()


map = Map()
map.add_scene(starting_scene)
map.add_scene(death)
map.add_scene(armory)
map.add_scene(bridge)
map.add_scene(pod)
game = Engine(map)

game.play()