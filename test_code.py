from game.board import Board
from game.piece import *
from game.game import Game

import logging
import os

if os.path.exists('./Debug.log'):
    os.remove('./Debug.log')
logging.basicConfig(filename='./Debug.log', level=logging.INFO)

game = Game()


abc = np.where(game.board.spaces == 0)
stacked = np.vstack((abc[0], abc[1])).T
print(stacked)