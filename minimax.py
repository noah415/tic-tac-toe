import TicTacToe

def best_move(puzzle, computer_char, player_char):
    ''' Returns a tuple of (row, col) that is the best choice 
    in the given circumstances (minimax AI) '''

    best = -1500
    best_choice = ()
    possibilities = get_pos(puzzle)
    
    for choice in possibilities:
        puzzle[choice[0]][choice[1]] = computer_char
        result = minimax(puzzle, 0, False, computer_char, player_char)
        puzzle[choice[0]][choice[1]] = " "

        best = max(result, best)
        if best == result:
            best_choice = choice

        
    return best_choice

def get_pos(puzzle):
    pos_list = []
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == " ":
                pos_list.append((i,j))

    return pos_list

def minimax(puzzle, depth, isMax, computer_char, player_char):

    if TicTacToe.scheck_status(puzzle):
        if isMax:
            return -1
        else:
            return 1
    if is_full(puzzle):
        return 0


    if isMax:
        best = -1500
        possibilities = get_pos(puzzle)
    
        for choice in possibilities:
           puzzle[choice[0]][choice[1]] = computer_char
           result = minimax(puzzle, 0, False, computer_char, player_char)
           puzzle[choice[0]][choice[1]] = " "

           best = max(result, best)
        
        return best

    elif not isMax:
        best = 1500
        possibilities = get_pos(puzzle)
    
        for choice in possibilities:
           puzzle[choice[0]][choice[1]] = player_char
           result = minimax(puzzle, 0, True, computer_char, player_char)
           puzzle[choice[0]][choice[1]] = " "
           result = result

           best = min(result, best)

        return best


def is_full(puzzle):
    list_pos = get_pos(puzzle)
    if len(list_pos) == 0:
        return True

    return False

