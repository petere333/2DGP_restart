import gfw
from pico2d import *
from player import *

player = None


def enter():
    global player
    player = Player()
    pass


def update():
    global player
    player.update()
    for b in player_bullets:
        b.update()
    for b in player_bullets:
        if b.crash:
            player_bullets.remove(b)
            del b


def draw():
    player.draw()
    for b in player_bullets:
        b.draw()
    pass


def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_LEFT:
            player.dx -= 5
        elif e.key == SDLK_RIGHT:
            player.dx += 5
        elif e.key == SDLK_SPACE:
            player.fire()
    elif e.type == SDL_KEYUP:
        if e.key == SDLK_LEFT:
            player.dx += 5
        elif e.key == SDLK_RIGHT:
            player.dx -= 5


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
