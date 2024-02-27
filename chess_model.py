from enum import Enum
from player import Player
from move import Move
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from move import Move

class MoveValidity(Enum):
    Valid = 1
    Invalid = 2
    MovingIntoCheck = 3
    StayingInCheck = 4

    def __str__(self):
        if self.value == 2:
            return 'Invalid move.'

        if self.value == 3:
            return 'Invalid -- cannot move into check.'

        if self.value == 4:
            return 'Invalid -- must move out of check.'


# TODO: create UndoException
class UndoException(Exception):
    pass


class ChessModel:
    # TODO: fill in this class
    def __init__(self, board, player: Player, nrows: int, ncols: int, message_code: MoveValidity):
        self.board = board
        self.__player = player
        self.__nrows = nrows
        self.__ncols = ncols
        self.__message_code = message_code

    @property
    def nrows(self):
        return self.__nrows

    @property
    def ncols(self):
        return self.__ncols

    @property
    def current_player(self):
        return self.__player

    @property
    def message_code(self):
        return self.__message_code

    def is_complete(self) -> bool:
        pass

    def is_valid_move(self, move: Move) -> bool:
        pass

    def move(self, move: Move):
        pass

    def in_check(self, p: Player):
        pass

    def piece_at(self, row: int, col: int) -> ChessPiece:
        pass

    def set_next_player(self):
        pass

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        pass

    def undo(self):
        pass
