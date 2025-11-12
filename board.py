from pieces import Piece

class Board:
    """Represents the chessboard and handles its display."""
    def __init__(self):
        # The board is an 8x8 list of lists (or a 2D array)
        # Each element can be a Piece object or None (for empty squares)
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        """Places the pieces in their initial positions."""
        # Place pawns
        for i in range(8):
            # i is the column index (0-7), 1 is the row index (for white pawns), etc.
            self.board[1][i] = Piece('black', 'pawn')
            self.board[6][i] = Piece('white', 'pawn')

        # Place back row pieces
        back_row_order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for i, piece_type in enumerate(back_row_order):
            self.board[0][i] = Piece('black', piece_type)
            self.board[7][i] = Piece('white', piece_type)

    def display(self):
        """Prints the current state of the board to the terminal."""
        print("  a b c d e f g h")
        print(" +-----------------+")
        # Rows in the list index go from 0 (rank 8) to 7 (rank 1)
        for i in range(8):
            row_label = 8 - i
            row_str = f"{row_label}|"
            for j in range(8):
                piece = self.board[i][j]
                if piece:
                    # Add a space for better visibility
                    row_str += f"{piece.get_unicode_char()} "
                else:
                    # Use a space for empty squares
                    row_str += ". "
            row_str += f"|{row_label}"
            print(row_str)
        print(" +-----------------+")
        print("  a b c d e f g h")

    def get_piece(self, row, col):
        """Gets the piece at a specific board coordinate (0-indexed)."""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def set_piece(self, row, col, piece):
        """Places a piece at a specific board coordinate (0-indexed)."""
        if 0 <= row < 8 and 0 <= col < 8:
            self.board[row][col] = piece

