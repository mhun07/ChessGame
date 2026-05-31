from dataclasses import dataclass, field
from enum import Enum
from copy import deepcopy

from core.config import DEFAULT_TIME_SECONDS
from core.timer import ChessTimer


class GameStatus(Enum):
    PLAYING = "playing"
    CHECK = "check"
    CHECKMATE = "checkmate"
    STALEMATE = "stalemate"
    TIMEOUT = "timeout"
    DRAW = "draw"


START_BOARD = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP"] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["wP"] * 8,
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
]


@dataclass
class GameState:
    board: list = field(default_factory=lambda: deepcopy(START_BOARD))
    turn: str = "w"

    selected: tuple | None = None
    legal_moves: list = field(default_factory=list)
    last_move: tuple | None = None

    move_history: list = field(default_factory=list)
    piece_images: dict = field(default_factory=dict)

    status: GameStatus = GameStatus.PLAYING
    game_over: bool = False
    winner_text: str = ""

    en_passant: tuple | None = None
    castling_rights: dict = field(default_factory=lambda: {
        "w": {"K": True, "Q": True},
        "b": {"K": True, "Q": True},
    })

    halfmove_clock: int = 0
    fullmove_number: int = 1
    move_scroll: int = 0

    promotion_menu: bool = False
    promotion_square: tuple | None = None
    promotion_from: tuple | None = None
    promotion_color: str | None = None
    promotion_choices: list = field(default_factory=lambda: ["Q", "R", "B", "N"])

    captured_white: list = field(default_factory=list)
    captured_black: list = field(default_factory=list)

    white_timer: ChessTimer = field(default_factory=lambda: ChessTimer(DEFAULT_TIME_SECONDS))
    black_timer: ChessTimer = field(default_factory=lambda: ChessTimer(DEFAULT_TIME_SECONDS))

    theme_name: str = "classic"

    ui_message: str = ""
    ui_message_timer: float = 0.0

    replay_mode: bool = False
    replay_index: int = 0
    replay_snapshots: list = field(default_factory=list)

    time_control_seconds: int = DEFAULT_TIME_SECONDS

    def snapshot(self):
        return {
            "board": deepcopy(self.board),
            "turn": self.turn,
            "selected": self.selected,
            "legal_moves": deepcopy(self.legal_moves),
            "last_move": self.last_move,
            "move_history": deepcopy(self.move_history),
            "status": self.status.value,
            "game_over": self.game_over,
            "winner_text": self.winner_text,
            "en_passant": self.en_passant,
            "castling_rights": deepcopy(self.castling_rights),
            "halfmove_clock": self.halfmove_clock,
            "fullmove_number": self.fullmove_number,
            "captured_white": deepcopy(self.captured_white),
            "captured_black": deepcopy(self.captured_black),
            "white_time": self.white_timer.time_left,
            "black_time": self.black_timer.time_left,
        }

    def restore_snapshot(self, data):
        self.board = deepcopy(data["board"])
        self.turn = data["turn"]
        self.selected = data.get("selected")
        self.legal_moves = deepcopy(data.get("legal_moves", []))
        self.last_move = data.get("last_move")
        self.move_history = deepcopy(data.get("move_history", []))

        status_value = data.get("status", GameStatus.PLAYING.value)
        self.status = GameStatus(status_value)

        self.game_over = data.get("game_over", False)
        self.winner_text = data.get("winner_text", "")
        self.en_passant = data.get("en_passant")

        self.castling_rights = deepcopy(
            data.get(
                "castling_rights",
                {
                    "w": {"K": True, "Q": True},
                    "b": {"K": True, "Q": True},
                },
            )
        )

        self.halfmove_clock = data.get("halfmove_clock", 0)
        self.fullmove_number = data.get("fullmove_number", 1)
        self.captured_white = deepcopy(data.get("captured_white", []))
        self.captured_black = deepcopy(data.get("captured_black", []))

        self.white_timer.time_left = data.get(
            "white_time",
            self.white_timer.time_left
        )

        self.black_timer.time_left = data.get(
            "black_time",
            self.black_timer.time_left
        )

    def set_message(self, text, seconds=3.0):
        self.ui_message = text
        self.ui_message_timer = float(seconds)

    def clear_selection(self):
        self.selected = None
        self.legal_moves.clear()

    def reset(self):
        self.board = deepcopy(START_BOARD)
        self.turn = "w"

        self.clear_selection()

        self.last_move = None
        self.move_history.clear()

        self.status = GameStatus.PLAYING
        self.game_over = False
        self.winner_text = ""

        self.en_passant = None

        self.castling_rights = {
            "w": {"K": True, "Q": True},
            "b": {"K": True, "Q": True},
        }

        self.halfmove_clock = 0
        self.fullmove_number = 1
        self.move_scroll = 0

        self.promotion_menu = False
        self.promotion_square = None
        self.promotion_from = None
        self.promotion_color = None

        self.captured_white.clear()
        self.captured_black.clear()

        self.white_timer.reset(self.time_control_seconds)
        self.black_timer.reset(self.time_control_seconds)

        self.replay_mode = False
        self.replay_index = 0
        self.replay_snapshots = []

        self.ui_message = ""
        self.ui_message_timer = 0.0

        self.replay_snapshots = [self.snapshot()]


state = GameState()


def __getattr__(name):
    if hasattr(state, name):
        return getattr(state, name)

    raise AttributeError(name)