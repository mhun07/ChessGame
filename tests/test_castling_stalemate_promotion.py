import unittest

from core.game_state import GameState
from engine.validator import legal_moves_for_piece, is_stalemate
from engine.logic import try_move


class TestAdvancedChessRules(unittest.TestCase):
    def test_kingside_castling_available_when_path_clear(self):
        state = GameState()
        state.board[7][5] = ""
        state.board[7][6] = ""

        moves = legal_moves_for_piece(state, (7, 4))

        self.assertIn((7, 6), moves)

    def test_castling_not_available_when_king_in_check(self):
        state = GameState()
        state.board[7][5] = ""
        state.board[7][6] = ""
        state.board[0][4] = ""
        state.board[3][4] = "bR"

        moves = legal_moves_for_piece(state, (7, 4))

        self.assertNotIn((7, 6), moves)

    def test_simple_stalemate(self):
        state = GameState()
        state.board = [[""] * 8 for _ in range(8)]
        state.board[0][0] = "bK"
        state.board[2][1] = "wQ"
        state.board[1][2] = "wK"
        state.turn = "b"

        self.assertTrue(is_stalemate(state, "b"))

    def test_promotion_to_knight(self):
        state = GameState()
        state.board = [[""] * 8 for _ in range(8)]
        state.board[1][0] = "wP"
        state.board[7][4] = "wK"
        state.board[0][7] = "bK"
        state.turn = "w"

        result = try_move(state, (1, 0), (0, 0), promotion="N")

        self.assertTrue(result)
        self.assertEqual(state.board[0][0], "wN")


if __name__ == "__main__":
    unittest.main()
