from components.physicBody import PhysicBody
from components.Rendering import Rendering


class Player(PhysicBody, Rendering):
    def __init__(self, x, y, pg):
        PhysicBody.__init__(self, x, y, pg)
        Rendering.__init__(self, pg)
        self.onGround = True
        self.sprites = pg.sprite.Group()

    def update(self):
        PhysicBody.update(self)
        keys_press = self.pg.key.get_pressed()

        self.hsp = int(keys_press[self.pg.K_d] - keys_press[self.pg.K_a])

        if self.y + self.vsp >= 500:
            while self.y < 500:
                self.y += 1
            self.vsp = 0
            self.onGround = True

        else:
            self.onGround = False

        if keys_press[self.pg.K_w] and self.onGround:
            self.vsp = -self.jumpForce

        self.x += self.hsp * self.spd
        self.y += self.vsp

    def draw(self):
        self.pg.draw.rect(self.sc, (255, 0, 0),
                          (self.x, self.y, 50, 100))
