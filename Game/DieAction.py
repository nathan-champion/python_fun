
from GameAction import GameAction
from Death import Death


class DieAction(GameAction):

    def __init__(self):
        super(DieAction, self).__init__()

    def do(self, game, outcome):
        death = Death(outcome.result)
        game.current_room = death
