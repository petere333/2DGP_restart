from pico2d import *
from random import *
import time

garbage = []



asteroid1 = None
asteroid2 = None
asteroid3 = None




class Space:
    x = None
    y = None
    speed = 0.5
    screen_out = False
    image_space = None

    def __init__(self, xp, yp):
        self.x = xp
        self.y = yp
        self.screen_out = False
        if Space.image_space is None:
            Space.image_space = load_image("../res/back.png")

    def update(self):
        if self.y >= -400:
            self.y -= self.speed
        else:
            self.screen_out = True

    def draw(self):
        Space.image_space.draw(self.x, self.y)


class Planet:
    x = None
    y = None
    speed = 1
    screen_out = False
    type = None
    planet1 = None
    planet2 = None
    planet3 = None

    def __init__(self, xp, yp, t):
        self.x = xp
        self.y = yp
        self.type = t
        self.screen_out = False
        if Planet.planet1 is None:
            Planet.planet1 = load_image("../res/planet1.png")
        if Planet.planet2 is None:
            Planet.planet2 = load_image("../res/planet2.png")
        if Planet.planet3 is None:
            Planet.planet3 = load_image("../res/planet3.png")

    def update(self):
        if self.y >= -225:
            self.y -= self.speed
        else:
            self.screen_out = True

    def draw(self):
        if self.type == 1:
            Planet.planet1.draw(self.x, self.y)
        elif self.type == 2:
            Planet.planet2.draw(self.x, self.y)
        elif self.type == 3:
            Planet.planet3.draw(self.x, self.y)


class Satellite:
    x = None
    y = None
    speed = 2.5
    screen_out = False
    type = None
    satellite1 = None
    satellite2 = None
    satellite3 = None

    def __init__(self, xp, yp, t):
        self.x = xp
        self.y = yp
        self.type = t
        if Satellite.satellite1 is None:
            Satellite.satellite1 = load_image("../res/satellite1.png")
        if Satellite.satellite2 is None:
            Satellite.satellite2 = load_image("../res/satellite2.png")
        if Satellite.satellite3 is None:
            Satellite.satellite3 = load_image("../res/satellite3.png")

    def update(self):
        if self.y >= -150:
            self.y -= self.speed
        else:
            self.screen_out = True

    def draw(self):
        if self.type == 1:
            Satellite.satellite1.draw(self.x, self.y)
        elif self.type == 2:
            Satellite.satellite2.draw(self.x, self.y)
        elif self.type == 3:
            Satellite.satellite3.draw(self.x, self.y)


class Background1:
    image_bg1 = []
    last_sat = 0
    time_next = 0

    def __init__(self):
        self.last_sat = time.time()
        self.time_next = randint(0, 40)*0.1 + 3
        self.image_bg1 = []
        self.image_bg1.append(Satellite(randint(50, 550), 200, randint(1, 3)))

    def update(self):
        for s in self.image_bg1:
            s.update()
        for s in self.image_bg1:
            if s.screen_out is True:
                garbage.append(s)
                self.image_bg1.remove(s)
                del s
        if self.last_sat+self.time_next < time.time():
            self.image_bg1.append(Satellite(randint(50, 500), 950, randint(1, 3)))
            self.last_sat = time.time()
            self.time_next = 3 + randint(0, 40)*0.1
        for i in range(len(garbage)):
            garbage.remove(garbage[-1])

    def draw(self):
        for s in self.image_bg1:
            s.draw()


class Background2:
    image_bg2 = []
    last_planet = 0
    time_next = 0

    def __init__(self):
        self.last_planet = time.time()
        self.time_next = 10 + randint(0, 40)*0.1
        self.image_bg2 = []
        self.image_bg2.append(Planet(randint(50, 550), 700, randint(1, 3)))

    def update(self):
        for p in self.image_bg2:
            p.update()
        for p in self.image_bg2:
            if p.screen_out is True:
                garbage.append(p)
                self.image_bg2.remove(p)
                del p

        if self.last_planet+self.time_next < time.time():
            self.image_bg2.append(Planet(randint(50, 550), 950, randint(1, 3)))
            self.last_planet = time.time()
            self.time_next = 10 + randint(0, 40)*0.1
        for i in range(len(garbage)):
            garbage.remove(garbage[-1])

    def draw(self):
        for p in self.image_bg2:
            p.draw()


class Background3:
    image_bg3 = []
    last_space = 0
    time_next = 0

    def __init__(self):
        self.last_space = time.time()
        self.time_next = 16
        self.image_bg3 = []
        self.image_bg3.append(Space(300, 400))
        self.image_bg3.append(Space(300, 1200))

    def update(self):
        for s in self.image_bg3:
            s.update()

        for s in self.image_bg3:
            if s.screen_out is True:
                garbage.append(s)
                self.image_bg3.remove(s)
                del s

        now = time.time()
        if self.last_space+self.time_next < now:
            self.image_bg3.append(Space(300, 1200))
            self.last_space = now
        for i in range(len(garbage)):
            garbage.remove(garbage[-1])

    def draw(self):
        for s in self.image_bg3:
            s.draw()

