import in_game  # game state
import before_play  # title state
import after_play  # score state
from pico2d import *

current_state = 0
win_close = False

# current state 0=title state 1=game state

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
    elif current_state == 2:
        after_play.init()
        after_play.final_score = in_game.current_score
        temp = "Score gained by STRAIGHTIEE : %d" % in_game.catch_normal
        after_play.strings.append(temp)
        temp = "Score gained by CURVIEE : %d" % in_game.catch_curve
        after_play.strings.append(temp)
        temp = "Score gained by CLONEE : %d" % in_game.catch_divide
        after_play.strings.append(temp)
        temp = "Score gained by evasion : %d" % in_game.bullets_evade
        after_play.strings.append(temp)
        temp = "Total Score : %d" % after_play.final_score
        after_play.strings.append(temp)
        while after_play.end_result is False:
            after_play.handle_event()

            clear_canvas()
            after_play.draw()
            update_canvas()
            delay(0.01)

            after_play.update()

    if in_game.change_state is not None:
        current_state = in_game.change_state
        in_game.change_state = None
    if before_play.change_state is not None:
        current_state = before_play.change_state
        before_play.change_state = None
    if after_play.change_state is not None:
        current_state = after_play.change_state
        after_play.change_state = None
    if in_game.closing is True or before_play.closing is True or after_play.closing is True:
        win_close = True

close_canvas()
quit(0)
