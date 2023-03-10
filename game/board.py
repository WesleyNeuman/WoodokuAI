import numpy as np
from pieces import *


class Board:
    spaces: np.array

    def __init__(self):
        self.spaces = self.initialize_board()
        

    def initialize_board(self):
        return np.array(
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
    

    def play_piece(self, piece: Piece, x, y):
        # This is a highly inefficient implementation due to using a loop, will swap later
        for space in piece.spaces:
            self.spaces[space.x + x][space.y + y] = 1

    
    def check_for_complete_regions(self):
        regions = []

        # Check columns and rows
        for i in range(0, 9):
            col = self.spaces[i, :]
            row = self.spaces[:, i]

            # column
            if col.sum() == 9:
                regions.append([i, ])
            
        pass