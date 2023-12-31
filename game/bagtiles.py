import unittest
import random
from game.tile import Tile

class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1),
            Tile('B', 3),
            Tile('C', 2),
            Tile('CH', 5),
            Tile('D', 2),
            Tile('E', 1),
            Tile('F', 4),
            Tile('G', 2),
            Tile('H', 4),
            Tile('I', 1),
            Tile('J', 6),
            Tile('L', 1),
            Tile('LL', 8),
            Tile('M', 3),
            Tile('N', 1),
            Tile('Ñ', 8),
            Tile('O', 1),
            Tile('P', 2),
            Tile('Q', 8),
            Tile('R', 1),
            Tile('RR', 8),
            Tile('S', 1),
            Tile('T', 1),
            Tile('U', 1),
            Tile('V', 4),
            Tile('X', 8),
            Tile('Y', 4),
            Tile('Z', 10),
            Tile('?', 0)
        ]
        random.shuffle(self.tiles)
    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles = self.tiles.pop(0)
        return tiles
    def put(self, tiles):
        self.tiles.extend(tiles)
    
    def initial_tiles(self):
        total = []
        bag = BagTiles()
        initial_tiles = {'A':11,'E':11,'O':8,'I':5,'S':5,'N':4,'L':3,'R':4,'U':4,'T':3,'D':4,'G':1,'C':3,'B':1,'M':1,'P':1,'H':1,'?':1}
        for letters, amount in initial_tiles.items():
            for _ in range(amount):
                for x in bag.tiles:
                    if x.letter == letters:
                        total.append(x)
        self.tiles.extend(total)

        