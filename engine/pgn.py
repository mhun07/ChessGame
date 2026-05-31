from datetime import date
from pathlib import Path

from core.config import SAVES_DIR
from engine.notation import result_text


def export_pgn(state, white="Trắng", black="Đen", event="Chess Game", site="Local"):
    result = result_text(state)

    lines = [
        f'[Event "{event}"]',
        f'[Site "{site}"]',
        f'[Date "{date.today().isoformat().replace("-", ".")}"]',
        f'[White "{white}"]',
        f'[Black "{black}"]',
        f'[Result "{result}"]',
        "",
    ]

    moves = []

    for i, move in enumerate(state.move_history):
        if i % 2 == 0:
            moves.append(f"{i // 2 + 1}.")

        san = move.get("san", "")

        if not san:
            san = "..."

        moves.append(san)

    moves.append(result)
    lines.append(" ".join(moves))

    return "\n".join(lines)


def save_pgn(state, filename="game_export.pgn"):
    SAVES_DIR.mkdir(exist_ok=True)

    path = Path(SAVES_DIR) / filename
    path.write_text(export_pgn(state), encoding="utf-8")

    return path
