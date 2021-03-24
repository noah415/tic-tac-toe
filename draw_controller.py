

class Draw_Controller:
    def __init__(self, draw, start, one_player, 
                two_player, start_selector_num, 
                board_selector_num, cursor, p1_game,
                p2_game, selector = None):

        self.draw = draw
        self.start = start
        self.one_player = one_player
        self.two_player = two_player
        self.start_selector_num = start_selector_num
        self.board_selector_num = board_selector_num
        self.cursor = cursor
        self.p1_game = p1_game
        self.p2_game = p2_game
        self.selector = selector