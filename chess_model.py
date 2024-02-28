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
    # If the undo method is called when there are no moves left to undo, raise an
    # UndoException (the GUI is already designed to handle this).
    pass


class ChessModel:
    # TODO: fill in this class
    def __init__(self):
        self.__player = Player.WHITE
        self.__nrows = 8
        self.__ncols = 8
        self.__message_code = None
        # setting the whole board as none
        self.board = [[None for i in range(self.__nrows)] for i in range(self.__ncols)]
        # setting starter pieces
        self.set_board()

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

    def set_board(self):
        # THIS THROWS AN ERROR WHEN GUI TRIES TO RUN, COULD BE WRONG
        # put pieces in starting position
        # pawns
        self.set_piece(1, 0, Pawn(Player.BLACK))
        self.set_piece(1, 1, Pawn(Player.BLACK))
        self.set_piece(1, 2, Pawn(Player.BLACK))
        self.set_piece(1, 3, Pawn(Player.BLACK))
        self.set_piece(1, 4, Pawn(Player.BLACK))
        self.set_piece(1, 5, Pawn(Player.BLACK))
        self.set_piece(1, 6, Pawn(Player.BLACK))
        self.set_piece(1, 7, Pawn(Player.BLACK))

        self.set_piece(6, 0, Pawn(Player.WHITE))
        self.set_piece(6, 1, Pawn(Player.WHITE))
        self.set_piece(6, 2, Pawn(Player.WHITE))
        self.set_piece(6, 3, Pawn(Player.WHITE))
        self.set_piece(6, 4, Pawn(Player.WHITE))
        self.set_piece(6, 5, Pawn(Player.WHITE))
        self.set_piece(6, 6, Pawn(Player.WHITE))
        self.set_piece(6, 7, Pawn(Player.WHITE))

        # rooks
        self.set_piece(0, 0, Rook(Player.BLACK))
        self.set_piece(0, 7, Rook(Player.BLACK))
        self.set_piece(7, 0, Rook(Player.WHITE))
        self.set_piece(7, 7, Rook(Player.WHITE))

        # knights
        self.set_piece(0, 1, Knight(Player.BLACK))
        self.set_piece(0, 6, Knight(Player.BLACK))
        self.set_piece(7, 1, Knight(Player.WHITE))
        self.set_piece(7, 6, Knight(Player.WHITE))

        # bishops
        self.set_piece(0, 2, Bishop(Player.BLACK))
        self.set_piece(0, 5, Bishop(Player.BLACK))
        self.set_piece(7, 2, Bishop(Player.WHITE))
        self.set_piece(7, 5, Bishop(Player.WHITE))

        # queens
        self.set_piece(0, 3, Queen(Player.BLACK))
        self.set_piece(7, 3, Queen(Player.WHITE))

        # kings
        self.set_piece(0, 4, King(Player.BLACK))
        self.set_piece(7, 4, King(Player.WHITE))

    def is_complete(self) -> bool:
        # check if game is complete
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
        if not 0 <= row < 7 or not 0 <= col < 7:
            raise ValueError("Row or Column out of bounds!")
        if not isinstance(piece, ChessPiece):
            raise TypeError("Piece is Invalid!")

    def undo(self):
        pass
