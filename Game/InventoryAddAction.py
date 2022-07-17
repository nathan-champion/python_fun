
from GameAction import GameAction

class InventoryAddAction(GameAction):

    def __init__(self):
        super(InventoryAddAction, self).__init__()

    def do(self, game, outcome):
        print(f"You pick up {outcome.result} and put it into your pack")