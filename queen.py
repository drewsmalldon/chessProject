from chess_piece import ChessPiece
from player import Player
from move import Move


class Queen(ChessPiece):

    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        return f"This is a {'White' if self.player == Player.WHITE else 'Black'} Queen."

    def type(self):
        return "Queen"

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
            verticalMovement = abs(move.from_row - move.to_row)
            destination = board[move.to_row][move.to_col]
            # checking to make sure both row and column movement are equal - showing diagonal movement
            if abs(move.to_row - move.from_row) == abs(move.to_col - move.from_col):
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
        return False


