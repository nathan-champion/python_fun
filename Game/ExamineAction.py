from GameAction import GameAction

class ExamineAction(GameAction):

    def __init__(self):
        super(ExamineAction, self).__init__()

    def do(self, game, outcome):
        print(outcome.result)