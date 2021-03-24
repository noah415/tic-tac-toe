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
        ''' if (draw_controller.selector == 10 or draw_controller.selector == 13) and draw_controller.start_selector_num == 0:
            draw_controller.draw = False
        elif (draw_controller.selector == 10 or draw_controller.selector == 13) and draw_controller.start_selector_num == 1:
            draw_controller.start = False
            draw_controller.one_player = True
        elif draw_controller.one_player and draw_controller.selector == ord('o'):
            draw_controller.start = True
            draw_controller.one_player = False
            draw_controller.start_selector_num = 1 '''

#this is for the different environment controls
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

#this controls the cursor on the board
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


#this is the options control printer
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
        
#this is the board selection control
        elif draw_controller.board_selector_num == 0:
            y = 1

        screen.refresh()

        #selector = -1



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