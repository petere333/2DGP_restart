from pico2d import *
import time
from math import *
from random import *

enemy_bullets = []
enemies = []

catch_normal = 0
catch_curve = 0
catch_divide = 0
num_normal = 0
num_curve = 0
num_divide = 0
bullets_evade = 0
num_bullets = 0




class Enemy:

    image = None
    explode1 = None
    explode2 = None
    explode3 = None
    explode4 = None
    explode5 = None
    explode6 = None

    def __init__(self, sx, sy, destructTime):
        if Enemy.image is None:
            Enemy.image = load_image("../res/sprites_32.png")
        if Enemy. explode1 is None:
            Enemy.explode1 = load_image("../res/explode1.png")
        if Enemy. explode2 is None:
            Enemy.explode2 = load_image("../res/explode2.png")
        if Enemy. explode3 is None:
            Enemy.explode3 = load_image("../res/explode3.png")
        if Enemy. explode4 is None:
            Enemy.explode4 = load_image("../res/explode4.png")
        if Enemy. explode5 is None:
            Enemy.explode5 = load_image("../res/explode5.png")
        if Enemy. explode6 is None:
            Enemy.explode6 = load_image("../res/explode6.png")
        self.type = 1
        self.x, self.y = sx, sy
        self.dx, self.dy = 0, 0
        self.last_fire = time.time()
        self.angle = atan2(self.dy, self.dx)
        self.direction = 0
        self.duration = random()*2.0+3
        self.collides = False
        self.spawnedTime = time.time()
        self.destructTime = destructTime
        self.speed = 6
        self.score = 100
        self.exploding = 0
        if self.dx == 0 and self.dy == 0:
            self.direction = 12
        else:
            for i in range(-18, 6):
                if pi/12*(-6+-6-i)-pi/24 <= self.angle < pi/12*(-6+-6-i)+pi/24:
                    self.direction = i+18
                    break
        print("number of enemies : ", len(enemies)+1)

    def draw(self):
        if self.collides is False:
            Enemy.image.clip_draw(32*(self.direction+1), 320, 32, 32, self.x, self.y, 50, 50)
        else:
            self.image.clip_draw(0, 0, 50, 50, self.x, self.y, 50, 50)

    def update(self):
        if 635 >= self.x+self.dx >= -35 and 835 >= self.y+self.dy >= -35:
            self.x, self.y = self.x+self.dx, self.y+self.dy
        now = time.time()
        if now-self.spawnedTime >= self.destructTime:
            tangle = atan2(-1, 0)
            self.dx = cos(tangle)*self.speed
            self.dy = sin(tangle)*self.speed
            self.score = 150
        if self.y < -25 or self.y > 825 or self.x < -25 or self.x > 625:
            self.collides = True

        if self.exploding / 10 == 0 and self.exploding > 0:
            self.image = Enemy.explode1
        elif self.exploding / 10 == 1:
            self.image = Enemy.explode2
        elif self.exploding / 10 == 2:
            self.image = Enemy.explode3
        elif self.exploding / 10 == 3:
            self.image = Enemy.explode4
        elif self.exploding / 10 == 4:
            self.image = Enemy.explode5
        elif self.exploding / 10 == 5:
            self.image = Enemy.explode6

    def fire(self):
        global enemy_bullets
        now = time.time()
        if self.last_fire+self.duration < now:
            enemy_bullets.append(Enemy_Bullet(self.x, self.y-12, 0, -4))
            self.last_fire = now


class CurveEnemy:

    image = None
    explode1 = None
    explode2 = None
    explode3 = None
    explode4 = None
    explode5 = None
    explode6 = None

    def __init__(self, sx, sy, destructTime, addi):
        if CurveEnemy.image is None:
            CurveEnemy.image = load_image("../res/sprites_32.png")
        if CurveEnemy. explode1 is None:
            CurveEnemy.explode1 = load_image("../res/explode1.png")
        if CurveEnemy. explode2 is None:
            CurveEnemy.explode2 = load_image("../res/explode2.png")
        if CurveEnemy. explode3 is None:
            CurveEnemy.explode3 = load_image("../res/explode3.png")
        if CurveEnemy. explode4 is None:
            CurveEnemy.explode4 = load_image("../res/explode4.png")
        if CurveEnemy. explode5 is None:
            CurveEnemy.explode5 = load_image("../res/explode5.png")
        if CurveEnemy. explode6 is None:
            CurveEnemy.explode6 = load_image("../res/explode6.png")
        self.type = 2
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
        self.speed = 6
        self.additional = addi
        self.addi = addi
        self.score = 100
        self.exploding = 0
        if self.dx == 0 and self.dy == 0:
            self.direction = 12
        else:
            for i in range(-18, 6):
                if pi / 12 * (-6 + -6 - i) - pi / 24 <= self.angle < pi / 12 * (-6 + -6 - i) + pi / 24:
                    self.direction = i + 18
                    break

    def draw(self):
        if self.collides is False:

            Enemy.image.clip_draw(32*(self.direction+1), 288, 32, 32, self.x, self.y, 50, 50)
        else:
            self.image.clip_draw(0, 0, 50, 50, self.x, self.y, 50, 50)

    def update(self):
        if 635 >= self.x+self.dx >= -35 and 835 >= self.y+self.dy >= -35:
            self.x, self.y = self.x+self.dx, self.y+self.dy
        now = time.time()
        if now-self.spawnedTime >= self.destructTime and self.y > 220:
            self.dy = self.speed * -1
            self.score = 150
        elif self.y <= 220 and self.sx <= 300:
            if self.dy >= -0.5:
                tx, ty = destructCurve(self.x, self.y, self.sx+600, 200, self.additional, 1, self.speed)
            elif self.dy <= 0.5:
                tx, ty = destructCurve(self.x, self.y, self.sx+300, 0, self.additional, 1, self.speed)
            self.dx = tx
            self.dy = ty
            self.score = 200
            self.additional += self.addi
        elif self.y <= 220 and self.sx > 300:
            if self.dy >= -0.5:
                tx, ty = destructCurve(self.x, self.y, self.sx-600, 200, self.additional, 0, self.speed)
            else:
                tx, ty = destructCurve(self.x, self.y, self.sx-300, 0, self.additional, 0, self.speed)
            self.dx = tx
            self.dy = ty
            self.score = 200
            self.additional += self.addi
        self.angle = atan2(self.dy, self.dx)
        if self.dx == 0 and self.dy == 0:
            self.direction = 12
        else:
            for i in range(-18, 6):
                if pi / 12 * (-6 + -6 - i) - pi / 24 <= self.angle < pi / 12 * (-6 + -6 - i) + pi / 24:
                    self.direction = i + 18
                    break
        if self.y < -25 or self.y > 825 or self.x < -25 or self.x > 625:
            self.collides = True

        if self.exploding / 10 == 0 and self.exploding > 0:
            self.image = CurveEnemy.explode1
        elif self.exploding / 10 == 1:
            self.image = CurveEnemy.explode2
        elif self.exploding / 10 == 2:
            self.image = CurveEnemy.explode3
        elif self.exploding / 10 == 3:
            self.image = CurveEnemy.explode4
        elif self.exploding / 10 == 4:
            self.image = CurveEnemy.explode5
        elif self.exploding / 10 == 5:
            self.image = CurveEnemy.explode6

    def fire(self):
        global enemy_bullets
        now = time.time()
        if self.last_fire+self.duration < now:
            xSpeed = None
            ySpeed = None
            if self.dx == 0 and self.dy == 0:
                xSpeed = 0
                ySpeed = -4
            else:
                temp = atan2(self.dy, self.dx)
                xSpeed = cos(temp)*4
                ySpeed = sin(temp)*4
            enemy_bullets.append(Enemy_Bullet(self.x, self.y-12, xSpeed, ySpeed))
            self.last_fire = now


class DivideEnemy:
    image = None
    explode1 = None
    explode2 = None
    explode3 = None
    explode4 = None
    explode5 = None
    explode6 = None

    def __init__(self, sx, sy, dxx, dyy, destructTime, en, divided):
        if DivideEnemy.image is None:
            DivideEnemy.image = load_image("../res/sprites_32.png")
        if DivideEnemy.explode1 is None:
            DivideEnemy.explode1 = load_image("../res/explode1.png")
        if DivideEnemy.explode2 is None:
            DivideEnemy.explode2 = load_image("../res/explode2.png")
        if DivideEnemy.explode3 is None:
            DivideEnemy.explode3 = load_image("../res/explode3.png")
        if DivideEnemy.explode4 is None:
            DivideEnemy.explode4 = load_image("../res/explode4.png")
        if DivideEnemy.explode5 is None:
            DivideEnemy.explode5 = load_image("../res/explode5.png")
        if DivideEnemy.explode6 is None:
            DivideEnemy.explode6 = load_image("../res/explode6.png")
        self.type = 3
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
        self.speed = 6
        self.enabled = en
        self.divided = divided
        self.score = 100
        self.exploding = 0
        if self.divided > 0:
            self.score = 200
        if self.dx == 0 and self.dy == 0:
            self.direction = 12
        else:
            for i in range(-18, 6):
                if pi / 12 * (-6 + -6 - i) - pi / 24 <= self.angle < pi / 12 * (-6 + -6 - i) + pi / 24:
                    self.direction = i + 18
                    break

    def draw(self):
        if self.collides is False:
            if self.divided == 0:
                DivideEnemy.image.clip_draw(32 * (self.direction + 1), 224, 32, 32, self.x, self.y, 50, 50)
            else:
                DivideEnemy.image.clip_draw(32 * (self.direction + 1), 192, 32, 32, self.x, self.y, 50, 50)
        else:
            self.image.clip_draw(0, 0, 50, 50, self.x, self.y, 50, 50)

    def update(self):
        if self.exploding / 10 == 0 and self.exploding > 0:
            self.image = DivideEnemy.explode1
        elif self.exploding / 10 == 1:
            self.image = DivideEnemy.explode2
        elif self.exploding / 10 == 2:
            self.image = DivideEnemy.explode3
        elif self.exploding / 10 == 3:
            self.image = DivideEnemy.explode4
        elif self.exploding / 10 == 4:
            self.image = DivideEnemy.explode5
        elif self.exploding / 10 == 5:
            self.image = DivideEnemy.explode6

        if 635 >= self.x+self.dx >= -35 and 835 >= self.y+self.dy >= -35:
            self.x, self.y = self.x+self.dx, self.y+self.dy
        now = time.time()

        if self.y < -25 or self.y > 825 or self.x < -25 or self.x > 625:
            self.collides = True

        if now-self.spawnedTime >= self.destructTime:
            if self.y >= 455:
                tangle = atan2(-1, 0)
                self.dx = cos(tangle)*self.speed
                self.dy = sin(tangle)*self.speed
                self.score = 150
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
                ySpeed = -4
            else:
                temp = atan2(self.dy, self.dx)
                xSpeed = cos(temp)*4
                ySpeed = sin(temp)*4
            enemy_bullets.append(Enemy_Bullet(self.x, self.y-12, xSpeed, ySpeed))
            self.last_fire = now


class Enemy_Bullet:
    image = None

    def __init__(self, x, y, dx, dy):
        if Enemy_Bullet.image is None:
            Enemy_Bullet.image = load_image("../res/bullet_monster_8.png")
        self.x, self.y = x, y
        self.dx = dx
        self.dy = dy
        self.crash = False
        self.crashed_to_wall = False
        print("number of enemy bullets : ", len(enemy_bullets)+1)

    def draw(self):
        Enemy_Bullet.image.draw(self.x, self.y)

    def update(self):
        global bullets_evade, num_bullets
        if -10 < self.y+self.dy < 810 and -10 < self.x+self.dx < 610:
            self.x, self.y = self.x+self.dx, self.y + self.dy
        else:
            self.crash = True
            self.crashed_to_wall = True

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
