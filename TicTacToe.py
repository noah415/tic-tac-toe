import minimax
import time
import sys

class TicTacToe():

    def __init__(self):
        self.puzzle =  [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]

    
    def print_game(self):
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
        enter_prompt_string = "Enter your choice\nRow (space) Column : "
        invalid_prompt_string = "\nInvalid selection, try again\n"


        invalid = True
        if player_char == None:
            player_char = "X"
        
        while invalid:
            for char in enter_prompt_string:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.05)

            choice = input()
            choice_list = choice.split()
            row = int(choice_list[0])
            col = int(choice_list[1])

            if self.puzzle[row][col] != " ":
                for char in invalid_prompt_string:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.05)
            else:
                self.puzzle[row][col] = player_char
                invalid = False

    def check_status(self):
        return self.check_row() or self.check_col() or self.check_diag()

    def check_row(self):

        for i in range(3):

            if self.puzzle[i][0] == self.puzzle[i][1] == self.puzzle[i][2] and self.puzzle[i][0] != " ":
                return True
            
        return False

    def check_col(self):

        for i in range(3):

            if self.puzzle[0][i] == self.puzzle[1][i] == self.puzzle[2][i] and self.puzzle[0][i] != " ":
                return True
            
        return False

    def check_diag(self):
        if self.puzzle[0][0] == self.puzzle[1][1] == self.puzzle[2][2] and self.puzzle[0][0] != " ":
            return True

        elif self.puzzle[0][2] == self.puzzle[1][1] == self.puzzle[2][0] and self.puzzle[0][2] != " ":
            return True

        else:
            return False

    def computer_turn(self, computer_char, player_char):

        choice_tup = minimax.best_move(self.puzzle, computer_char, player_char)

        self.puzzle[choice_tup[0]][choice_tup[1]] = computer_char


def scheck_status(puzzle):
    return scheck_row(puzzle) or scheck_col(puzzle) or scheck_diag(puzzle)


def scheck_row(puzzle):

    for i in range(3):

        if puzzle[i][0] == puzzle[i][1] == puzzle[i][2] and puzzle[i][0] != " ":
            return True
            
    return False


def scheck_col(puzzle):

    for i in range(3):

        if puzzle[0][i] == puzzle[1][i] == puzzle[2][i] and puzzle[0][i] != " ":
            return True
            
    return False


def scheck_diag(puzzle):
    if puzzle[0][0] == puzzle[1][1] == puzzle[2][2] and puzzle[0][0] != " ":
        return True

    elif puzzle[0][2] == puzzle[1][1] == puzzle[2][0] and puzzle[0][2] != " ":
        return True

    else:
        return False
        
        
            


