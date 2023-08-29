import unittest
from game.board import Board
from game.cell import Cell

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.grid),15)

    
    