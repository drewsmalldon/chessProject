from abc import ABC, abstractmethod
from move import Move
from player import Player


class ChessPiece(ABC):
    '''
    This class is a parent class of each of the chess pieces. It contains abstract classes that all the pieces
    must have in their layout
    '''

    def __init__(self, player: Player):
        self.__player = player

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, new_player):
        self.__player = new_player

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def is_valid_move(self, move: Move, board) -> bool:
        # making sure the move is a valid spot, between indexes 0 and 7
        if (
            move.from_row < 0 or
            move.from_col < 0 or
            move.from_row > 7 or
            move.from_col > 7
        ):
            return False

        if (
            move.to_row < 0 or
            move.to_col < 0 or
            move.to_row > 7 or
            move.to_col > 7
        ):
            return False

        # making sure starting and ending locations are different
        start_spot = board[move.from_row][move.from_col]
        end_spot = board[move.to_row][move.to_col]
        if start_spot == end_spot:
            return False

        # making sure self is located at starting location in move
        if start_spot != self:
            return False

        # making sure end location does not already contain player's piece
        if end_spot is not None and end_spot.player == self.player:
            return False
        # If all is good, return true - good move
        return True
