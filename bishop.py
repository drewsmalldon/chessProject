from chess_piece import ChessPiece
from player import Player
from move import Move


class Bishop(ChessPiece):

    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        return f"{'White' if self.player == Player.WHITE else 'Black'} bishop."

    def type(self):
        return "Bishop"

    def is_valid_move(self, move: Move, board) -> bool:
        if not super().is_valid_move(move, board):
            return False
            # checking to make sure both row and column movement are equal - showing diagonal movement
        if abs(move.to_row - move.from_row) == abs(move.to_col - move.from_col):
            verticalMovement = abs(move.from_row - move.to_row)
            destination = board[move.to_row][move.to_col]
            # if bishop is moving up and to the right, check each to make sure there are no pieces in the way
            if destination is None or destination.player != self.player:
                if move.from_col < move.to_col and move.from_row > move.to_row:
                    for spot in range(1, verticalMovement):
                        if board[move.from_row - spot][move.from_col + spot] is not None:
                            return False
                    return True

            # if bishop is moving down and to the right, check each to make sure there are no pieces in the way
                elif move.from_col < move.to_col and move.from_row < move.to_row:
                    for spot in range(1, verticalMovement):
                        if board[move.from_row + spot][move.from_col + spot] is not None:
                            return False
                    return True

            # if bishop is moving down and to the left, check each to make sure there are no pieces in the way
                elif move.from_col > move.to_col and move.from_row < move.to_row:
                    for spot in range(1, verticalMovement):
                        if board[move.from_row + spot][move.from_col - spot] is not None:
                            return False
                    return True

            # if bishop is moving up and to the left, check each to make sure there are no pieces in the way
                elif move.from_col > move.to_col and move.from_row > move.to_row:
                    for spot in range(1, verticalMovement):
                        if board[move.from_row - spot][move.from_col - spot] is not None:
                            return False
                    return True
