from chess_piece import ChessPiece
from player import Player
from move import Move


class Knight(ChessPiece):

    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        return f"This is a {'White' if self.player == Player.WHITE else 'Black'} Knight."

    def type(self):
        return "Knight"

    def is_valid_move(self, move: Move, board: list[list[ChessPiece]]) -> bool:
        if super().is_valid_move(move, board):
            # find differences in rows and columns to use later
            difference_in_rows = abs(move.to_row - move.from_row)
            difference_in_cols = abs(move.to_col - move.from_col)
            destination = board[move.to_row][move.to_col]
            # if the moves create the L shape, then it is a valid move
            if (
                    difference_in_rows == 2 and difference_in_cols == 1 or
                    difference_in_cols == 2 and difference_in_rows == 1
                ):
                # if there is no piece in destination or theres an enemy piece, you can move there
                if destination is None or destination.player != self.player:
                    return True
            return False

        else:
            return False


