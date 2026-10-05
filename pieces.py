start_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq"


class Piece:
    def __init__(self, type, color, img_path):
        self.type = type
        self.color = color
        self.img = img_path



    def load_position_from_fen(fen):
        piece_type_from_symbol = {
            'k': Piece("king", "black", "res/king_black.png"),
            'K': Piece("king", "white", "res/king_white.png"),
            'q': Piece("queen", "black", "res/queen_black.png"),
            'Q': Piece("queen", "white", "res/queen_white.png"),
            'r': Piece("rook", "black", "res/rook_black.png"),
            'R': Piece("rook", "white", "res/rook_white.png"),
            'b': Piece("bishop", "black", "res/bishop_black.png"),
            'B': Piece("bishop", "white", "res/bishop_white.png"),
            'n': Piece("knight", "black", "res/knight_black.png"),
            'N': Piece("knight", "white", "res/knight_white.png"),
            'p': Piece("Pawn", "black", "res/pawn_black.png"),
            'P': Piece("Pawn", "white", "res/pawn_white.png")
        }