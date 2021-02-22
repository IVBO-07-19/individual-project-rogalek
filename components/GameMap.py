import pygame
from random import *
class Map :
    def __init__(self, wd, hg):
        self.wd = wd
        self.hg = hg

    def getWidth(self):
       return self.wd

    def getHeight(self):
        return self.hg

class Shapes :
    def __init__(self):
        self.shapes = ['square', 'vertical_rect', 'gorisont_rect']

    def getShape(self):
        return self.shapes[randint(0, 2)]

pygame.init()
screen = pygame.display.set_mode((1280, 720))
x = 0 ; y =0 ; hg = 100 ; wd = 60
while x!=screen.get_width():
    shapes =Shapes()
    shape =shapes.getShape()
    if shape=="square":
        y = randint(0, 720)
        pygame.draw.rect(screen,(255,255,255),(x,y,x+hg,y+hg))
        x = x + hg

    elif shape =="vertical_rect":
        y = randint(0, 720)
        pygame.draw.rect(screen,(255,255,255),(x,y,x+wd,y+hg))
        x = x + wd
    elif shape=="gorisont_rect":
        y = randint(0, 720)
        pygame.draw.rect(screen,(255,255,255), (x, y, x + hg, y + wd))
        x = x + hg
        pygame.display.update()