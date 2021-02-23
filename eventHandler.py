import sys


class EventHandler:
    def __init__(self, game, menu):
        self.game = game
        self.menu = menu

    def setInputs(self, events, pg, mouse):

        for e in events:
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.MOUSEBUTTONDOWN and not self.game:

                # if the mouse is clicked on the
                # button the game is terminated
                if 1280 / 2 <= mouse[0] <= 1280 / 2 + 140 and 720 / 2 <= mouse[1] <= 720 / 2 + 40:
                    self.game = True
                    self.menu = False