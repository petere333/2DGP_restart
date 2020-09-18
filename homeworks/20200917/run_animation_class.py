from pico2d import *
from random import *

open_canvas()


class Boy:
    def __init__(self):
        self.x, self.y = randint(100, get_canvas_width()-100), randint(100, get_canvas_height()-100)
        self.dx, self.dy = random(), 0
        self.frame = randint(0, 8)
        self.image = load_image("../res/animation_sheet.png")

    def update(self):
        self.frame = (self.frame+1) % 8
        self.x += self.dx * 5
        self.y += self.dy * 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image("../res/grass.png")

    def draw(self):
        self.image.draw(400, 30)


def render_proc():
    global boy, grass, soccer_team
    clear_canvas()
    grass.draw()
    for b in soccer_team:
        b.draw()
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
            elif e.key == SDLK_LEFT:
                boy.dx -= 1
            elif e.key == SDLK_RIGHT:
                boy.dx += 1
            elif e.key == SDLK_UP:
                boy.dy += 1
            elif e.key == SDLK_DOWN:
                boy.dy -= 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                boy.dx += 1
            elif e.key == SDLK_RIGHT:
                boy.dx -= 1
            elif e.key == SDLK_UP:
                boy.dy -= 1
            elif e.key == SDLK_DOWN:
                boy.dy += 1
        elif e.type == SDL_MOUSEMOTION:
            boy.x, boy.y = e.x, get_canvas_height()-e.y-1


def logic_proc():
    global soccer_team
    for b in soccer_team:
        b.update()


def game_loop():
    global esc
    hide_cursor()
    while not esc:
        render_proc()
        event_proc()
        logic_proc()
        delay(0.03)


# main program

esc = False  # whether i try to escape
grass = Grass()
soccer_team = [Boy() for i in range(11)]
boy = soccer_team[0]
game_loop()
close_canvas()
