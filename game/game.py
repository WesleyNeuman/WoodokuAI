import numpy as np
from pieces import Piece
from board import *

class Game:
    score: int
    board: np.array
    streak: int
    turn_count: int
    pieces = [] # the pieces in the current round

    def __init__(self):
        self.score = 0
        self.streak = 0
        self.turn_count = 0
        self.board = Board()
    

game = Game()
print(game.board)