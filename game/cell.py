from game.tile import Tile
class Cell:
    def __init__(self, multiplayer, multiplayer_type):
        self.multiplayer = multiplayer
        self.multiplayer_type = multiplayer_type
        self.letter = None
    def add_letter(self,letter:Tile):
        self.letter = letter
    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplayer_type == 'letter':
            return self.letter.value * self.multiplayer
        if self.multiplayer_type == 'word':
            return self.letter.value
        
        