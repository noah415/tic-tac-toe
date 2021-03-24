import curses
import os

def draw_board(screen, board, y, x):
    screen.addstr(y, x,board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    screen.addstr(y+1, x-2,"-------------")
    screen.addstr(y+2, x,board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    screen.addstr(y+3, x-2,"-------------")
    screen.addstr(y+4, x,board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def environment_switch(draw_controller):
    y = 1

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
    