import curses
import os

def board_cursor_controller(draw_controller, screen):
    if draw_controller.selector == curses.KEY_RIGHT:
        draw_controller.cursor[1] += 4
        if draw_controller.cursor[1] > 40:
            draw_controller.cursor[1] = 32
    elif draw_controller.selector == curses.KEY_LEFT:
        draw_controller.cursor[1] -= 4
        if draw_controller.cursor[1] < 32:
            draw_controller.cursor[1] = 40
    elif draw_controller.selector == curses.KEY_UP:
        draw_controller.cursor[0] -= 2
        if draw_controller.cursor[0] < 10:
            draw_controller.cursor[0] = 14
    elif draw_controller.selector == curses.KEY_DOWN:
        draw_controller.cursor[0] += 2
        if draw_controller.cursor[0] > 14:
            draw_controller.cursor[0] = 10
    screen.addstr(draw_controller.cursor[0], draw_controller.cursor[1], "*", curses.A_BLINK)

def draw_board(screen, board, y, x):
    screen.addstr(y, x,board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    screen.addstr(y+1, x-2,"-------------")
    screen.addstr(y+2, x,board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    screen.addstr(y+3, x-2,"-------------")
    screen.addstr(y+4, x,board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def environment_controller(draw_controller, screen):
    if draw_controller.start:
        print_center("UNBEATABLE TIC TAC TOE", screen, 25, 75)
        print_center("Choose Option <enter>", screen, 27, 75)
        if draw_controller.selector == curses.KEY_RIGHT:
            draw_controller.start_selector_num += 1
            if draw_controller.start_selector_num == 3:
                draw_controller.start_selector_num = 0
        elif draw_controller.selector == curses.KEY_LEFT:
            draw_controller.start_selector_num -= 1
            if draw_controller.start_selector_num == -1:
                draw_controller.start_selector_num = 2


    elif draw_controller.one_player:
        draw_controller.start_selector_num = 3
        draw_board(screen, draw_controller.p1_game.puzzle, 10, 32)
        screen.addstr(22, 0, "CONTROLS: ARROW KEYS MOVE CURSOR")       
        screen.addstr(23, 0, "PRESS <enter> TO PLACE CHARACTER")
        screen.addstr(24, 0, "PRESS \"o\" FOR OPTIONS")
        board_cursor_controller(draw_controller, screen)

def environment_switch(draw_controller):
    if (draw_controller.selector == 10 or draw_controller.selector == 13) and draw_controller.start_selector_num == 0:
        draw_controller.draw = False
    elif (draw_controller.selector == 10 or draw_controller.selector == 13) and draw_controller.start_selector_num == 1:
        draw_controller.start = False
        draw_controller.one_player = True
    elif draw_controller.one_player and draw_controller.selector == ord('o'):
        draw_controller.start = True
        draw_controller.one_player = False
        draw_controller.start_selector_num = 1

def option_switch(draw_controller, screen):
    if draw_controller.start_selector_num == 0:
        screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
        screen.addstr(0,57,"PLAYER VS PLAYER")
        screen.addstr(0,0,"QUIT", curses.A_UNDERLINE)
        screen.addstr(0,5,"*")
        
    elif draw_controller.start_selector_num == 1:
        screen.addstr(0,25,"PLAYER VS UNBEATABLE AI", curses.A_UNDERLINE)
        screen.addstr(0,49,"*")
        screen.addstr(0,57,"PLAYER VS PLAYER")
        screen.addstr(0,0,"QUIT")

    elif draw_controller.start_selector_num == 2:
        screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
        screen.addstr(0,57,"PLAYER VS PLAYER", curses.A_UNDERLINE)
        screen.addstr(0,74,"*")
        screen.addstr(0,0,"QUIT")

    elif draw_controller.start_selector_num == 3:
        if draw_controller.one_player:
            screen.addstr(0,25,"PLAYER VS UNBEATABLE AI", curses.A_UNDERLINE)
            screen.addstr(0,57,"PLAYER VS PLAYER")
            screen.addstr(0,0,"QUIT")

def print_center(message, screen, height, width):
    # Calculate center row
    middle_row = int(height / 2)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(width / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    screen.addstr(middle_row, x_position, message)
    screen.refresh()

def update_ball(screen, ball):
    dy = 1
    dx = 1
    bally = ball[0]
    ballx = ball[1]

    if bally == 24:
        dy = -1
    if ballx == 74:
        dx = -1

    newball = [bally+dy, ballx+dx]

    screen.addstr(bally+dy, ballx+dx, "#")

    return newball
    