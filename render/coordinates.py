import pygame

from core.constants import screen
from core.config import SQ, THEMES
from core.fonts import get_font

import core.game_state as gs


def draw_coordinates():
    theme = THEMES[gs.state.theme_name]
    font = get_font(16)

    files = "abcdefgh"

    for i in range(8):
        text = font.render(
            files[i],
            True,
            theme["text"]
        )

        screen.blit(
            text,
            (i * SQ + 5, 8 * SQ - 20)
        )

        text2 = font.render(
            str(8 - i),
            True,
            theme["text"]
        )

        screen.blit(
            text2,
            (5, i * SQ + 5)
        )
