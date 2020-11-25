from pico2d import *
import time

image = None
bgm = None
start_sound = None
end_title = False
closing = False
change_state = None
title_font = None
last_time = 0
blink = True


def init():
    global image, end_title, closing, change_state, title_font, last_time, blink, bgm, start_sound
    title_font = load_font("../res/score.ttf", 30)
    end_title = False
    closing = False
    change_state = None
    blink = True
    last_time = 0
    image = load_image('../res/back.png')
    start_sound = load_wav("../sounds/game_start.wav")
    bgm = load_music("../sounds/title_bgm.ogg")
    start_sound.set_volume(128)
    bgm.set_volume(60)
    bgm.repeat_play()


def update():
    global blink, last_time
    now = time.time()
    if last_time + 0.5 <= now:
        last_time = time.time()
        if blink is True:
            blink = False
        else:
            blink = True
    pass


def draw():
    global image, title_font, blink
    image.draw(300, 400)
    if blink is True:
        title_font.draw(100, 385, "Press Space Bar to Start", (255, 255, 255))


def handle_event():
    global end_title, closing, change_state, start_sound, bgm
    evt = get_events()
    for e in evt:
        if e.type == SDL_QUIT:
            end_title = True
            closing = True
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            end_title = True
            closing = True
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
            start_sound.play(1)
            bgm.stop()
            change_state = 1
            end_title = True
