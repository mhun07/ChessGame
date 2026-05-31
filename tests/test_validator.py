import unittest

from core.game_state import GameState
from engine.validator import is_in_check, legal_moves_for_piece


class TestValidator(unittest.TestCase):
    def test_start_position_not_in_check(self):
        state = GameState()

        self.assertFalse(is_in_check(state.board, "w", state))
        self.assertFalse(is_in_check(state.board, "b", state))

    def test_knight_has_two_legal_moves_at_start(self):
        state = GameState()

        moves = legal_moves_for_piece(state, (7, 1))

        self.assertIn((5, 0), moves)
        self.assertIn((5, 2), moves)
        self.assertEqual(len(moves), 2)

    def test_simple_check_detection(self):
        state = GameState()
        state.board = [[""] * 8 for _ in range(8)]
        state.board[7][4] = "wK"
        state.board[0][4] = "bR"
        state.board[0][0] = "bK"

        self.assertTrue(is_in_check(state.board, "w", state))


if __name__ == "__main__":
    unittest.main()
