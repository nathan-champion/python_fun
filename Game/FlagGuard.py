from Guard import Guard

class FlagGuard(Guard):

    def __init__(self):
        super(FlagGuard, self).__init__()

    def allowed(self, text, game):
        super(FlagGuard, self).allowed(text, game)
        try:
            return game.flags.index(self.type) > -1
        except:
            return False
