from TicTacToe import *
import minimax
import time
import sys

def main():
    output_string = "\nHello!\nThis is a game of Tic Tac Toe\nPlayer 1 uses \"X\" and Player 2 uses \"O\"\nEnjoy the game!\n\n"

    for char in output_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    game = TicTacToe()
    player1_turn = True
    player_char = ""
    
    while not game.check_status():
        if player1_turn:
            print("Player 1")
            player_char = "X"
        else:
            print("Player 2")
            player_char = "O"
            
        player1_turn = not player1_turn

        game.player_turn(player_char)
        print("\n\n")
        game.print_game()
        print("\n\n")

    if (player1_turn):
        print("Player 2 win!!")
    else:
        print("Player 1 win!!")

        




    


if __name__ == "__main__":
    main()

