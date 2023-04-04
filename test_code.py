from game.board import Board
from game.piece import *
from game.game import Game

import logging
import os

if os.path.exists('./Debug.log'):
    os.remove('./Debug.log')
logging.basicConfig(filename='./Debug.log', level=logging.INFO)


game = Game()

print(game.game_state())