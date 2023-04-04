import tensorflow as tf
from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *

def woodoku_model():
    input_board = Input(shape=(9, 9, 4), dtype='int16', name='board_input')

