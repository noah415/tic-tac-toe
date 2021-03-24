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
        if (draw_controller.selector == 10 or draw_controller.selector == 13) and start_selector_num == 0:
            draw_controller.draw = False
        elif (draw_controller.selector == 10 or draw_controller.selector == 13) and start_selector_num == 1:
            draw_controller.start = False
            one_player = True
        elif one_player and draw_controller.selector == ord('o'):
            draw_controller.start = True
            one_player = False
            start_selector_num = 1

#this is for the different environment controls
        if draw_controller.start:
            print_center("UNBEATABLE TIC TAC TOE", screen, 25, 75)
            print_center("Choose Option <enter>", screen, 27, 75)
            if draw_controller.selector == curses.KEY_RIGHT:
                start_selector_num += 1
                if start_selector_num == 3:
                    start_selector_num = 0
            elif draw_controller.selector == curses.KEY_LEFT:
                start_selector_num -= 1
                if start_selector_num == -1:
                    start_selector_num = 2


        elif one_player:
            start_selector_num = 3
            draw_board(screen, p1_game.puzzle, 10, 32)
            screen.addstr(22, 0, "CONTROLS: ARROW KEYS MOVE CURSOR")       
            screen.addstr(23, 0, "PRESS <enter> TO PLACE CHARACTER")
            screen.addstr(24, 0, "PRESS \"o\" FOR OPTIONS")

#this controls the cursor on the board
            if draw_controller.selector == curses.KEY_RIGHT:
                cursor[1] += 4
                if cursor[1] > 40:
                    cursor[1] = 32
            elif draw_controller.selector == curses.KEY_LEFT:
                cursor[1] -= 4
                if cursor[1] < 32:
                    cursor[1] = 40
            elif draw_controller.selector == curses.KEY_UP:
                cursor[0] -= 2
                if cursor[0] < 10:
                    cursor[0] = 14
            elif draw_controller.selector == curses.KEY_DOWN:
                cursor[0] += 2
                if cursor[0] > 14:
                    cursor[0] = 10
            screen.addstr(cursor[0], cursor[1], "*", curses.A_BLINK)


#this is the options control printer
        if start_selector_num == 0:
            screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
            screen.addstr(0,57,"PLAYER VS PLAYER")
            screen.addstr(0,0,"QUIT", curses.A_UNDERLINE)
            screen.addstr(0,5,"*")
            
        elif start_selector_num == 1:
            screen.addstr(0,25,"PLAYER VS UNBEATABLE AI", curses.A_UNDERLINE)
            screen.addstr(0,49,"*")
            screen.addstr(0,57,"PLAYER VS PLAYER")
            screen.addstr(0,0,"QUIT")

        elif start_selector_num == 2:
            screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
            screen.addstr(0,57,"PLAYER VS PLAYER", curses.A_UNDERLINE)
            screen.addstr(0,74,"*")
            screen.addstr(0,0,"QUIT")

        elif start_selector_num == 3:
            if one_player:
                screen.addstr(0,25,"PLAYER VS UNBEATABLE AI", curses.A_UNDERLINE)
                screen.addstr(0,57,"PLAYER VS PLAYER")
                screen.addstr(0,0,"QUIT")
        
#this is the board selection control
        elif board_selector_num == 0:
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