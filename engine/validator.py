from utils.helpers import opposite, clone_board
from engine.move_generator import get_piece_moves


def find_king(board, color):
    king = color + "K"

    for r in range(8):
        for c in range(8):
            if board[r][c] == king:
                return (r, c)

    return None


def is_square_attacked(board, square, by_color, state=None):
    for r in range(8):
        for c in range(8):
            piece = board[r][c]

            if not piece or piece[0] != by_color:
                continue

            if square in get_piece_moves(board, (r, c), state, attacks_only=True):
                return True

    return False


def is_in_check(board, color, state=None):
    king_pos = find_king(board, color)

    if king_pos is None:
        return True

    return is_square_attacked(board, king_pos, opposite(color), state)


def simulate_move(board, src, dst, promotion="Q"):
    new = clone_board(board)
    _apply_temp_move(new, src, dst, promotion)
    return new


def _apply_temp_move(board, src, dst, promotion="Q"):
    sr, sc = src
    dr, dc = dst

    piece = board[sr][sc]
    captured_main = board[dr][dc]
    en_passant_capture = None
    rook_move = None

    board[sr][sc] = ""

    if piece and piece[1] == "P" and sc != dc and captured_main == "":
        en_passant_capture = (sr, dc, board[sr][dc])
        board[sr][dc] = ""

    if piece and piece[1] == "K" and abs(dc - sc) == 2:
        if dc == 6:
            rook_move = ((dr, 7), (dr, 5), board[dr][7], board[dr][5])
            board[dr][5] = board[dr][7]
            board[dr][7] = ""

        elif dc == 2:
            rook_move = ((dr, 0), (dr, 3), board[dr][0], board[dr][3])
            board[dr][3] = board[dr][0]
            board[dr][0] = ""

    placed_piece = piece

    if piece and piece[1] == "P" and dr in (0, 7):
        placed_piece = piece[0] + promotion

    board[dr][dc] = placed_piece

    undo_data = {
        "src": src,
        "dst": dst,
        "piece": piece,
        "captured_main": captured_main,
        "en_passant_capture": en_passant_capture,
        "rook_move": rook_move,
    }

    return undo_data


def _undo_temp_move(board, undo_data):
    sr, sc = undo_data["src"]
    dr, dc = undo_data["dst"]

    board[sr][sc] = undo_data["piece"]
    board[dr][dc] = undo_data["captured_main"]

    if undo_data["en_passant_capture"]:
        r, c, piece = undo_data["en_passant_capture"]
        board[r][c] = piece

    if undo_data["rook_move"]:
        rook_src, rook_dst, rook_piece, rook_dst_old = undo_data["rook_move"]
        rsr, rsc = rook_src
        rdr, rdc = rook_dst
        board[rsr][rsc] = rook_piece
        board[rdr][rdc] = rook_dst_old


def castle_path_safe(state, color, src, dst):
    row = 7 if color == "w" else 0
    enemy = opposite(color)

    if is_in_check(state.board, color, state):
        return False

    path = [(row, 5), (row, 6)] if dst[1] == 6 else [(row, 3), (row, 2)]

    return all(
        not is_square_attacked(state.board, sq, enemy, state)
        for sq in path
    )


def legal_moves_for_piece(state, src):
    board = state.board
    r, c = src
    piece = board[r][c]

    if not piece:
        return []

    color = piece[0]
    legal = []

    for dst in get_piece_moves(board, src, state):
        if piece[1] == "K" and abs(dst[1] - c) == 2:
            if not castle_path_safe(state, color, src, dst):
                continue

        # Tối ưu: áp dụng tạm trên board thật rồi undo, tránh copy board nhiều lần.
        undo_data = _apply_temp_move(board, src, dst)

        safe = not is_in_check(board, color, state)

        _undo_temp_move(board, undo_data)

        if safe:
            legal.append(dst)

    return legal


def all_legal_moves(state, color):
    moves = []

    for r in range(8):
        for c in range(8):
            piece = state.board[r][c]

            if piece and piece[0] == color:
                src = (r, c)

                for dst in legal_moves_for_piece(state, src):
                    moves.append((src, dst))

    return moves


def is_checkmate(state, color):
    return is_in_check(state.board, color, state) and len(all_legal_moves(state, color)) == 0


def is_stalemate(state, color):
    return not is_in_check(state.board, color, state) and len(all_legal_moves(state, color)) == 0
