import TicTacToe
import minimax
import curses
import os
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
    draw = True#0
    start = True#1
    one_player = False#2
    two_player = False#3

    start_selector_num = 0#4
    board_selector_num = 0#5
    cursor = [10,32]#6
    p1_game = TicTacToe.TicTacToe()#7
    p2_game = TicTacToe.TicTacToe()#8

    draw_controller = [draw, start, one_player, two_player, start_selector_num, board_selector_num,
                        cursor, p1_game, p2_game]

    while draw_controller[0]:
        selector = screen.getch()#9
        draw_controller = [draw, start, one_player, two_player, start_selector_num, board_selector_num,
                        cursor, p1_game, p2_game, selector]
        screen.clear()

#environment switcher
        draw_controller = environment_switcher(draw_controller)
        ''' if (selector == 10 or selector == 13) and start_selector_num == 0:
            draw = False
        elif (selector == 10 or selector == 13) and start_selector_num == 1:
            start = False
            one_player = True
        elif one_player and selector == ord('o'):
            start = True
            one_player = False
            start_selector_num = 1 '''

#this is for the different environment controls
        if draw_controller[1]:
            print_center("UNBEATABLE TIC TAC TOE", screen, 25, 75)
            print_center("Choose Option <enter>", screen, 27, 75)
            if selector == curses.KEY_RIGHT:
                draw_controller[4] += 1
                if draw_controller[4] == 3:
                    draw_controller[4] = 0
            elif selector == curses.KEY_LEFT:
                draw_controller[4] -= 1
                if draw_controller[4] == -1:
                    draw_controller[4] = 2


        elif draw_controller[2]:
            draw_controller[4] = 3
            draw_board(screen, draw_controller[7].puzzle, 10, 32)
            screen.addstr(22, 0, "CONTROLS: ARROW KEYS MOVE CURSOR")       
            screen.addstr(23, 0, "PRESS <enter> TO PLACE CHARACTER")
            screen.addstr(24, 0, "PRESS \"o\" FOR OPTIONS")

#this controls the cursor on the board
            if selector == curses.KEY_RIGHT:
                draw_controller[6][1] += 4
                if draw_controller[6][1] > 40:
                    draw_controller[6][1] = 32
            elif selector == curses.KEY_LEFT:
                draw_controller[6][1] -= 4
                if draw_controller[6][1] < 32:
                    draw_controller[6][1] = 40
            elif selector == curses.KEY_UP:
                draw_controller[6][0] -= 2
                if draw_controller[6][0] < 10:
                    draw_controller[6][0] = 14
            elif selector == curses.KEY_DOWN:
                draw_controller[6][0] += 2
                if draw_controller[6][0] > 14:
                    draw_controller[6][0] = 10
            screen.addstr(draw_controller[6][0], draw_controller[6][1], "*", curses.A_BLINK)


#this is the options control printer
        if draw_controller[4] == 0:
            screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
            screen.addstr(0,57,"PLAYER VS PLAYER")
            screen.addstr(0,0,"QUIT", curses.A_UNDERLINE)
            screen.addstr(0,5,"*")
            
        elif draw_controller[4] == 1:
            screen.addstr(0,25,"PLAYER VS UNBEATABLE AI", curses.A_UNDERLINE)
            screen.addstr(0,49,"*")
            screen.addstr(0,57,"PLAYER VS PLAYER")
            screen.addstr(0,0,"QUIT")

        elif draw_controller[4] == 2:
            screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
            screen.addstr(0,57,"PLAYER VS PLAYER", curses.A_UNDERLINE)
            screen.addstr(0,74,"*")
            screen.addstr(0,0,"QUIT")

        elif draw_controller[4] == 3:
            if draw_controller[2]:
                screen.addstr(0,25,"PLAYER VS UNBEATABLE AI", curses.A_UNDERLINE)
                screen.addstr(0,57,"PLAYER VS PLAYER")
                screen.addstr(0,0,"QUIT")
        
#this is the board selection control
        elif draw_controller[5] == 0:
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