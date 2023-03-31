import numpy as np
from game import piece


class Board:
    spaces: np.array

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
    

    def play_piece(self, piece: piece.Piece, x, y):
        self.spaces[x:x+5, y:y+5] = piece.spaces
    

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