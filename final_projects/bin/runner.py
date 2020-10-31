import in_game
import before_play
from pico2d import *

current_state = 0
win_close = False


open_canvas(600, 800)

while win_close is False:
    if current_state == 0:
        before_play.init()
        while before_play.end_title is False:
            before_play.handle_event()

            clear_canvas()
            before_play.draw()
            update_canvas()
            delay(0.01)

            before_play.update()

    elif current_state == 1:
        in_game.init()
        while in_game.endgame is False:
            in_game.handle_event()

            clear_canvas()
            in_game.draw()
            update_canvas()
            delay(0.01)

            in_game.update()

    if in_game.change_state is not None:
        current_state = in_game.change_state
        in_game.change_state = None
    if before_play.change_state is not None:
        current_state = before_play.change_state
        before_play.change_state = None
    if in_game.closing is True or before_play.closing is True:
        win_close = True

close_canvas()
quit(0)
