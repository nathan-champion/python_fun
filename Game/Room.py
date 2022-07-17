from Choice import Choice

class Room(object):

    def __init__(self):
        self.initial_description = ""
        self.continual_description = ""
        self.entered = False
        self.name = "None"
        self.choices = []
        self.outcomes = []


    def read_from_open_file(self, file):
        self.name = file.readline().strip()
        
        self.initial_description = file.readline().rstrip()
        self.continual_description = file.readline().rstrip()

        for i in range(0, int(file.readline())):
            self.choices.append(file.readline().strip())
            read_outcomes = file.readline().strip().split('^')
            
            all_outcomes = []
            
            for outcome in read_outcomes:
                all_outcomes.append(outcome)

            self.outcomes.append(all_outcomes)
            
    def enter(self, game):
        if self.entered:
            text = self.continual_description
        else:
            text = self.initial_description
            self.entered = True
 
        print(text)

        choices = Choice(self.choices)
        action_index = choices.present(game)

        return self.outcomes[action_index]   


