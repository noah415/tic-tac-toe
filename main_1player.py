from TicTacToe import *
import minimax
import time
import sys

def main():
    output_string = "\nHello!\nThis is a game of Tic Tac Toe\nPlayer uses \"O\" and Computer uses \"X\"\nEnjoy the game!\n\n"

    for char in output_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    game = TicTacToe()
    player_turn = False
    tie = False
    player_char = "O"
    computer_char = "X"
    
    while not game.check_status():
        if player_turn:
            print("Player Move")
            game.player_turn(player_char)
        else:
            print("Computer Move")
            game.computer_turn(computer_char, player_char)
            
        player_turn = not player_turn

        
        print("\n")
        game.print_game()
        print("\n\n")

        if minimax.is_full(game.puzzle):
            tie = True
            break


    if tie:
        print("There was a tie")
    elif (player_turn):
        print("Computer win!!")
    else:
        print("Player win!!")
        

        




    


if __name__ == "__main__":
    main()