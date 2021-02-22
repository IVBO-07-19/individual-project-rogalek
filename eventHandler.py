import sys


class EventHandler:
    def __init__(self):
        pass

    def setInputs(self, events, pg):
        for e in events:
            if e.type == pg.QUIT:
                sys.exit()
