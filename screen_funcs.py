import curses
import os
import TicTacToe

def board_cursor_controller(draw_controller, screen):
    if draw_controller.selector == curses.KEY_RIGHT:
        draw_controller.cursor[1] += 4
        draw_controller.board_selector[1] += 1
        if draw_controller.cursor[1] > 40:
            draw_controller.cursor[1] = 32
            draw_controller.board_selector[1] = 0

    elif draw_controller.selector == curses.KEY_LEFT:
        draw_controller.cursor[1] -= 4
        draw_controller.board_selector[1] -= 1
        if draw_controller.cursor[1] < 32:
            draw_controller.cursor[1] = 40
            draw_controller.board_selector[1] = 2

    elif draw_controller.selector == curses.KEY_UP:
        draw_controller.cursor[0] -= 2
        draw_controller.board_selector[0] -= 1
        if draw_controller.cursor[0] < 10:
            draw_controller.cursor[0] = 14
            draw_controller.board_selector[0] = 2

    elif draw_controller.selector == curses.KEY_DOWN:
        draw_controller.cursor[0] += 2
        draw_controller.board_selector[0] += 1
        if draw_controller.cursor[0] > 14:
            draw_controller.cursor[0] = 10
            draw_controller.board_selector[0] = 0
    character = draw_controller.p1_game.puzzle[draw_controller.board_selector[0]][draw_controller.board_selector[1]]
    screen.addstr(draw_controller.cursor[0], draw_controller.cursor[1], character, curses.A_UNDERLINE)
    screen.addstr(24,53, "PLAYER @: "+ "row "+
        str(draw_controller.board_selector[0]) + " col " + str(draw_controller.board_selector[1]))

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
        screen.addstr(23, 0, "CONTROLS: ARROW KEYS MOVE CURSOR")       
        screen.addstr(24, 0, "PRESS <enter> TO SELECT")
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
        screen.addstr(8,0,"PLAYER PLAYING AS: "+ draw_controller.p1_game.player_char)
        screen.addstr(8,59,"AI PLAYING AS: "+ draw_controller.p1_game.computer_char)

        if draw_controller.p1_game.game_end() and not draw_controller.p1_game.is_full():
            draw_controller.start = False
            draw_controller.one_player = False
            draw_controller.player_won = True
            draw_controller.tie = False
            draw_controller.computer_won = False

        if not draw_controller.p1_game.game_end() and draw_controller.computer_turn:
            draw_controller.p1_game.computer_turn(draw_controller.p1_game.computer_char,draw_controller.p1_game.player_char)

            

            draw_controller.computer_turn = False
            draw_controller.player_turn = True

        draw_board(screen, draw_controller.p1_game.puzzle, 10, 32)
        screen.addstr(22, 0, "CONTROLS: ARROW KEYS MOVE CURSOR")       
        screen.addstr(23, 0, "PRESS <enter> TO PLACE CHARACTER")
        screen.addstr(24, 0, "PRESS \"o\" FOR OPTIONS")
        
        board_cursor_controller(draw_controller, screen)

        if draw_controller.p1_game.game_end():
            draw_controller.player_turn = False
            draw_controller.computer_turn = False
            draw_controller.start = False
            draw_controller.one_player = False
            #draw_controller.start_selector_num = 1

            old_puzzle = draw_controller.p1_game.puzzle

            if not draw_controller.player_won:
                screen.clear()
                if draw_controller.p1_game.is_full():
                    draw_controller.computer_won = False
                    draw_controller.player_won = False
                    draw_controller.tie = True
                    print_center("THERE WAS A TIE", screen, 25, 75)
                    screen.addstr(22, 0, "CONTROLS: ARROW KEYS MOVE CURSOR")       
                    screen.addstr(23, 0, "PRESS <enter> TO PLACE CHARACTER")
                    print_center("PRESS \"o\" FOR OPTIONS TO RESTART OR QUIT", screen, 27, 75)

                else:
                    draw_controller.tie = False
                    draw_controller.player_won = False
                    draw_controller.computer_won = True
                    print_center("THE COMPUTER BEAT YOU. IS THAT ALL YOU GOT?", screen, 25, 75)
                    screen.addstr(22, 0, "CONTROLS: ARROW KEYS MOVE CURSOR")       
                    screen.addstr(23, 0, "PRESS <enter> TO PLACE CHARACTER")
                    print_center("PRESS \"o\" FOR OPTIONS TO RESTART OR QUIT", screen, 27, 75)
            draw_board(screen, old_puzzle, 5, 32)
            draw_controller.p1_game = TicTacToe.TicTacToe()

    #this is where they were

        

def environment_switch(draw_controller, screen):
    if (draw_controller.selector == 10 or draw_controller.selector == 13) and draw_controller.start_selector_num == 0:
        draw_controller.draw = False

    elif (draw_controller.selector == 10 or draw_controller.selector == 13) and draw_controller.start_selector_num == 1:
        draw_controller.start = False
        draw_controller.one_player = True
        print_center("PRESS X TO PLAY X", screen, 25, 75)
        print_center("OR", screen, 27, 75)
        print_center("PRESS O TO PLAY O", screen, 29, 75)
        lilChar = screen.getch()
        if lilChar == ord('x'):
            draw_controller.p1_game.player_char = 'X'
            draw_controller.p1_game.computer_char = 'O'
            draw_controller.player_turn = True
            draw_controller.computer_turn = False
        else:
            draw_controller.p1_game.player_char = 'O'
            draw_controller.p1_game.computer_char = 'X'
            draw_controller.player_turn = False
            draw_controller.computer_turn = True
        screen.clear()

    elif draw_controller.one_player and draw_controller.selector == ord('o'):
        draw_controller.start = True
        draw_controller.one_player = False
        draw_controller.start_selector_num = 1

    elif (draw_controller.selector == 10 or draw_controller.selector == 13) and draw_controller.one_player:
        if draw_controller.player_turn:
            draw_controller.p1_game.player_turn_UI(draw_controller.board_selector,draw_controller.p1_game.player_char)
            draw_controller.player_turn = False
            draw_controller.computer_turn = True

    elif (draw_controller.computer_won or draw_controller.tie) and draw_controller.selector == ord('o'):
        draw_controller.tie = False
        draw_controller.computer_won = False
        draw_controller.start = True
        draw_controller.start_selector_num = 0

    elif (draw_controller.computer_won or draw_controller.tie) and draw_controller.selector != ord('o'):
        draw_controller.draw = False
        #screen.addstr()

def option_switch(draw_controller, screen):
    if draw_controller.start_selector_num == 0:
        screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
        screen.addstr(0,57,"PLAYER VS PLAYER")
        screen.addstr(1,57,"(COMING SOON)")
        screen.addstr(0,0,"QUIT", curses.A_UNDERLINE)
        screen.addstr(0,5,"*")
        
    elif draw_controller.start_selector_num == 1:
        screen.addstr(0,25,"PLAYER VS UNBEATABLE AI", curses.A_UNDERLINE)
        screen.addstr(0,49,"*")
        screen.addstr(0,57,"PLAYER VS PLAYER")
        screen.addstr(1,57,"(COMING SOON)")
        screen.addstr(0,0,"QUIT")

    elif draw_controller.start_selector_num == 2:
        screen.addstr(0,25,"PLAYER VS UNBEATABLE AI")
        screen.addstr(0,57,"PLAYER VS PLAYER", curses.A_UNDERLINE)
        screen.addstr(1,57,"(COMING SOON)")
        screen.addstr(0,74,"*")
        screen.addstr(0,0,"QUIT")

    elif draw_controller.start_selector_num == 3:
        if draw_controller.one_player:
            screen.addstr(0,25,"PLAYER VS UNBEATABLE AI", curses.A_UNDERLINE)
            screen.addstr(0,57,"PLAYER VS PLAYER")
            screen.addstr(1,57,"(COMING SOON)")
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
    