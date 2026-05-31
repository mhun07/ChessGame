import unittest

from core.game_state import GameState
from engine.special_moves import update_en_passant, is_promotion


class TestSpecialMoves(unittest.TestCase):
    def test_en_passant_square_after_double_pawn_move(self):
        state = GameState()
        piece = state.board[6][4]  # wP ở e2

        update_en_passant(state, (6, 4), (4, 4), piece)

        self.assertEqual(state.en_passant, (5, 4))

    def test_promotion_detection(self):
        self.assertTrue(is_promotion("wP", (0, 0)))
        self.assertTrue(is_promotion("bP", (7, 0)))
        self.assertFalse(is_promotion("wP", (4, 0)))
        self.assertFalse(is_promotion("wQ", (0, 0)))


if __name__ == "__main__":
    unittest.main()
