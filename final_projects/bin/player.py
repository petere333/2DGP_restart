from pico2d import *
import time
from enemy import *

player_bullets = []


class Player:

    image = None
    shot_sound = None

    def __init__(self):
        if Player.image is None:
            Player.image = load_image("../res/sprites_32.png")
        if Player.shot_sound is None:
            Player.shot_sound = load_wav("../sounds/shot.wav")
        self.x = 300
        self.y = 50
        self.dx = 0
        self.dy = 0
        self.last_fire = time.time()
        self.duration = 0.3
        self.collides = False
        self.invincible = False
        self.last_inv = 0
        self.life = 3
        self.cheating = False

    def draw(self):
        if self.invincible is False:
            Player.image.clip_draw(0, 480, 32, 32, self.x, self.y, 50, 50)
        else:
            Player.image.clip_draw(0, 448, 32, 32, self.x, self.y, 50, 50)

    def update(self):
        if 575 >= self.x+self.dx >= 25:
            self.x += self.dx
        if 30 <= self.y+self.dy <= 130:
            self.y += self.dy
        if self.invincible is True:
            if self.last_inv + 3 < time.time():
                self.invincible = False
        if self.cheating is True:
            self.invincible = True
            self.last_inv = time.time()

    def fire(self):
        global player_bullets
        now = time.time()
        if self.last_fire+self.duration < now:
            player_bullets.append(Player_Bullet(self.x, self.y+12))
            Player.shot_sound.set_volume(60)
            Player.shot_sound.play(1)
            self.last_fire = now


class Player_Bullet:

    image = None

    def __init__(self, x, y):
        if Player_Bullet.image is None:
            Player_Bullet.image = load_image("../res/bullet_8.png")
        self.x, self.y = x, y
        self.dy = 10
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