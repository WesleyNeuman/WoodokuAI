from game.piece import *
from game.board import *

import numpy as np
import random
from typing import List
import math

class Game:
    score: int
    board: Board()
    streak: int
    turn_count: int
    pieces: List[Piece]
    round_pieces: List[Piece] # the pieces in the current round

    def __init__(self):
        self.score = 0
        self.streak = 0
        self.turn_count = 0
        self.pieces = define_pieces()
        self.board = Board()
        self.round_pieces = self.get_round_pieces()

        self.display_ui()


    def run_game_loop(self):
        pass


    def display_ui(self):
        print("------- {0} -------".format(self.score))
        print(self.board.spaces)
        print()
        for i in range(0, len(self.round_pieces)):
            print("--- Piece {0} ---".format(i))
            print(self.round_pieces[i].spaces)
            print()


    def get_round_pieces(self):
        max_roll = len(self.pieces) - 1
        return [
            self.pieces[random.randint(0, max_roll)],
            self.pieces[random.randint(0, max_roll)],
            self.pieces[random.randint(0, max_roll)]
        ]
    

    def q_playable_moves(self):
        open = np.where(self.board.spaces == 0)
        open_coords = np.vstack((open[0], open[1])).T

        # Sort coordinates by distance from center as spaces near the center will be more likely to exit with the true condition more quickly
        sort_by_center = lambda x: math.sqrt((x[0]-5)**2 + (x[1]-5)**2)
        center_sort_order = sort_by_center(open_coords)
        open_coords2 = np.lexsort((open_coords, center_sort_order))

        for i in self.round_pieces:
            for j in open_coords:
                if q_eligible_move(self.board.spaces, i, j) == True:
                    return True
                
        return False


def q_eligible_move(board_spaces, piece: Piece, space_to_check):
    sliced = board_spaces[
        space_to_check[0]:space_to_check[0]+piece.height(), 
        space_to_check[1]:space_to_check[1]+piece.length()
        ]
    
    joined = np.add(sliced, piece.spaces)
    if joined.max() > 1:
        return False
    else:
        return True
    
            

