import tkinter as tk


class ChessSquare:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    @property
    def is_light(self) -> bool:
        return (self.row + self.col) % 2 != 0

    @property
    def start_x(self) -> int:
        return self.row * 100

    @property
    def start_y(self) -> int:
        return self.col * 100


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
        self.chess_positions = {}
        self.draw_board()

    def draw_board(self):
        for row in range(0, 8):
            for col in range(0, 8):
                square = ChessSquare(row, col)
                square_color = self.LIGHT_COLOR if square.is_light else self.DARK_COLOR
                
                rect_id = self.create_rectangle(
                    square.start_x,
                    square.start_y,
                    square.start_x + 200,
                    square.start_y + 200,
                    fill=square_color
                )
                
                self.chess_positions[(row, col)] = rect_id