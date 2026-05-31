from core.config import BOARD_X, BOARD_Y, SQ, BOARD_SIZE

def in_bounds(r, c):
    return 0 <= r < 8 and 0 <= c < 8

def opposite(color):
    return "b" if color == "w" else "w"

def clone_board(board):
    return [row[:] for row in board]

def square_to_screen(row, col):
    return BOARD_X + col * SQ, BOARD_Y + row * SQ

def screen_to_square(x, y):
    if not (BOARD_X <= x < BOARD_X + BOARD_SIZE and BOARD_Y <= y < BOARD_Y + BOARD_SIZE):
        return None
    return (y - BOARD_Y) // SQ, (x - BOARD_X) // SQ
