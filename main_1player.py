from TicTacToe import *
import minimax
import time
import sys

def main():
    ''' Calls the mother function (play_tic_tac_toe) and gives the user an 
    option to choose whether to play again or quit '''

    output_string = "\nHello!\nThis is a game of Tic Tac Toe\nPlayer competes against Computer AI\nEnjoy the game!\n\n"
    player_again_string = "If you would like to play again press \"y\" then <enter>\nOtherwise press any other key, then <enter> to exit\n" + \
                            "Your choice <enter>: "
    keep_playing = True

    for char in output_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.029)

    while keep_playing:
        play_tic_tac_toe()

        for char in player_again_string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.029)

        keep_playing_input = input()
        if keep_playing_input != "y":
            break



def play_tic_tac_toe():
    ''' This is the mother function. It holds most of the rules of tic tac toe and 
    implements player's taking turns. '''

    #these are all of the strings printed to the console
    player_choice_string = "press \"x\" for player \"X\" or \"o\" for player \"O\" then <enter>: "
    invalid_output_string = "Invalid input, try again\n"
    player_move_string = "Player Move: "
    computer_move_string = "Computer Move: "
    tie_string = "There was a tie\n\n"
    player_win_string = "Player win!!\n\n"
    player_lose_string = "Player lost :(\n\n"

    #creates a game and initializes a few variables
    game = TicTacToe()
    tie = False
    chosen = False

    #this while loop controls the player's character being used'
    while not chosen:
        for char in player_choice_string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.029)


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
                time.sleep(.029)

    print("\n")
    game.print_game()
    print("\n\n")
    
    #this while loop controls the players' turn and game status
    while not game.check_status():
        if player_turn:
            for char in player_move_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.029)

            game.player_turn(player_char)
        else:
            for char in computer_move_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.029)

        
            game.computer_turn(computer_char, player_char)
            
        player_turn = not player_turn

        
        print("\n")
        game.print_game()
        print("\n\n")

        if minimax.is_full(game.puzzle):
            tie = True
            break

    #this if statements determine the end game status
    if tie:
        for char in tie_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.029)
    elif (player_turn):
        for char in player_lose_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.029)
    else:
        for char in player_win_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.029)


if __name__ == "__main__":
    main()