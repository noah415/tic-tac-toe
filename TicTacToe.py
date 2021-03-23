import minimax
import time
import sys

class TicTacToe():
    ''' This is a tic tac toe game class. It holds most of the methods 
    that will manipulate the game board such as: player_turn and computer_turn '''

    def __init__(self):
        self.puzzle =  [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]

    
    def print_game(self):
        ''' prints the game board in a pleasing way '''
        print("\t   [col]")
        print("           0 1 2")
        for i in range(3):
            if i == 1:
                print("   [row]" + str(i) + "[", end = " ")
            else:
                print("\t" + str(i) + "[", end = " ")

            for j in range(3):
                print(self.puzzle[i][j] + " ", end="")

            print("]")

    def player_turn(self, player_char = None):
        ''' Will prompt the player for a row and column to assign the 
        player's character '''
        enter_prompt_string = "Enter your choice\nRow (space) Column : "
        invalid_prompt_string = "\nInvalid selection, try again\n"


        invalid = True
        if player_char == None:
            player_char = "X"
        
        while invalid:
            for char in enter_prompt_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.029)

            choice = input()

            if len(choice) != 3:
                for char in invalid_prompt_string:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.029)
                continue

            choice_list = choice.split()
            row = int(choice_list[0])
            col = int(choice_list[1])

            if row > 2 or row < 0 or col > 2 or col < 0 or self.puzzle[row][col] != " ":
                for char in invalid_prompt_string:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.029)
            else:
                self.puzzle[row][col] = player_char
                invalid = False

    def check_status(self):
        ''' calls on its helper function to return True or False. 
        Determining whether the game board has a winner '''
        return self.check_row() or self.check_col() or self.check_diag()

    def check_row(self):
        ''' helper function to check status that returns a bool 
        if any rows have a winner '''

        for i in range(3):

            if self.puzzle[i][0] == self.puzzle[i][1] == self.puzzle[i][2] and self.puzzle[i][0] != " ":
                return True
            
        return False

    def check_col(self):
        ''' helper function to check_status that returns a bool 
        determing whether there is a winner in any of the cols '''
        for i in range(3):

            if self.puzzle[0][i] == self.puzzle[1][i] == self.puzzle[2][i] and self.puzzle[0][i] != " ":
                return True
            
        return False

    def check_diag(self):
        ''' helper function to check_status, which returns a bool 
        determining whether there is a winner in any of the rows '''
        if self.puzzle[0][0] == self.puzzle[1][1] == self.puzzle[2][2] and self.puzzle[0][0] != " ":
            return True

        elif self.puzzle[0][2] == self.puzzle[1][1] == self.puzzle[2][0] and self.puzzle[0][2] != " ":
            return True

        else:
            return False

    def computer_turn(self, computer_char, player_char):
        ''' This method is used when it is currently the computers turn.
        This method calls a function that uses the minimax algorithm, and 
        returns the best move determined by it. '''

        choice_tup = minimax.best_move(self.puzzle, computer_char, player_char)

        self.puzzle[choice_tup[0]][choice_tup[1]] = computer_char


def scheck_status(puzzle):
    ''' Statically checks a puzzle array '''
    return scheck_row(puzzle) or scheck_col(puzzle) or scheck_diag(puzzle)


def scheck_row(puzzle):
    ''' helper to scheck_status '''

    for i in range(3):

        if puzzle[i][0] == puzzle[i][1] == puzzle[i][2] and puzzle[i][0] != " ":
            return True
            
    return False


def scheck_col(puzzle):
    ''' helper to scheck_status '''

    for i in range(3):

        if puzzle[0][i] == puzzle[1][i] == puzzle[2][i] and puzzle[0][i] != " ":
            return True
            
    return False


def scheck_diag(puzzle):
    ''' helper to scheck_status '''
    if puzzle[0][0] == puzzle[1][1] == puzzle[2][2] and puzzle[0][0] != " ":
        return True

    elif puzzle[0][2] == puzzle[1][1] == puzzle[2][0] and puzzle[0][2] != " ":
        return True

    else:
        return False
        
        
            


