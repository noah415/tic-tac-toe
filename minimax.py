import TicTacToe
import time

def best_move(puzzle, computer_char, player_char):
    ''' Returns a tuple of (row, col) that is the best choice 
    in the given circumstances (minimax AI) '''

    best = -1500
    best_choice = ()
    possibilities = get_pos(puzzle)
    if len(possibilities) == 0:
        raise IndexError
    
    ''' for all possible choices:
            - call minimax on all possible choices
            - if one choice is ranked better choose it
            - after all possible choices return the best choice <tuple> (row, col) '''

    for choice in possibilities:
        puzzle[choice[0]][choice[1]] = computer_char
        result = minimax(puzzle, 0, False, computer_char, player_char, -1500, 1500)
        puzzle[choice[0]][choice[1]] = " "

        best = max(result, best)
        if best == result:
            best_choice = choice

        
    return best_choice



def get_pos(puzzle):
    ''' retrieves all possible choices the computer can make 
    and returns a list of them '''
    pos_list = []
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == " ":
                pos_list.append((i,j))

    return pos_list

def minimax(puzzle, depth, isMax, computer_char, player_char, alpha, beta):
    ''' this is a recursive function that returns 1, -1, or 0
        1: this move will most likely end in a win
       -1: this move will most likely end in a loss
        0: this move will most likely end in a tie '''
    if TicTacToe.scheck_status(puzzle): #if there is a win
        if isMax:
            return -10 + depth
        else:
            return 10 - depth
    if is_full(puzzle): #if there is a tie
        return 0


    if isMax: #if recursion is favoring the computer (MAX)
        best = -1500
        possibilities = get_pos(puzzle)
    
        ''' for all possibilities, recursively call the minimax function on each
        and choose the best fit option '''
        for choice in possibilities:
           puzzle[choice[0]][choice[1]] = computer_char
           result = minimax(puzzle, depth+1, False, computer_char, player_char, alpha, beta)
           puzzle[choice[0]][choice[1]] = " "

           best = max(result, best)

           alpha = max(alpha, result)
           if alpha >= beta:
               break
        
        return best

    elif not isMax: #if recursion is favoring the player (MIN)
        best = 1500
        possibilities = get_pos(puzzle)
    

        ''' for all possibilities, recursively call the minimax function on each
        and choose the best fit option '''
        for choice in possibilities:
           puzzle[choice[0]][choice[1]] = player_char
           result = minimax(puzzle, depth+1, True, computer_char, player_char, alpha, beta)
           puzzle[choice[0]][choice[1]] = " "
           result = result

           best = min(result, best)

           beta = min(beta, result)
           if alpha >= beta:
               break

        return best


def is_full(puzzle):
    ''' Returns True if the puzzle is full, False if not '''
    list_pos = get_pos(puzzle)
    if len(list_pos) == 0:
        return True

    return False

