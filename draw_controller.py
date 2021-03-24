

class Draw_Controller:
    def __init__(self, draw, start, one_player, 
                two_player, start_selector_num, 
                board_selector, cursor, p1_game,
                p2_game, selector = None, player_turn = False, 
                computer_turn = False, player1_turn = True, 
                player2_turn = False, player_won = False,
                computer_won = False, tie = False):

        self.draw = draw
        self.start = start
        self.one_player = one_player
        self.two_player = two_player
        self.start_selector_num = start_selector_num
        self.board_selector = board_selector
        self.cursor = cursor
        self.p1_game = p1_game
        self.p2_game = p2_game
        self.selector = selector
        self.player_turn = player_turn
        self.computer_turn = computer_turn
        self.player1_turn = player1_turn
        self.player2_turn = player2_turn
        self.player_won = player_won
        self.computer_won = computer_won
        self.tie = tie