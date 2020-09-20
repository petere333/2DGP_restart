from pico2d import *
from random import *
import helper

open_canvas()


class Boy:
    def __init__(self):
        self.pos=(randint(100, get_canvas_width()-100), randint(100, get_canvas_height()-100))
        self.target=None
        self.delta=(0, 0)
        self.speed=5
        self.moving=False
        self.frame = randint(0, 8)
        self.image = load_image("../res/run_animation.png")

    def update(self):
        self.frame = (self.frame+1) % 8
        if self.moving:
            helper.move_toward_obj(self)
            if (self.pos[0] < self.target[0] + self.speed / 2 and self.pos[0] > self.target[0] - self.speed / 2) and (self.pos[1] < self.target[1] + self.speed / 2 and self.pos[1] > self.target[1] - self.speed / 2):
                self.moving = False
                self.speed = 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.pos[0], self.pos[1])


class Grass:
    def __init__(self):
        self.image = load_image("../res/grass.png")

    def draw(self):
        self.image.draw(400, 30)


def render_proc():
    global boy, grass
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


def event_proc():
    global esc, boy
    evt = get_events()
    for e in evt:
        if e.type == SDL_QUIT:
            esc = True
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                esc = True
        elif e.type==SDL_MOUSEBUTTONDOWN:
            if e.button==SDL_BUTTON_LEFT:
                target=(e.x, get_canvas_height()-e.y)
                helper.set_target(boy, target)
                boy.delta = boy.delta[1]
                if boy.moving:
                    boy.speed+=5
                boy.moving=True

def logic_proc():
    global boy,moving
    boy.update()

def game_loop():
    global esc
    while not esc:
        render_proc()
        event_proc()
        logic_proc()
        delay(0.03)


# main program

esc = False  # whether i try to escape
grass = Grass()
boy=Boy()
game_loop()
close_canvas()
