from utils.helpers import in_bounds

KNIGHT_DIRS = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
KING_DIRS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
BISHOP_DIRS = [(-1,-1),(-1,1),(1,-1),(1,1)]
ROOK_DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
QUEEN_DIRS = BISHOP_DIRS + ROOK_DIRS

def get_piece_moves(board, pos, state=None, attacks_only=False):
    r, c = pos
    piece = board[r][c]
    if not piece:
        return []

    color, kind = piece[0], piece[1]

    if kind == "P":
        return pawn_moves(board, r, c, color, state, attacks_only)
    if kind == "N":
        return jump_moves(board, r, c, color, KNIGHT_DIRS)
    if kind == "B":
        return slide_moves(board, r, c, color, BISHOP_DIRS)
    if kind == "R":
        return slide_moves(board, r, c, color, ROOK_DIRS)
    if kind == "Q":
        return slide_moves(board, r, c, color, QUEEN_DIRS)
    if kind == "K":
        return king_moves(board, r, c, color, state, attacks_only)

    return []

def pawn_moves(board, r, c, color, state=None, attacks_only=False):
    moves = []
    direction = -1 if color == "w" else 1
    start_row = 6 if color == "w" else 1

    for dc in (-1, 1):
        nr, nc = r + direction, c + dc
        if in_bounds(nr, nc):
            if attacks_only:
                moves.append((nr, nc))
            else:
                target = board[nr][nc]
                if target and target[0] != color:
                    moves.append((nr, nc))
                if state and state.en_passant == (nr, nc):
                    moves.append((nr, nc))

    if attacks_only:
        return moves

    nr = r + direction
    if in_bounds(nr, c) and board[nr][c] == "":
        moves.append((nr, c))
        nr2 = r + 2 * direction
        if r == start_row and in_bounds(nr2, c) and board[nr2][c] == "":
            moves.append((nr2, c))

    return moves

def jump_moves(board, r, c, color, dirs):
    moves = []
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):
            target = board[nr][nc]
            if not target or target[0] != color:
                moves.append((nr, nc))
    return moves

def slide_moves(board, r, c, color, dirs):
    moves = []
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        while in_bounds(nr, nc):
            target = board[nr][nc]
            if not target:
                moves.append((nr, nc))
            else:
                if target[0] != color:
                    moves.append((nr, nc))
                break
            nr += dr
            nc += dc
    return moves

def king_moves(board, r, c, color, state=None, attacks_only=False):
    moves = jump_moves(board, r, c, color, KING_DIRS)

    if attacks_only or state is None:
        return moves

    row = 7 if color == "w" else 0
    rights = state.castling_rights.get(color, {})

    if r == row and c == 4:
        if rights.get("K") and board[row][5] == "" and board[row][6] == "" and board[row][7] == color + "R":
            moves.append((row, 6))
        if rights.get("Q") and board[row][1] == "" and board[row][2] == "" and board[row][3] == "" and board[row][0] == color + "R":
            moves.append((row, 2))

    return moves

def all_pseudo_moves(board, color, state=None):
    moves = []
    for r in range(8):
        for c in range(8):
            if board[r][c] and board[r][c][0] == color:
                for dst in get_piece_moves(board, (r, c), state):
                    moves.append(((r, c), dst))
    return moves
