from GameAction import GameAction

class FlagAddAction(GameAction):

    def __init__(self):
        super(FlagAddAction, self).__init__()

    def do(self, game, outcome):
        game.flags.append(outcome.result)