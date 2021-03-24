import curses
from curses import wrapper
import os
from screen_funcs import *

def setup(screen):
    print_center("Welcome to Tic Tac Toe", screen)
    screen.addstr(0,0,"Player vs AI")
    screen.addstr(2,0,"Player vs Player")
    screen.addstr(4,0,"Quit", curses.A_BLINK)
    screen.addstr(4,5,"*")
    screen.refresh()


def draw(screen):
    draw = True
    start = True
    one_player = False
    two_player = False
    start_selector_num = 0

    while draw:
        selector = screen.getkey()
        if (start):
            start_selector_num = draw_start(screen, start_selector_num, selector)

        selector = ''



def main(screen):
    os.system("printf '\e[8;25;75t'")
    curses.curs_set(0)
    curses.cbreak()

    
    setup(screen)

    draw(screen)
        

    
    curses.napms(3000)
    curses.curs_set(1)
    curses.echo()
    curses.nocbreak()
if __name__ == "__main__":
    wrapper(main)