from GameAction import GameAction

class FlagRemoveAction(GameAction):

    def __init__(self):
        super(FlagRemoveAction, self).__init__()

    def do(self, game, outcome):
        game.flags.remove(outcome.result)