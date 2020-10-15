from pico2d import *
from game_state import *
import time
import helper
from enemy import *

player_bullets = []


class Player:

    image = None

    def __init__(self):
        if Player.image is None:
            Player.image = load_image("../res/sprites_32.png")
        self.x = 300
        self.y = 50
        self.dx = 0
        self.dy = 0
        self.last_fire = time.time()
        self.duration = 0.5
        self.collides = False

    def draw(self):
        Player.image.clip_draw(0, 480, 32, 32, self.x, self.y)

    def update(self):
        if 584 >= self.x+self.dx >= 16:
            self.x += self.dx
        if 30 <= self.y+self.dy <= 130:
            self.y += self.dy

    def fire(self):
        global player_bullets
        now = time.time()
        if self.last_fire+self.duration < now:
            player_bullets.append(Player_Bullet(self.x, self.y+12))
            self.last_fire = now


class Player_Bullet:

    image = None

    def __init__(self, x, y):
        if Player_Bullet.image is None:
            Player_Bullet.image = load_image("../res/bullet_8.png")
        self.x, self.y = x, y
        self.dy = 5
        self.crash = False
        print("number of bullets : ", len(player_bullets)+1)

    def draw(self):
        Player_Bullet.image.draw(self.x, self.y)

    def update(self):
        if self.y+self.dy < 810:
            self.x, self.y = self.x, self.y + self.dy
        else:
            self.crash = True

    def __del__(self):
        print("number of bullets : ", len(player_bullets))