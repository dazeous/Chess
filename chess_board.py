import tkinter as tk
from pieces import get_piece

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq"


class ChessSquare:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    @property
    def is_light(self) -> bool:
        return (self.row + self.col) % 2 != 0

    @property
    def x(self) -> int:
        return self.col * 100

    @property
    def y(self) -> int:
        return self.row * 100


class ChessBoard(tk.Canvas):
    LIGHT_COLOR = "#D3C696"
    DARK_COLOR = "#2D8931"

    def __init__(self, master):
        super().__init__(
            master,
            width=800,
            height=800,
            bg="white",
            highlightthickness=4,
            highlightbackground="black",
        )
        self.square_ids = {}     # Maps (row, col) -> canvas_rectangle_id
        self.board_state = {}     # Maps (row, col) -> Piece instance
        self.piece_ids = {}      # Maps (row, col) -> canvas_image_id
        self._image_cache = []   # Prevents garbage collection of Tkinter images

        self.draw_board()
        self.load_position_from_fen(START_FEN)

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                square = ChessSquare(row, col)
                square_color = self.LIGHT_COLOR if square.is_light else self.DARK_COLOR

                rect_id = self.create_rectangle(
                    square.x,
                    square.y,
                    square.x + 200,
                    square.y + 200,
                    fill=square_color
                )
                self.square_ids[(row, col)] = rect_id

    def display_piece(self, piece, row: int, col: int):
        """Draws a piece on the canvas at (row, col) and tracks its ID."""
        x = col * 100 + 5
        y = row * 100 + 5

        tk_img = piece.load_image()
        self._image_cache.append(tk_img)

        # NW anchor places top-left corner of the image at (x, y)
        img_id = self.create_image(x, y, image=tk_img, anchor="nw", tags="piece")

        # Track state & image IDs
        self.board_state[(row, col)] = piece
        self.piece_ids[(row, col)] = img_id

    def load_position_from_fen(self, fen: str):
        # Clear existing pieces
        self.delete("piece")
        self.board_state.clear()
        self.piece_ids.clear()

        fen_board = fen.split(' ')[0]
        row, col = 0, 0

        for symbol in fen_board:
            if symbol == '/':
                row += 1
                col = 0
            elif symbol.isdigit():
                col += int(symbol)
            else:
                piece = get_piece(symbol)
                self.display_piece(piece, row, col)
                col += 1

    def move_piece(self, from_sq: tuple[int, int], to_sq: tuple[int, int]):
        """Helper method for future move logic."""
        if from_sq not in self.piece_ids:
            return

        piece_id = self.piece_ids.pop(from_sq)
        piece = self.board_state.pop(from_sq)

        # Handle capture on destination square
        if to_sq in self.piece_ids:
            self.delete(self.piece_ids[to_sq])

        # Animate / Reposition image on canvas
        to_x = to_sq[1] * 100
        to_y = to_sq[0] * 100
        self.coords(piece_id, to_x, to_y)

        # Update mappings
        self.piece_ids[to_sq] = piece_id
        self.board_state[to_sq] = piece