FILES = "abcdefgh"


def square_name(pos):
    r, c = pos
    return FILES[c] + str(8 - r)


def move_to_coord(src, dst, promotion=None):
    text = square_name(src) + square_name(dst)
    if promotion:
        text += promotion.lower()
    return text


def result_text(state):
    if not state.game_over:
        return "*"

    text = state.winner_text.lower()

    if "trắng thắng" in text or "white wins" in text:
        return "1-0"

    if "đen thắng" in text or "black wins" in text:
        return "0-1"

    return "1/2-1/2"


def simple_san(piece, src, dst, captured="", promotion=None, castle=False, check=False, mate=False):
    if castle:
        text = "O-O" if dst[1] == 6 else "O-O-O"

    else:
        kind = "" if piece[1] == "P" else piece[1]
        capture = "x" if captured else ""

        if piece[1] == "P" and captured:
            kind = FILES[src[1]]

        text = f"{kind}{capture}{square_name(dst)}"

        if promotion:
            text += f"={promotion}"

    if mate:
        text += "#"
    elif check:
        text += "+"

    return text
