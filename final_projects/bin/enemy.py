from pico2d import *
from game_state import *
import time
from math import *
from random import *

enemy_bullets = []
enemies = []


class Enemy:

    image = None

    def __init__(self, sx, sy):
        if Enemy.image is None:
            Enemy.image = load_image("../res/sprites_32.png")
        self.x, self.y = sx, sy
        self.dx, self.dy = 0, -1
        self.last_fire = time.time()
        self.angle = atan2(self.dy, self.dx)
        self.direction = 0
        self.duration = random()*2.0+3
        self.collides = False
        for i in range(-18, 6):
            if pi/12*(-6+-6-i)-pi/24 <= self.angle < pi/12*(-6+-6-i)+pi/24:
                self.direction = i+18
                break
        print("number of enemies : ", len(enemies)+1)

    def draw(self):
        Enemy.image.clip_draw(32*(self.direction+1), 320, 32, 32, self.x, self.y)

    def update(self):
        if 584 >= self.x+self.dx >= 16:
            self.x, self.y = self.x+self.dx, self.y+self.dy
        if self.y <= 300:
            self.dy = -8
        if self.y < 16:
            self.collides = True

    def fire(self):
        global enemy_bullets
        now = time.time()
        if self.last_fire+self.duration < now:
            enemy_bullets.append(Enemy_Bullet(self.x, self.y-12))
            self.last_fire = now

    def __del__(self):
        print("number of enemies : ", len(enemies))


class Enemy_Bullet:
    image = None

    def __init__(self, x, y):
        if Enemy_Bullet.image is None:
            Enemy_Bullet.image = load_image("../res/bullet_monster_8.png")
        self.x, self.y = x, y
        self.dy = -3
        self.crash = False
        print("number of enemy bullets : ", len(enemy_bullets)+1)

    def draw(self):
        Enemy_Bullet.image.draw(self.x, self.y)

    def update(self):
        if self.y+self.dy > 4:
            self.x, self.y = self.x, self.y + self.dy
        else:
            self.crash = True

    def __del__(self):
        print("number of enemy bullets : ", len(enemy_bullets))
