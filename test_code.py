from game import board
from game import piece

b = board.Board()
print(b.spaces)

pieces = piece.define_pieces()

piece2play = pieces[2]
print(piece2play.spaces)

b.play_piece(piece2play, 0, 0)
print(b.spaces)