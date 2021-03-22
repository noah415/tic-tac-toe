from TicTacToe import *
import minimax
import time
import sys

def main():
    output_string = "\nHello!\nThis is a game of Tic Tac Toe\nPlayer competes against Computer AI\nEnjoy the game!\n\n"
    player_choice_string = "press \"x\" for player \"X\" or \"o\" for player \"O\" then <enter>: "
    invalid_output_string = "Invalid input, try again\n"
    player_move_string = "Player Move: "
    computer_move_string = "Computer Move: "
    tie_string = "There was a tie"
    player_win_string = "Player win!!"
    player_lose_string = "Player lost :("


    game = TicTacToe()
    tie = False
    chosen = False

    for char in output_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    while not chosen:
        for char in player_choice_string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.05)


        player_choice = input()
        if player_choice == "x":
            player_char = "X"
            computer_char = "O"
            player_turn = True
            chosen = True
        elif player_choice == "o":
            player_char = "O"
            computer_char = "X"
            player_turn = False
            chosen = True
        else:
            for char in invalid_output_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.05)

    print("\n")
    game.print_game()
    print("\n\n")
    
    while not game.check_status():
        if player_turn:
            for char in player_move_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.05)

            game.player_turn(player_char)
        else:
            for char in computer_move_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.05)

            time.sleep(2)

            game.computer_turn(computer_char, player_char)
            
        player_turn = not player_turn

        
        print("\n")
        game.print_game()
        print("\n\n")

        if minimax.is_full(game.puzzle):
            tie = True
            break


    if tie:
        for char in tie_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.05)
    elif (player_turn):
        for char in player_lose_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.05)
    else:
        for char in player_win_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.05)
        


if __name__ == "__main__":
    main()