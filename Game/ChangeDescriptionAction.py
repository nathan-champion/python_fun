from GameAction import GameAction

class ChangeDescriptionAction(GameAction):

    def __init__(self):
        super(ChangeDescriptionAction, self).__init__()

    def do(self, game, outcome):
        game.current_room.continual_description = outcome.result