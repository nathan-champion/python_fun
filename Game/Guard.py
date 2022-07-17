class Guard(object):

    def __init__(self):
        super(Guard, self).__init__()
        self.type = "" 

    def allowed(self, text, game):
        self.type = text
        return True
    