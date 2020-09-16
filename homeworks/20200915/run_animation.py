from pico2d import *

open_canvas()

# variables
character = load_image("../res/animation_sheet.png")
grass = load_image("../res/grass.png")
x, y = get_canvas_width() // 2, 80  # current coordination
dx = 0  # delta x, speed
dy = 0  # delta y, speed
esc = False  # whether i try to escape
frame = 0  # current clip number


def render_proc():
    global frame, x, y, character, grass
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame+1) % 8


def event_proc():
    global esc, x, y, dx, dy
    evt = get_events()
    for e in evt:
        if e.type == SDL_QUIT:
            esc = True
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                esc = True
            elif e.key == SDLK_LEFT:
                dx -= 1
            elif e.key == SDLK_RIGHT:
                dx += 1
            elif e.key == SDLK_UP:
                dy += 1
            elif e.key == SDLK_DOWN:
                dy -= 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                dx += 1
            elif e.key == SDLK_RIGHT:
                dx -= 1
            elif e.key == SDLK_UP:
                dy -= 1
            elif e.key == SDLK_DOWN:
                dy += 1
        elif e.type == SDL_MOUSEMOTION:
            x, y = e.x, get_canvas_height()-e.y-1


def logic_proc():
    global x, y, dx, dy
    x += dx * 5
    y += dy * 5


def game_loop():
    global esc
    hide_cursor()
    while not esc:
        render_proc()
        event_proc()
        logic_proc()
        delay(0.01)


# main program


game_loop()
close_canvas()
