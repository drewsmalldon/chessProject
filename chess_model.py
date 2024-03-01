import copy
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
    # UndoException (the GUI is already designed to handle this). LEAVE AS PASS! NO NEED TO DO ANYTHING ELSE
    pass


class ChessModel:
    '''
    This class creates a model of the game of chess. This class holds the chessboard and all the game logic
    '''
    def __init__(self):
        self.__player = Player.WHITE
        self.__nrows = 8
        self.__ncols = 8
        self.__message_code = None
        self.board = [[None] * self.__ncols for i in range(self.__nrows)]
        # list keeping track of all moves
        self.__history = []

        # Set up white pieces
        self.set_piece(0, 0, Rook(Player.BLACK))
        self.set_piece(0, 1, Knight(Player.BLACK))
        self.set_piece(0, 2, Bishop(Player.BLACK))
        self.set_piece(0, 3, Queen(Player.BLACK))
        self.set_piece(0, 4, King(Player.BLACK))
        self.set_piece(0, 5, Bishop(Player.BLACK))
        self.set_piece(0, 6, Knight(Player.BLACK))
        self.set_piece(0, 7, Rook(Player.BLACK))
        for col in range(8):
            self.set_piece(1, col, Pawn(Player.BLACK))

        # Set up black pieces
        self.set_piece(7, 0, Rook(Player.WHITE))
        self.set_piece(7, 1, Knight(Player.WHITE))
        self.set_piece(7, 2, Bishop(Player.WHITE))
        self.set_piece(7, 3, Queen(Player.WHITE))
        self.set_piece(7, 4, King(Player.WHITE))
        self.set_piece(7, 5, Bishop(Player.WHITE))
        self.set_piece(7, 6, Knight(Player.WHITE))
        self.set_piece(7, 7, Rook(Player.WHITE))
        for col in range(8):
            self.set_piece(6, col, Pawn(Player.WHITE))

    @property
    def nrows(self):
        '''
        :return: number of rows
        '''
        return self.__nrows

    @property
    def ncols(self):
        '''
        :return: number of columns
        '''
        return self.__ncols

    @property
    def current_player(self):
        '''
        :return: current player
        '''
        return self.__player

    @property
    def messageCode(self):
        '''
        :return: message code
        '''
        return self.__message_code

    def is_complete(self) -> bool:
        '''
        This method will return true or false based on if the game is complete
        :return: true or false
        '''
        # we will later determine if player in check, and if there are moves available
        in_check = False
        has_moves_available = False

        # if in check, make in_check true
        if self.in_check(self.current_player):
            in_check = True

        # if there is a move available, make has moves available true
        # loop through all squares on the chess board
        for row in range(self.__nrows):
            for col in range(self.__ncols):
                # grab current piece belonging to self.player
                piece = self.piece_at(row, col)
                # if there is a piece belonging to player loop through all possible destinations
                if piece and piece.player == self.current_player:
                    for to_row in range(self.__nrows):
                        for to_col in range(self.__ncols):
                            # create a variable for each potential move
                            move = Move(row, col, to_row, to_col)
                            # if that move is a valid move, then there is moves available, so then break out of all loops
                            if self.is_valid_move(move):
                                has_moves_available = True
                                break

                        if has_moves_available:
                            break
                    if has_moves_available:
                        break
                if has_moves_available:
                    break

        # if the player is in check and has no moves, GAME OVER
        if in_check and not has_moves_available:
            return True

        # otherwise game is not done
        return False



    def is_valid_move(self, move: Move) -> bool:
        '''
        This method will check if the move was valid
        :param move: the spot the piece wants to move to
        :return: true or false
        '''
        # check if move is within bounds
        if (
            move.from_row < 0 or
            move.from_col < 0 or
            move.from_row > self.__nrows or
            move.from_col > self.__ncols
        ):
            self.__message_code = MoveValidity.Invalid
            return False

        if (
            move.to_row < 0 or
            move.to_col < 0 or
            move.to_row > self.__nrows or
            move.to_col > self.__ncols
        ):
            self.__message_code = MoveValidity.Invalid
            return False

        # grab the target piece object
        piece = self.piece_at(move.from_row, move.from_col)
        # if none, return false
        if piece is None:
            self.__message_code = MoveValidity.Invalid
            return False

        # make sure it is the players turn
        if piece.player != self.current_player:
            self.__message_code = MoveValidity.Invalid
            return False

        # Check specific pieces move validity
        if not piece.is_valid_move(move, self.board):
            self.__message_code = MoveValidity.Invalid
            return False

        # create a copy of board called temp board to simulate the move
        temp = copy.deepcopy(self.board)
        # set old spot to none and update values
        temp[move.to_row][move.to_col] = temp[move.from_row][move.from_col]
        temp[move.from_row][move.from_col] = None

        # check if in check after the move
        if self.in_check(self.current_player, temp):
            self.__message_code = MoveValidity.MovingIntoCheck
            return False
        # if all checks out, valid move
        self.__message_code = MoveValidity.Valid
        return True

    def move(self, move: Move):
        '''
        carries out move provided in the move object
        :param move: move object
        :return: none
        '''
        if self.is_valid_move(move):
            # add move to history
            self.__history.append(move)

            # check if pawn needs to get promoted
            piece = self.board[move.from_row][move.from_col]
            if isinstance(piece, Pawn) and (move.to_row == 0 or move.to_row == 7):
                # replace with queen
                self.board[move.to_row][move.to_col] = Queen(piece.player)
            else:
                # move normally
                self.board[move.to_row][move.to_col] = self.board[move.from_row][move.from_col]

            # clear starting position
            self.board[move.from_row][move.from_col] = None

            self.set_next_player()
            return True
        else:
            return False

    def in_check(self, p: Player, board = None):
        '''
        Check if a player is in check
        :param p: current player
        :param board: whether it is temp or normal board
        :return: none
        '''
        # allow board attribute to use a temp board for checking, if no board is passed, its the normal board
        if board is None:
            board = self.board
        # initialize king row and col
        king_row, king_col = None, None

        # find the current location of the king of current player
        for row in range(self.__nrows):
            for col in range(self.__ncols):
                piece = board[row][col]
                if isinstance(piece, King) and piece.player == p:
                    king_row, king_col = row, col
                    break
            if king_row is not None:
                break
        if king_row is None:
            raise ValueError("King not on the board")

        # check if opponent is threatening current players king
        for row in range(self.__nrows):
            for col in range(self.__ncols):
                piece = board[row][col]
                if piece is not None and piece.player != p:
                    # move the piece to the king, if that is allowed, in check is true
                    move = Move(row, col, king_row, king_col)
                    if piece.is_valid_move(move, board):
                        return True
    def piece_at(self, row: int, col: int) -> ChessPiece:
        '''
        returns current piece at a current location
        :param row: row
        :param col: column
        :return: chessPiece
        '''
        return self.board[row][col]

    def set_next_player(self):
        '''
        sets the player to the next player after turn
        :return: none
        '''
        if self.current_player == Player.WHITE:
            self.__player = Player.BLACK
        else:
            self.__player = Player.WHITE

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        '''
        sets piece on board
        :param row: row
        :param col: column
        :param piece: what piece is it
        :return: none
        '''
        # checks if row and col are in bounds
        if not (0 <= row < self.__nrows) or not (0 <= col <= self.__ncols):
            raise ValueError("Row and Column must be in bounds")
        # check if piece is type chesspiece
        if not isinstance(piece, ChessPiece):
            raise TypeError("Piece must be a Chess piece.")
        self.board[row][col] = piece

    def undo(self):
        '''
        undo move
        :return: none
        '''
        if len(self.__history) == 0:
            raise UndoException("No moves to undo!")

        previous_move = self.__history.pop()

        # reverse the move
        self.board[previous_move.from_row][previous_move.from_col] = self.board[previous_move.to_row][previous_move.to_col]
        self.board[previous_move.to_row][previous_move.to_col] = None

