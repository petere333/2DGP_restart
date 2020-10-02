from pico2d import *
from game_state import *
import time
import helper

player_bullets = []


class Player:

    image = None

    def __init__(self):
        if Player.image is None:
            Player.image = load_image("../res/sprites_32.png")
        self.x, self.y = 300, 50
        self.dx, self.dy = 0, 0
        self.last_fire = 0

    def draw(self):
        Player.image.clip_draw(0, 480, 32, 32, self.x, self.y)

    def update(self):

        if 584 >= self.x+self.dx >= 16:
            self.x, self.y = self.x+self.dx, self.y+self.dy

    def fire(self):
        global player_bullets, player_bullets_count
        now = time.time()
        if self.last_fire+0.5 < now:
            player_bullets.append(Player_Bullet(self.x, self.y+12))
            self.last_fire = now
            print("number of bullets : ", len(player_bullets))

class Player_Bullet:
    image = None

    def __init__(self, x, y):
        if Player_Bullet.image is None:
            Player_Bullet.image = load_image("../res/bullet_8.png")
        self.x, self.y = x, y
        self.dy = 5
        self.crash = False

    def draw(self):
        Player_Bullet.image.draw(self.x, self.y)

    def update(self):
        if self.y+self.dy < 796:
            self.x, self.y = self.x, self.y + self.dy
        else:
            self.crash = True

    def __del__(self):
        print("number of bullets : ", len(player_bullets))