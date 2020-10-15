import gfw
from pico2d import *
from player import *
from enemy import *
import title_state
import time

player = None
image_back = None

def enter():
    global player, image_back
    if image_back is None:
        image_back = load_image("../res/back.png")
    if player is None:
        player = Player()
    if len(enemies) == 0:
        enemies.append(CurveEnemy(301, 600, 10, 1))
        enemies.append(CurveEnemy(333, 600, 10, 2))
        enemies.append(CurveEnemy(365, 600, 10, 10))
        enemies.append(CurveEnemy(32, 600, 5, 4))
        enemies.append(CurveEnemy(64, 600, 5, 5))
        enemies.append(CurveEnemy(96, 600, 5, 20))

    pass


def update():
    global player, enemies, enemy_bullets, player_bullets
    player.update()
    for en in enemies:
        en.update()
        en.fire()
    for b in player_bullets:
        b.update()
    for eb in enemy_bullets:
        eb.update()

    for b in player_bullets:
        for en in enemies:
            if en.x-12 <= b.x <= en.x+12 and en.y-12 <= b.y <= en.y+12:
                b.crash = True
                en.collides = True

    for en in enemies:
        if en.collides:
            enemies.remove(en)
            del en
    for b in player_bullets:
        if b.crash:
            player_bullets.remove(b)
            del b

    for eb in enemy_bullets:
        if player.x-12 <= eb.x <= player.x+12 and player.y-12 <= eb.y <= player.y+12:
            eb.crash = True
            player.collides = True
    for eb in enemy_bullets:
        if eb.crash:
            enemy_bullets.remove(eb)
            del eb

    for en in enemies:
        if player.x-21 <= en.x <= player.x+21 and player.y-21 <= en.y <= player.y+21:
            player.collides = True

    if player.collides:
        del player
        player = None
        for b in player_bullets:
            player_bullets.remove(b)
            del b
        player_bullets = []
        for en in enemies:
            enemies.remove(en)
            del en
        enemies = []
        for eb in enemy_bullets:
            enemy_bullets.remove(eb)
            del eb
        enemy_bullets = []
        quit(0)


def draw():
    global player, player_bullets, enemy_bullets, enemies, image_back
    image_back.draw(300,400)
    player.draw()
    for en in enemies:
        en.draw()
    for b in player_bullets:
        b.draw()
    for eb in enemy_bullets:
        eb.draw()
    pass


def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.change(title_state)
        elif e.key == SDLK_LEFT:
            player.dx -= 5
        elif e.key == SDLK_RIGHT:
            player.dx += 5
        elif e.key == SDLK_UP:
            player.dy += 5
        elif e.key == SDLK_DOWN:
            player.dy -= 5
        elif e.key == SDLK_SPACE:
            player.fire()
    elif e.type == SDL_KEYUP:
        if e.key == SDLK_LEFT:
            player.dx += 5
        elif e.key == SDLK_RIGHT:
            player.dx -= 5
        elif e.key == SDLK_UP:
            player.dy -= 5
        elif e.key == SDLK_DOWN:
            player.dy += 5

def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
