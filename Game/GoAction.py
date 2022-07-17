from GameAction import GameAction

class GoAction(GameAction):

    def __init__(self):
        super(GoAction, self).__init__()

    def do(self, game, outcome):
        game.current_room = game.rooms[outcome.result]