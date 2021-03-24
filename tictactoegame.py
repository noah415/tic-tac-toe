import TicTacToe
import minimax
import curses
import os
from draw_controller import *
from curses import wrapper
from screen_funcs import *

def setup(screen):
    print_center("UNBEATABLE TIC TAC TOE", screen, 25, 75)
    print_center("Choose Option <enter>", screen, 27, 75)
    screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
    screen.addstr(0,57,"PLAYER VS PLAYER")
    screen.addstr(0,0,"QUIT", curses.A_UNDERLINE)
    screen.addstr(0,5,"*")
    screen.refresh()

def draw(screen):
    draw = True
    start = True
    one_player = False
    two_player = False

    start_selector_num = 0
    board_selector_num = 0
    cursor = [10,32]
    p1_game = TicTacToe.TicTacToe()
    p2_game = TicTacToe.TicTacToe()

    draw_controller = Draw_Controller(draw, start, one_player, two_player, 
                                        start_selector_num, board_selector_num, 
                                        cursor, p1_game, p2_game)

    while draw_controller.draw:
        draw_controller.selector = screen.getch() 
        screen.clear()

        #environment switcher
        environment_switch(draw_controller)

        #this is for the different environment controls
        environment_controller(draw_controller, screen)

        #this is the options control printer
        option_switch(draw_controller, screen)

        #this is the board player turn controller

        screen.refresh()

def main(screen):
    os.system("printf '\e[8;25;75t'")
    curses.curs_set(0)
    curses.cbreak()

    
    setup(screen)

    draw(screen)
        

    screen.clear()
    print_center("GOODBYE :)", screen, 25, 75)
    screen.refresh()
    curses.napms(1500)
    curses.curs_set(1)
    curses.echo()
    curses.nocbreak()
if __name__ == "__main__":
    wrapper(main)