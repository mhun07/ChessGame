from pathlib import Path

APP_NAME = "Chess game của Minh Hưng nèee !!!"

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
SAVES_DIR = BASE_DIR / "saves"

WIDTH = 1180
HEIGHT = 820

BOARD_SIZE = 720
SQ = BOARD_SIZE // 8
BOARD_X = 30
BOARD_Y = 50

SIDEBAR_X = BOARD_X + BOARD_SIZE + 30
SIDEBAR_WIDTH = WIDTH - SIDEBAR_X - 30

FPS = 120

DEFAULT_TIME_SECONDS = 10 * 60
INCREMENT_SECONDS = 0
AUTO_QUEEN = False

SHOW_COORDINATES = True
SHOW_LEGAL_MOVES = True
SHOW_LAST_MOVE = True
SHOW_CHECK = True

THEMES = {
    "classic": {
        "light": (240, 217, 181),
        "dark": (181, 136, 99),
        "background": (18, 20, 24),
        "panel": (28, 30, 36),
        "panel_light": (42, 45, 53),
        "text": (240, 240, 240),
        "muted": (150, 150, 150),
        "accent": (80, 140, 255),
        "danger": (255, 85, 85),
        "success": (80, 210, 120),
        "warning": (255, 210, 80),
        "last_move": (245, 230, 90, 120),
        "legal": (60, 160, 255, 120),
        "capture": (255, 80, 80, 120),
        "check": (255, 40, 40, 150),
    },
    "green": {
        "light": (235, 236, 208),
        "dark": (119, 149, 86),
        "background": (16, 19, 16),
        "panel": (27, 34, 27),
        "panel_light": (43, 54, 43),
        "text": (240, 240, 240),
        "muted": (160, 168, 160),
        "accent": (95, 180, 120),
        "danger": (255, 90, 90),
        "success": (90, 220, 130),
        "warning": (255, 215, 90),
        "last_move": (245, 230, 90, 120),
        "legal": (70, 170, 120, 120),
        "capture": (255, 80, 80, 120),
        "check": (255, 40, 40, 150),
    },
    "blue": {
        "light": (222, 235, 247),
        "dark": (88, 132, 170),
        "background": (15, 18, 25),
        "panel": (25, 31, 42),
        "panel_light": (38, 48, 64),
        "text": (240, 245, 255),
        "muted": (155, 165, 180),
        "accent": (80, 155, 255),
        "danger": (255, 85, 85),
        "success": (85, 210, 135),
        "warning": (255, 215, 90),
        "last_move": (245, 230, 90, 120),
        "legal": (80, 155, 255, 120),
        "capture": (255, 80, 80, 120),
        "check": (255, 40, 40, 150),
    },
}

CURRENT_THEME = "classic"
