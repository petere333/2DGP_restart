from pico2d import *


image = None
end_title = False
closing = False
change_state = None


def init():
    global image, end_title, closing, change_state

    end_title = False
    closing = False
    change_state = None
    image = load_image('../res/back.png')


def update():
    pass


def draw():
    image.draw(300, 400)


def handle_event():
    global end_title, closing, change_state
    evt = get_events()
    for e in evt:
        if e.type == SDL_QUIT:
            end_title = True
            closing = True
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            end_title = True
            closing = True
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
            change_state = 1
            end_title = True
