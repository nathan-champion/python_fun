from Room import Room

class Death(Room):

    def __init__(self, death_text):
        super(Death, self).__init__()
        self.name = "Death"
        self.death_text = death_text
    
    def enter(self, game):
        print(self.death_text)