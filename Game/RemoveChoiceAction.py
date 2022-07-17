from GameAction import GameAction

class RemoveChoiceAction(GameAction):

    def __init__(self):
        super(RemoveChoiceAction, self).__init__()

    def do(self, game, outcome):
        for i in reversed(range(len(game.current_room.choices))):
            if game.current_room.choices[i].find(outcome.result) != -1:
                print ("FOUND!", game.current_room.choices[i])
                game.current_room.choices.remove(game.current_room.choices[i])
        