from game.piece import *
from game.board import *

import numpy as np
import random
from typing import List
import math

points_for_scoring = 9

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

        self.run_game_loop()


    def run_game_loop(self):
        while self.q_playable_moves():
            self.turn_count += 1
            self.display_ui()

            print("Take Turn: Type <piece number>, <x position>, <y position>")
            print("Quit: Type q or quit")
            move = input()

            if move == 'q' or move == 'quit' or move == 'Q' or move == 'Quit':
                break

            commands = move.split(',')
            commands[0] = int(commands[0])
            commands[1] = int(commands[1])
            commands[2] = int(commands[2])

            if len(commands) > 3:
                print('Unable to parse play, please try again')

            if commands[0] > len(self.round_pieces):
                print('Selected piece not available')

            self.take_turn(commands[0], commands[1], commands[2])

            earned_points = self.board.check_for_complete_regions()
            if earned_points > 0:
                self.streak += 1
            else:
                self.streak = 0

            self.score += 9 * earned_points * earned_points * self.streak

            if len(self.round_pieces) == 0:
                self.round_pieces = self.get_round_pieces()

        print('Thanks for playing!')


            
    def take_turn(self, piece_num, x, y):
        if self.board.play_piece(self.round_pieces[piece_num], x, y):
            del self.round_pieces[piece_num]


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
        center_sort_order = np.array(list(map(sort_by_center, open_coords)))
        #open_coords2 = np.lexsort((open_coords, center_sort_order))

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
    
            

