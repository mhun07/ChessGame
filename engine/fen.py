from core.game_state import GameState

PIECE_TO_FEN = {
    "wP": "P", "wN": "N", "wB": "B", "wR": "R", "wQ": "Q", "wK": "K",
    "bP": "p", "bN": "n", "bB": "b", "bR": "r", "bQ": "q", "bK": "k",
}
FEN_TO_PIECE = {v: k for k, v in PIECE_TO_FEN.items()}
FILES = "abcdefgh"

def board_to_fen_board(board):
    rows = []
    for row in board:
        empty = 0
        out = ""
        for piece in row:
            if piece == "":
                empty += 1
            else:
                if empty:
                    out += str(empty)
                    empty = 0
                out += PIECE_TO_FEN[piece]
        if empty:
            out += str(empty)
        rows.append(out)
    return "/".join(rows)

def castling_to_fen(rights):
    text = ""
    if rights["w"].get("K"):
        text += "K"
    if rights["w"].get("Q"):
        text += "Q"
    if rights["b"].get("K"):
        text += "k"
    if rights["b"].get("Q"):
        text += "q"
    return text or "-"

def ep_to_fen(ep):
    if ep is None:
        return "-"
    r, c = ep
    return FILES[c] + str(8 - r)

def to_fen(state):
    return " ".join([
        board_to_fen_board(state.board),
        state.turn,
        castling_to_fen(state.castling_rights),
        ep_to_fen(state.en_passant),
        str(state.halfmove_clock),
        str(state.fullmove_number),
    ])

def fen_board_to_board(fen_board):
    board = []
    for row in fen_board.split("/"):
        out = []
        for ch in row:
            if ch.isdigit():
                out.extend([""] * int(ch))
            else:
                out.append(FEN_TO_PIECE[ch])
        board.append(out)
    return board

def from_fen(fen):
    parts = fen.strip().split()
    state = GameState()
    state.board = fen_board_to_board(parts[0])
    state.turn = parts[1]

    rights = parts[2]
    state.castling_rights = {
        "w": {"K": "K" in rights, "Q": "Q" in rights},
        "b": {"K": "k" in rights, "Q": "q" in rights},
    }

    if parts[3] == "-":
        state.en_passant = None
    else:
        file = FILES.index(parts[3][0])
        rank = int(parts[3][1])
        state.en_passant = (8 - rank, file)

    state.halfmove_clock = int(parts[4])
    state.fullmove_number = int(parts[5])
    return state
