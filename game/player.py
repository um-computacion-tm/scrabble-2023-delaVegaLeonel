import unittest
import random
from game.bagtiles import BagTiles

class Player:
    def __init__(self):
        self.rack = []

    def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))

    def exchange_tiles(self,index,bag=BagTiles):
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.append(new_tile)
        

import unittest
from game.player import Player
from game.models import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

    def test_validate_user_has_letters(self):

        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]

        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.has_letters(tiles)

        self.assertEqual(is_valid, True)
        
        def test_validate_fail_when_user_has_not_letters(self):
            bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
        ]
        player = Player(bag_tile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]

        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, False)

if __name__ == '__main__':
    unittest.main()
