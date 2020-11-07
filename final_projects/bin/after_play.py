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
score_font = None

def init():
    global image, end_result, closing, change_state, score_font, final_score, strings, index, last_time
    score_font = load_font("../res/score.ttf", 30)
    end_result = False
    closing = False
    change_state = None
    index = 0
    last_time = 0
    final_score = 0
    strings = []
    image = load_image('../res/back.png')

def update():
    global index, last_time
    now = time.time()
    if last_time+0.5 <= now and index < 5:
        index += 1
        last_time = time.time()
    pass


def draw():
    global index, image, score_font, strings
    image.draw(300, 400)
    for i in range(index):
        score_font.draw(100, 700-i*100, strings[i], (255, 255, 255))



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
