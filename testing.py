import unittest
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
from chess_model import ChessModel

class TestChessModel(unittest.TestCase):
    def test_valid_move_pawn(self):
        # Testing all the pawns from starting position, allowing 1 or two spots moved
        move = Move(6, 0, 4, 0)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 0, 5, 0)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 1, 4, 1)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 1, 5, 1)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 2, 4, 2)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 2, 5, 2)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 3, 4, 3)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 3, 5, 3)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 4, 4, 4)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 4, 5, 4)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 5, 4, 5)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 5, 5, 5)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 6, 4, 6)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 6, 5, 6)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 7, 4, 7)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)

        move = Move(6, 7, 5, 7)
        self.chess_model = ChessModel()
        self.assertEqual(self.chess_model.is_valid_move(move), True)





if __name__ == '__main__':
    unittest.main()
