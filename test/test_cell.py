import unittest
from game.cell import Cell
from game.tile import Tile

class TestCell(unittest.TestCase):
    def test_cell(self):
        cell = Cell(multiplayer=2, multiplayer_type='letter')
        self.assertEqual(cell.multiplayer,2)
        self.assertEqual(cell.multiplayer_type,'letter')
        self.assertEqual(cell.letter, None)
    
    def test_add_letter(self):
        cell = Cell(multiplayer=1, multiplayer_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)
    
    def test_cell_value(self):
        cell = Cell(multiplayer=1, multiplayer_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(), 3)
    
    def test_cell_multiplayer_letter(self):
        cell = Cell(multiplayer=2, multiplayer_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

    def test_cell_multiplayer_word(self):
        cell = Cell(multiplayer=2, multiplayer_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),3,)

    def test_cell_letter(self):
        cell = Cell(1, None)
        self.assertEqual(cell.calculate_value(),0)
if __name__ == '__main__':
    unittest.main()

    
    