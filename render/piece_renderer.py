from core.config import BOARD_X, BOARD_Y, SQ


def draw_pieces(screen, state):
    for r in range(8):
        for c in range(8):
            piece = state.board[r][c]

            if not piece:
                continue

            img = state.piece_images.get(piece)

            if img:
                screen.blit(
                    img,
                    (
                        BOARD_X + c * SQ,
                        BOARD_Y + r * SQ
                    )
                )
