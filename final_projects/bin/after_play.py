from pico2d import *
import time

image = None
end_result = False
closing = False
change_state = None
final_score = None
strings = []
index = 0
last_time = 0
last_blink = 0
score_font = None
blink = False


def init():
    global image, end_result, closing, change_state, score_font, final_score, strings, index, last_time, blink, last_blink
    score_font = load_font("../res/score.ttf", 30)
    end_result = False
    closing = False
    change_state = None
    index = 0
    last_time = 0
    last_blink = 0
    final_score = 0
    strings = []
    image = load_image('../res/back.png')
    blink = False


def update():
    global index, last_time, blink, last_blink

    if index < 5:
        now = time.time()
        if last_time+0.5 <= now:
            index += 1
            last_time = time.time()
    elif index == 5:
        now2 = time.time()
        if last_blink+0.1 <= now2:
            if blink is True:
                blink = False
            else:
                blink = True
            last_blink = time.time()


def draw():
    global index, image, score_font, strings
    image.draw(300, 400)
    for i in range(index):
        score_font.draw(50, 700 - i * 100, strings[i], (255, 255, 255))
    if index == 5 and blink is True:
        score_font.draw(50, 200, "Press Space Key to Return Title", (255, 255, 255))



def handle_event():
    global end_result, closing, change_state, index
    evt = get_events()
    for e in evt:
        if e.type == SDL_QUIT:
            end_result = True
            closing = True
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            if index < 5:
                index = 5
            else:
                change_state = 0
                end_result = True
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if index < 5:
                index = 5
            else:
                change_state = 0
                end_result = True
