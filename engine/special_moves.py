def update_castling_rights(state, src, dst, piece, captured):
    color = piece[0]

    if piece[1] == "K":
        state.castling_rights[color]["K"] = False
        state.castling_rights[color]["Q"] = False

    if piece[1] == "R":
        if src == (7, 0):
            state.castling_rights["w"]["Q"] = False
        elif src == (7, 7):
            state.castling_rights["w"]["K"] = False
        elif src == (0, 0):
            state.castling_rights["b"]["Q"] = False
        elif src == (0, 7):
            state.castling_rights["b"]["K"] = False

    if captured == "wR":
        if dst == (7, 0):
            state.castling_rights["w"]["Q"] = False
        elif dst == (7, 7):
            state.castling_rights["w"]["K"] = False

    if captured == "bR":
        if dst == (0, 0):
            state.castling_rights["b"]["Q"] = False
        elif dst == (0, 7):
            state.castling_rights["b"]["K"] = False

def apply_special_move(state, src, dst, piece):
    sr, sc = src
    dr, dc = dst
    captured = state.board[dr][dc]

    if piece[1] == "P" and sc != dc and captured == "":
        captured = state.board[sr][dc]
        state.board[sr][dc] = ""

    if piece[1] == "K" and abs(dc - sc) == 2:
        if dc == 6:
            state.board[dr][5] = state.board[dr][7]
            state.board[dr][7] = ""
        elif dc == 2:
            state.board[dr][3] = state.board[dr][0]
            state.board[dr][0] = ""

    return captured

def update_en_passant(state, src, dst, piece):
    state.en_passant = None
    sr, sc = src
    dr, dc = dst
    if piece[1] == "P" and abs(dr - sr) == 2:
        state.en_passant = ((sr + dr) // 2, sc)

def is_promotion(piece, dst):
    return bool(piece and piece[1] == "P" and dst[0] in (0, 7))
