from chess_board import ChessBoard
import tkinter as tk
class ChessApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess")
        self.window.geometry("1200x1200")
        
        # Configure root layout centering
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        # Initialize Board Widget
        self.board = ChessBoard(self.window)
        self.board.grid(row=0, column=0, sticky="")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = ChessApp()
    app.run()