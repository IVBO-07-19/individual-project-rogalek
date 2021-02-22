import pygame as pg
from player import Player
from eventHandler import EventHandler

FPS = 60

sc = pg.display.set_mode((1280, 720))
eventHandle = EventHandler()
clock = pg.time.Clock()
pg.display.update()
player = Player(20, 20, pg)
while 1:
    eventHandle.setInputs(events=pg.event.get(), pg=pg)
    player.update()
    player.draw()
    pg.draw.rect(sc, (0, 0, 0), (0, 600, 1280, 720))

    pg.display.update()
    sc.fill((200, 200, 200))
    clock.tick(FPS)
