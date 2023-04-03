from game.piece import Piece

import numpy as np
import logging

class Board:
    spaces: np.array
    height = 9
    length = 9

    def __init__(self):
        self.spaces = self.generate_empty_board()
        

    def generate_empty_board(self):
        return np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
    

    def play_piece(self, piece: Piece, x, y):
        height = x+piece.height()
        length = y+piece.length()

        if height > self.height:
            logging.warning("Cannot play piece - X coord of {0} is larger than the limit of {1}".format(height, self.height))
            return False
        elif x < 0:
            logging.warning("Cannot play piece - X coord of {0} is less than 0".format(x, 0))
            return False
        elif length > self.length:
            logging.warning("Cannot play piece - Y coord of {0} is larger than the limit of {1}".format(length, self.length))
            return False
        elif y < 0:
            logging.warning("Cannot play piece - Y coord of {0} is less than 0".format(y, 0))
            return False
        
        candidate = np.add(self.spaces[x:height, y:length], piece.spaces)

        if candidate.max() > 1:
            logging.warning("Cannot play piece - Other pieces obstruct placement")
            return False
        else:
            logging.info("Piece played successfully")
            self.spaces[x:height, y:length] = candidate
            return True
    

    def get_region_sum(self, slicer):
        return np.sum(self.spaces[slicer])

    
    def check_for_complete_regions(self):
        elim_regions = self.generate_empty_board()
        total_regions = 0

        # Check columns and rows
        for i in range(0, 9):
            col = self.spaces[i, :]
            row = self.spaces[:, i]

            # column
            if np.sum(col) == 9:
                elim_regions[i, :] = np.ones(9)
                total_regions += 1

            # row
            if np.sum(row) == 9:
                elim_regions[:, i] = np.ones(9)
                total_regions += 1

        # Check sections of 3
        for x in range(1, 7, 3):
            for y in range(1, 7, 3):
                slicer = np.index_exp[x:x+2, y:y+2]
                if self.get_region_sum(slicer) == 9:
                    elim_regions[slicer] = np.ones((3, 3))
                    total_regions += 1

        # Clear scored sections from board
        self.spaces = np.subtract(self.spaces, elim_regions)

        return total_regions