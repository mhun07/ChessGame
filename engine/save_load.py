import json
from pathlib import Path

from core.config import SAVES_DIR
from engine.fen import to_fen, from_fen


last_error = ""


def _safe_float(value, default):
    try:
        value = float(value)
        return max(0.0, value)
    except (TypeError, ValueError):
        return default


def _safe_list(value):
    return value if isinstance(value, list) else []


def save_game(state, filename="savegame.json"):
    SAVES_DIR.mkdir(exist_ok=True)

    path = Path(SAVES_DIR) / filename

    data = {
        "fen": to_fen(state),
        "white_time": state.white_timer.time_left,
        "black_time": state.black_timer.time_left,
        "move_history": state.move_history,
        "captured_white": state.captured_white,
        "captured_black": state.captured_black,
        "replay_snapshots": state.replay_snapshots,
        "replay_index": state.replay_index,
    }

    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    state.set_message("Đã lưu ván đấu")
    return path


def load_game(filename="savegame.json"):
    global last_error

    path = Path(SAVES_DIR) / filename

    if not path.exists():
        last_error = f"Không tìm thấy file save: {path.name}"
        print(last_error)
        return None

    try:
        data = json.loads(path.read_text(encoding="utf-8"))

        if not isinstance(data, dict):
            raise ValueError("File save không đúng định dạng JSON object.")

        fen = data.get("fen")

        if not isinstance(fen, str) or len(fen.split()) != 6:
            raise ValueError("FEN trong file save không hợp lệ.")

        state = from_fen(fen)

        state.white_timer.time_left = _safe_float(
            data.get("white_time"),
            state.white_timer.time_left
        )

        state.black_timer.time_left = _safe_float(
            data.get("black_time"),
            state.black_timer.time_left
        )

        state.move_history = _safe_list(data.get("move_history"))
        state.captured_white = _safe_list(data.get("captured_white"))
        state.captured_black = _safe_list(data.get("captured_black"))
        state.replay_snapshots = _safe_list(data.get("replay_snapshots"))
        state.replay_index = int(data.get("replay_index", max(0, len(state.replay_snapshots) - 1))) if state.replay_snapshots else 0
        state.replay_mode = False

        if not state.replay_snapshots:
            state.replay_snapshots = [state.snapshot()]

        state.set_message("Đã tải ván đấu")
        last_error = ""
        return state

    except Exception as exc:
        last_error = f"Lỗi khi tải savegame: {exc}"
        print(last_error)
        return None
