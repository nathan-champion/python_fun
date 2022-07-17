
class Outcome(object):

    def __init__(self, string):
        self.type, self.result = string.split(':')

    def to_str(self):
        s = "{}:{}".format(self.type, self.result)
        return s