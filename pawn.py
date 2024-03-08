from chess_piece import ChessPiece
from player import Player
from move import Move
from queen import Queen


class Pawn(ChessPiece):

    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        return f"{'White' if self.player == Player.WHITE else 'Black'} pawn."

    def type(self):
        return "Pawn"

    def is_valid_move(self, move: Move, board) -> bool:
        # check if it's a move within range of the board (from chessPiece)
        if not super().is_valid_move(move, board):
            return False
            # recreating this variable to keep track of the end spot for checking
        end_spot = board[move.to_row][move.to_col]
        # Checking player color, for different integer value changes
        if self.player == Player.WHITE:
            # if it is moving from starting location, it is allowed to move forward 2 spaces, if there is
            # not a piece in between starting and ending locations (at row 5)
            if move.from_row == 6 and move.to_row == 4 and move.from_col == move.to_col:
                if board[5][move.from_col] is None and end_spot is None:
                    return True
            # capture move, checking if it moves diagonally, only allowed if the space is occupied
            elif move.to_row == move.from_row - 1 and abs(move.to_col - move.from_col) == 1:
                if end_spot is not None:
                    return True
            # typical move of one space difference
            elif move.to_row == move.from_row - 1 and move.to_col == move.from_col:
                # if space is occupied, cant move there
                if end_spot is None:
                    return True

        # if player is the color black, we have to change integer values to + not - as they are moving
        # the other way on the board.
        elif self.player == Player.BLACK:
            # if it is moving from starting location, it is allowed to move forward 2 spaces, if there is
            # not a piece in between starting and ending locations (at row 2)
            if move.from_row == 1 and move.to_row == 3 and move.from_col == move.to_col:
                if board[2][move.from_col] is None and end_spot is None:
                    return True
            # capture move, checking if it moves diagonally, only allowed if the space is occupied
            if move.to_row == move.from_row + 1 and abs(move.to_col - move.from_col) == 1:
                if end_spot is not None:
                    return True
            # typical move of one space difference
            if move.to_row == move.from_row + 1 and move.to_col == move.from_col:
                # if space is occupied, cant move there
                if end_spot is None:
                    return True
        return False
