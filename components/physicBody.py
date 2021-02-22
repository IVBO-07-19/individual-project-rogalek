class PhysicBody(object):
    def __init__(self, x, y, pg):
        self.x = x
        self.y = y
        self.spd = 6
        self.grav = 3
        self.hsp = 0
        self.vsp = 0
        self.jumpForce = 40

    def update(self):
        self.vsp += self.grav