from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles
import uuid

class Scrabble:
    def __init__(self,player_count):
        self.board = Board()
        self.bagtiles = BagTiles()
        self.gameid = str(uuid.uuid4())
        self.players = []
        for _ in range(player_count):
            self.players.append(Player())