import curses
from curses import wrapper
import os

def setup(screen):
    print_center("welcome to tic tac toe", screen)
    screen.addstr(0,0,"Player vs AI")
    screen.addstr(0,0,"Player vs Player")
    screen.addstr(0,0,"Quit")


def print_center(message, screen):
    # Calculate center row
    middle_row = int(25 / 2)

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(75 / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text
    screen.addstr(middle_row, x_position, message)
    screen.refresh()

def draw_board(screen):
    pass


def draw(screen):
    draw = True
    start = True
    one_player = False
    two_player = False

    while draw:
        if (start):
            print_center("welcome to tic tac toe", screen)

    


def main(screen):
    os.system("printf '\e[8;25;75t'")
    curses.curs_set(0)
    curses.echo()

    
    setup(screen)

    draw(screen)
        

    
    curses.napms(3000)
    curses.curs_set(1)
    curses.endwin()



if __name__ == "__main__":
    wrapper(main)