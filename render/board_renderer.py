import pygame
from core.config import BOARD_X, BOARD_Y, BOARD_SIZE, SQ, THEMES, SHOW_COORDINATES
from core.fonts import get_font

def draw_board(screen, theme_name="classic"):
    theme = THEMES[theme_name]

    for r in range(8):
        for c in range(8):
            color = theme["light"] if (r + c) % 2 == 0 else theme["dark"]
            rect = pygame.Rect(BOARD_X + c * SQ, BOARD_Y + r * SQ, SQ, SQ)
            pygame.draw.rect(screen, color, rect)

    if SHOW_COORDINATES:
        font = get_font(16)
        for i in range(8):
            file_text = chr(ord("a") + i)
            rank_text = str(8 - i)
            file_surf = font.render(file_text, True, (30, 30, 30))
            rank_surf = font.render(rank_text, True, (30, 30, 30))
            screen.blit(file_surf, (BOARD_X + i * SQ + SQ - 18, BOARD_Y + BOARD_SIZE - 22))
            screen.blit(rank_surf, (BOARD_X + 5, BOARD_Y + i * SQ + 4))
