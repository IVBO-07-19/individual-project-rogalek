import pygame as pg
from player import Player
from eventHandler import EventHandler

menu_running = True
game_running = False
width = 1280
height = 720
FPS = 60
pg.init()
pg.display.set_caption("Name of game")
sc = pg.display.set_mode((width, height))
eventHandle = EventHandler(game_running, menu_running)
clock = pg.time.Clock()
pg.display.update()
player = Player(20, 20, pg)
pg.mixer.init()
# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)
# defining a font
smallfont = pg.font.SysFont('Corbel', 35)
# this font
text = smallfont.render('start game', True, (255, 255, 255))
while True:
    while eventHandle.menu:
        clock.tick(FPS)
        mouse = pg.mouse.get_pos()
        eventHandle.setInputs(events=pg.event.get(), pg=pg, mouse=mouse)

        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pg.draw.rect(sc, color_light, [width / 2, height / 2, 140, 40])

        else:
            pg.draw.rect(sc, color_dark, [width / 2, height / 2, 140, 40])

            # superimposing the text onto our button
        sc.blit(text, (width / 2 + 50, height / 2))
        pg.display.flip()
        sc.fill((255, 255, 255))



    while eventHandle.game:
        clock.tick(FPS)
        eventHandle.setInputs(events=pg.event.get(), pg=pg, mouse=mouse)
        player.update()
        player.draw()
        pg.draw.rect(sc, (0, 0, 0), (0, 600, 1280, 720))
        pg.display.update()
        pg.display.flip()
        sc.fill((200, 200, 200))
