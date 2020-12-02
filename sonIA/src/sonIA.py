class Bot(object):

    def __init__(self):
        pass

    def act(self, xdif, ydif, vel):
        if (ydif < 10 or xdif < 10):
            return 1
        if xdif < 15 and ydif > 10:
            return 0
        pass