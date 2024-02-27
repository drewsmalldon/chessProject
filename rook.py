from chess_piece import ChessPiece
from player import Player
from move import Move


class Rook(ChessPiece):

    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        return f"This is a {'White' if self.player == Player.WHITE else 'Black'} rook."

    def type(self):
        return "Rook"

    def is_valid_move(self, move: Move, board: list[list[ChessPiece]]) -> bool:
        if super().is_valid_move(move, board):
            # either column has to be the same or row has to be the same, not both
            if move.from_col == move.to_col and not move.from_row == move.to_row:
                # finding all the spaces in between the start and stop
                min_spot = min(move.to_row, move.from_row) + 1
                max_spot = max(move.to_row, move.from_row)
                # loop through each spot in between, if occupied, cant go to that spot
                for row in range(min_spot, max_spot):
                    if board[row][move.from_col] is not None:
                        return False
                return True

            elif not move.from_col == move.to_col and move.from_row == move.to_row:
                # finding all the spaces in between the start and stop
                min_spot = min(move.to_col, move.from_col) + 1
                max_spot = max(move.to_col, move.from_col)
                # loop through each spot in between, if occupied, cant go to that spot
                for col in range(min_spot, max_spot):
                    if board[move.from_row][col] is not None:
                        return False
                return True
            else:
                return False
        else:
            return False


