class Piece:
    """Represents a single chess piece."""
    def __init__(self, color, type):
        self.color = color  # 'white' or 'black'
        self.type = type    # 'pawn', 'rook', 'knight', 'bishop', 'queen', 'king'

    def get_unicode_char(self):
        """Returns the Unicode character for the piece."""
        # Unicode mapping for chess pieces
        unicode_map = {
            ('white', 'pawn'): '♙',
            ('white', 'rook'): '♖',
            ('white', 'knight'): '♘',
            ('white', 'bishop'): '♗',
            ('white', 'queen'): '♕',
            ('white', 'king'): '♔',
            ('black', 'pawn'): '♟',
            ('black', 'rook'): '♜',
            ('black', 'knight'): '♞',
            ('black', 'bishop'): '♝',
            ('black', 'queen'): '♛',
            ('black', 'king'): '♚',
        }
        return unicode_map.get((self.color, self.type), ' ')

    def __repr__(self):
        """String representation for debugging."""
        return f"{self.color} {self.type}"


