from chess_piece import ChessPiece
from player import Player
from move import Move


class King(ChessPiece):

    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        return f"This is a {'White' if self.player == Player.WHITE else 'Black'} king."

    def type(self):
        return "King"

    def is_valid_move(self, move: Move, board: list[list[ChessPiece]]) -> bool:
        if super().is_valid_move(move, board):
            # find row and column differences, for reference later
            difference_in_rows = abs(move.to_row - move.from_row)
            difference_in_cols = abs(move.to_col - move.from_col)
            destination = board[move.to_row][move.to_col]
            # checking if the move was a move by 1 space in any direction
            if difference_in_rows <= 1 and difference_in_cols <= 1:
                # if the spot is empty or contains enemy piece, valid move
                if destination is None or destination.player != self.player:
                    return True
            return False

        else:
            return False


