from PIL import Image, ImageTk


class Piece:
    def __init__(self, piece_type: str, color: str, symbol: str):
        self.type = piece_type
        self.color = color
        self.symbol = symbol
        self.tk_image = None
    def load_image(self, target_size: int = 85):
        if self.tk_image is None:
            filename = f"res/{self.type}_{self.color}.png"
            img = Image.open(filename)
            # Resize using Lanczos resampling for crisp quality
            img = img.resize((target_size, target_size), Image.Resampling.LANCZOS)
            self.tk_image = ImageTk.PhotoImage(img)
        return self.tk_image


# Factory mapping by FEN symbol
PIECE_SPECS = {
    'k': ('king', 'black'),   'K': ('king', 'white'),
    'q': ('queen', 'black'),  'Q': ('queen', 'white'),
    'r': ('rook', 'black'),   'R': ('rook', 'white'),
    'b': ('bishop', 'black'), 'B': ('bishop', 'white'),
    'n': ('knight', 'black'), 'N': ('knight', 'white'),
    'p': ('pawn', 'black'),   'P': ('pawn', 'white'),
}

def get_piece(symbol: str) -> Piece:
    piece_type, color = PIECE_SPECS[symbol]
    return Piece(piece_type, color, symbol)