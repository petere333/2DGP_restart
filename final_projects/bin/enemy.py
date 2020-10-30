from pico2d import *
from game_state import *
import time
from math import *
from random import *

enemy_bullets = []
enemies = []


class Enemy:

    image = None

    def __init__(self, sx, sy, destructTime):
        if Enemy.image is None:
            Enemy.image = load_image("../res/sprites_32.png")
        self.x, self.y = sx, sy
        self.dx, self.dy = 0, 0
        self.last_fire = time.time()
        self.angle = atan2(self.dy, self.dx)
        self.direction = 0
        self.duration = random()*2.0+3
        self.collides = False
        self.spawnedTime = time.time()
        self.destructTime = destructTime
        self.speed = 4
        if self.dx == 0 and self.dy == 0:
            self.direction = 12
        else:
            for i in range(-18, 6):
                if pi/12*(-6+-6-i)-pi/24 <= self.angle < pi/12*(-6+-6-i)+pi/24:
                    self.direction = i+18
                    break
        print("number of enemies : ", len(enemies)+1)

    def draw(self):
        Enemy.image.clip_draw(32*(self.direction+1), 320, 32, 32, self.x, self.y)

    def update(self):
        if 626 >= self.x+self.dx >= -26 and 826 >= self.y+self.dy >= -26:
            self.x, self.y = self.x+self.dx, self.y+self.dy
        now = time.time()
        if now-self.spawnedTime >= self.destructTime:
            tangle = atan2(-1, 0)
            self.dx = cos(tangle)*self.speed
            self.dy = sin(tangle)*self.speed
        if self.y < -16 or self.y > 816 or self.x < -16 or self.x > 616:
            self.collides = True

    def fire(self):
        global enemy_bullets
        now = time.time()
        if self.last_fire+self.duration < now:
            enemy_bullets.append(Enemy_Bullet(self.x, self.y-12, 0, -6))
            self.last_fire = now

    def __del__(self):
        print("number of enemies : ", len(enemies))


class CurveEnemy:

    image = None

    def __init__(self, sx, sy, destructTime, addi):
        if CurveEnemy.image is None:
            CurveEnemy.image = load_image("../res/sprites_32.png")
        self.x, self.y = sx, sy
        self.sx = self.x
        self.dx, self.dy = 0, 0
        self.last_fire = time.time()
        self.angle = atan2(self.dy, self.dx)
        self.direction = 0
        self.duration = random() * 2.0 + 3
        self.collides = False
        self.spawnedTime = time.time()
        self.destructTime = destructTime
        self.speed = 4
        self.additional = addi
        self.addi = addi
        if self.dx == 0 and self.dy == 0:
            self.direction = 12
        else:
            for i in range(-18, 6):
                if pi / 12 * (-6 + -6 - i) - pi / 24 <= self.angle < pi / 12 * (-6 + -6 - i) + pi / 24:
                    self.direction = i + 18
                    break
        print("number of enemies : ", len(enemies) + 1)

    def draw(self):
        CurveEnemy.image.clip_draw(32*(self.direction+1), 288, 32, 32, self.x, self.y)

    def update(self):
        if 626 >= self.x+self.dx >= -26 and 826 >= self.y+self.dy >= -26:
            self.x, self.y = self.x+self.dx, self.y+self.dy
        now = time.time()
        if now-self.spawnedTime >= self.destructTime and self.y > 200:
            self.dy = -6
        elif self.y <= 200 and self.sx <= 300:
            if self.dy >= -0.5:
                tx, ty = destructCurve(self.x, self.y, self.sx+600, 200, self.additional, 1, self.speed)
            elif self.dy <= 0.5:
                tx, ty = destructCurve(self.x, self.y, self.sx+300, 0, self.additional, 1, self.speed)
            self.dx = tx
            self.dy = ty

            self.additional += self.addi
        elif self.y <= 200 and self.sx > 300:
            if self.dy >= -0.5:
                tx, ty = destructCurve(self.x, self.y, self.sx-600, 200, self.additional, 0, self.speed)
            else:
                tx, ty = destructCurve(self.x, self.y, self.sx-300, 0, self.additional, 0, self.speed)
            self.dx = tx
            self.dy = ty
            self.additional += self.addi
        self.angle = atan2(self.dy, self.dx)
        if self.dx == 0 and self.dy == 0:
            self.direction = 12
        else:
            for i in range(-18, 6):
                if pi / 12 * (-6 + -6 - i) - pi / 24 <= self.angle < pi / 12 * (-6 + -6 - i) + pi / 24:
                    self.direction = i + 18
                    break
        if self.y < -16 or self.y > 816 or self.x < -16 or self.x > 616:
            self.collides = True

    def fire(self):
        global enemy_bullets
        now = time.time()
        if self.last_fire+self.duration < now:
            xSpeed = None
            ySpeed = None
            if self.dx == 0 and self.dy == 0:
                xSpeed = 0
                ySpeed = -6
            else:
                temp = atan2(self.dy, self.dx)
                xSpeed = cos(temp)*self.speed
                ySpeed = sin(temp)*self.speed
            enemy_bullets.append(Enemy_Bullet(self.x, self.y-12, xSpeed, ySpeed))
            self.last_fire = now

    def __del__(self):
        print("number of enemies : ", len(enemies))


class DivideEnemy:
    image = None

    def __init__(self, sx, sy, dxx, dyy, destructTime, en, divided):
        if CurveEnemy.image is None:
            CurveEnemy.image = load_image("../res/sprites_32.png")
        self.x, self.y = sx, sy
        self.sx = self.x
        self.dx, self.dy = dxx, dyy
        self.last_fire = time.time()
        self.angle = atan2(self.dy, self.dx)
        self.direction = 0
        self.duration = random() * 2.0 + 3
        self.collides = False
        self.spawnedTime = time.time()
        self.destructTime = destructTime
        self.speed = 4
        self.enabled = en
        self.divided = divided
        if self.dx == 0 and self.dy == 0:
            self.direction = 12
        else:
            for i in range(-18, 6):
                if pi / 12 * (-6 + -6 - i) - pi / 24 <= self.angle < pi / 12 * (-6 + -6 - i) + pi / 24:
                    self.direction = i + 18
                    break
        print("number of enemies : ", len(enemies) + 1)

    def draw(self):
        CurveEnemy.image.clip_draw(32*(self.direction+1), 224, 32, 32, self.x, self.y)

    def update(self):
        if 626 >= self.x+self.dx >= -26 and 826 >= self.y+self.dy >= -26:
            self.x, self.y = self.x+self.dx, self.y+self.dy
        now = time.time()

        if self.y < -16 or self.y > 816 or self.x < -16 or self.x > 616:
            self.collides = True

        if now-self.spawnedTime >= self.destructTime:
            if self.y >= 455:
                tangle = atan2(-1, 0)
                self.dx = cos(tangle)*self.speed
                self.dy = sin(tangle)*self.speed
            elif 445 <= self.y <= 455 and self.divided == 0:
                tangle = atan2(-2, 1)
                tangle2 = atan2(-2, -1)
                dxx1 = cos(tangle)*self.speed
                dxx2 = cos(tangle2)*self.speed
                dyy1 = sin(tangle)*self.speed
                dyy2 = sin(tangle2)*self.speed
                enemies.append(DivideEnemy(self.x, self.y, dxx1, dyy1, 0, False, 1))
                enemies.append(DivideEnemy(self.x, self.y, dxx2, dyy2, 0, False, 1))
                enemies.remove(self)
                del self
            elif 245 <= self.y <= 255 and self.divided == 1:
                tangle = atan2(-2, 1)
                tangle2 = atan2(-2, -1)
                dxx1 = cos(tangle)*self.speed
                dxx2 = cos(tangle2)*self.speed
                dyy1 = sin(tangle)*self.speed
                dyy2 = sin(tangle2)*self.speed
                enemies.append(DivideEnemy(self.x, self.y, dxx1, dyy1, 0, False, 2))
                enemies.append(DivideEnemy(self.x, self.y, dxx2, dyy2, 0, False, 2))
                enemies.remove(self)
                del self


    def fire(self):
        global enemy_bullets, enemies
        now = time.time()

        if self.last_fire+self.duration < now and self.enabled is True:
            xSpeed = 0
            ySpeed = 0
            if self.dx == 0 and self.dy == 0:
                xSpeed = 0
                ySpeed = -6
            else:
                temp = atan2(self.dy, self.dx)
                xSpeed = cos(temp)*6
                ySpeed = sin(temp)*6
            enemy_bullets.append(Enemy_Bullet(self.x, self.y-12, xSpeed, ySpeed))
            self.last_fire = now

    def __del__(self):
        print("number of enemies : ", len(enemies))

class Enemy_Bullet:
    image = None

    def __init__(self, x, y, dx, dy):
        if Enemy_Bullet.image is None:
            Enemy_Bullet.image = load_image("../res/bullet_monster_8.png")
        self.x, self.y = x, y
        self.dx = dx
        self.dy = dy
        self.crash = False
        print("number of enemy bullets : ", len(enemy_bullets)+1)

    def draw(self):
        Enemy_Bullet.image.draw(self.x, self.y)

    def update(self):
        if -10 < self.y+self.dy < 810 and -10 < self.x+self.dx < 610:
            self.x, self.y = self.x+self.dx, self.y + self.dy
        else:
            self.crash = True

    def __del__(self):
        print("number of enemy bullets : ", len(enemy_bullets))


def destructCurve(startX, startY, endX, endY, additional, mode, speed):
    tangle = None
    if mode == 1:
        tangle = atan2(endY-startY, additional)
    else:
        tangle = atan2(endY - startY, -additional)
    tx = cos(tangle)*speed
    ty = sin(tangle)*speed
    return tx, ty
