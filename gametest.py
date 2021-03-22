import unittest
from TicTacToe import *

class GameTests(unittest.TestCase):

    ''' def test_print(self):
        game = TicTacToe()

        game.print_game() '''

    ''' def test_player_turn2(self):
        game = TicTacToe()

        game.player_turn()
        game.print_game()
        game.player_turn()
        game.print_game() '''

    def test_checkrows1(self):
        game = TicTacToe()
        
        for i in range(3):
            game.puzzle[0][i] = "X"

        self.assertTrue(game.check_row())
        self.assertFalse(game.check_col())
        self.assertFalse(game.check_diag())

    def test_checkrows2(self):
        game = TicTacToe()
        
        game.puzzle = [["O", "X", "O"],
                       [" ", "O", "O"],
                       ["X", "X", "X"]]

        self.assertTrue(game.check_row())
        self.assertFalse(game.check_col())
        self.assertFalse(game.check_diag())

    def test_checkcols1(self):
        game = TicTacToe()
        
        game.puzzle = [["O", "X", "O"],
                       [" ", " ", "O"],
                       [" ", " ", "O"]]

        self.assertFalse(game.check_row())
        self.assertTrue(game.check_col())
        self.assertFalse(game.check_diag())

    def test_checkdiag1(self):
        game = TicTacToe()
        
        game.puzzle = [["O", "X", "O"],
                       [" ", "O", " "],
                       ["O", " ", " "]]

        self.assertFalse(game.check_row())
        self.assertFalse(game.check_col())
        self.assertTrue(game.check_diag())

    def test_check_status1(self):
        game = TicTacToe()
        
        game.puzzle = [["O", "X", "O"],
                       [" ", "X", " "],
                       ["O", " ", " "]]

        self.assertFalse(game.check_status())

    def test_check_status2(self):
        game = TicTacToe()
        
        game.puzzle = [["O", "X", "O"],
                       ["X", "X", "O"],
                       ["O", "O", "X"]]

        self.assertFalse(game.check_status())

    def test_check_status3(self):
        game = TicTacToe()
        
        game.puzzle = [[" ", " ", " "],
                       [" ", " ", " "],
                       [" ", " ", " "]]

        self.assertFalse(game.check_status())

    def test_check_status4(self):
        game = TicTacToe()
        
        game.puzzle = [["O", "O", "O"],
                       [" ", "O", " "],
                       [" ", " ", " "]]

        self.assertTrue(game.check_status())

    def test_check_status5(self):
        game = TicTacToe()
        
        game.puzzle = [["X", "O", "O"],
                       [" ", "O", " "],
                       [" ", "O", " "]]

        self.assertTrue(game.check_status())

    def test_check_status6(self):
        game = TicTacToe()
        
        game.puzzle = [["X", "O", "O"],
                       [" ", "X", " "],
                       [" ", "O", "X"]]

        self.assertTrue(game.check_status())





if __name__ == "__main__":
    unittest.main()