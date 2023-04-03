import numpy as np

class Piece:
    spaces: np.array

    def __init__(self, spaces):
        self.spaces = spaces

    def height(self):
        return self.spaces.shape[0]
    
    def length(self):
        return self.spaces.shape[1]


# Pieces are defined in such a way that every piece has a (0, 0) that's used as the primary placement point


@staticmethod
def define_pieces():
    pieces = []

    # Dot
    pieces.append(Piece(np.array([
        [1]
    ])))

    # Horizontal 2
    pieces.append(Piece(np.array([
        [1, 1]
    ])))

    # Horizontal 3
    pieces.append(Piece(np.array([
        [1, 1, 1]
    ])))

    # Horizontal 4
    pieces.append(Piece(np.array([
        [1, 1, 1, 1]
    ])))

    # Horizontal 5
    pieces.append(Piece(np.array([
        [1, 1, 1, 1, 1]
    ])))

    # Vertical 2
    pieces.append(Piece(np.array([
        [1],
        [1]
    ])))

    # Vertical 3
    pieces.append(Piece(np.array([
        [1],
        [1],
        [1]
    ])))

    # Vertical 4
    pieces.append(Piece(np.array([
        [1],
        [1],
        [1],
        [1]
    ])))

    # Vertical 5
    pieces.append(Piece(np.array([
        [1],
        [1],
        [1],
        [1],
        [1]
    ])))

    # Left L 1
    pieces.append(Piece(np.array([
        [1, 0],
        [1, 0],
        [1, 1]
    ])))

    # Left L 2
    pieces.append(Piece(np.array([
        [1, 1, 1],
        [1, 0, 0],
    ])))

    # Left L 3
    pieces.append(Piece(np.array([
        [1, 1],
        [0, 1],
        [0, 1],
    ])))

    # Left L 4
    pieces.append(Piece(np.array([
        [0, 0, 1],
        [1, 1, 1]
    ])))

    # Right L 1
    pieces.append(Piece(np.array([
        [0, 1],
        [0, 1],
        [1, 1]
    ])))

    # Right L 2
    pieces.append(Piece(np.array([
        [1, 1, 1],
        [0, 0, 1],
    ])))

    # Right L 3
    pieces.append(Piece(np.array([
        [1, 1],
        [1, 0],
        [1, 0],
    ])))

    # Right L 4
    pieces.append(Piece(np.array([
        [1, 0, 0],
        [1, 1, 1]
    ])))

    # Big L 1
    pieces.append(Piece(np.array([
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 1]
    ])))

    # Big L 2
    pieces.append(Piece(np.array([
        [1, 1, 1],
        [1, 0, 0],
        [1, 0, 0],
    ])))

    # Big L 3
    pieces.append(Piece(np.array([
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
    ])))

    # Big L 4
    pieces.append(Piece(np.array([
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ])))

    # Square
    pieces.append(Piece(np.array([
        [1, 1],
        [1, 1]
    ])))

    # Squiggle 1
    pieces.append(Piece(np.array([
        [0, 1, 1],
        [1, 1, 0]
    ])))

    # Squiggle 2
    pieces.append(Piece(np.array([
        [1, 0],
        [1, 1],
        [0, 1]
    ])))

    # Squiggle 3
    pieces.append(Piece(np.array([
        [1, 1, 0],
        [0, 1, 1]
    ])))

    # Squiggle 4
    pieces.append(Piece(np.array([
        [0, 1],
        [1, 1],
        [1, 0]
    ])))

    # Cross
    pieces.append(Piece(np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ])))

    # Part Cross 1
    pieces.append(Piece(np.array([
        [0, 1, 0],
        [1, 1, 1]
    ])))

    # Part Cross 2
    pieces.append(Piece(np.array([
        [1, 0],
        [1, 1],
        [1, 0]
    ])))

    # Part Cross 3
    pieces.append(Piece(np.array([
        [1, 1, 1],
        [0, 1, 0]
    ])))

    # Part Cross 4
    pieces.append(Piece(np.array([
        [0, 1],
        [1, 1],
        [0, 1]
    ])))

    # Diag 2 Up
    pieces.append(Piece(np.array([
        [0, 1],
        [1, 0]
    ])))

    # Diag 3 Up
    pieces.append(Piece(np.array([
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ])))

    # Diag 4 Up
    pieces.append(Piece(np.array([
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]
    ])))

    # Diag 2 Down
    pieces.append(Piece(np.array([
        [1, 0],
        [0, 1]
    ])))

    # Diag 3 Down
    pieces.append(Piece(np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])))

    # Diag 4 Down
    pieces.append(Piece(np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])))
    
    # for piece in pieces:
    #     for i in range(0, 5):
    #         for j in range(0, 5):
    #             print(piece.spaces[i][j], end='')
    #         print()
    #     print()

    return pieces

    