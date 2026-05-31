from core.config import THEMES
from render.board_renderer import draw_board
from render.highlight import draw_highlights
from render.piece_renderer import draw_pieces
from render.ui_renderer import draw_sidebar

def draw_game(screen, state):
    theme = THEMES[state.theme_name]
    screen.fill(theme["background"])
    draw_board(screen, state.theme_name)
    draw_highlights(screen, state, state.theme_name)
    draw_pieces(screen, state)
    draw_sidebar(screen, state, state.theme_name)
