import pygame
from core.config import BOARD_X, BOARD_Y, SQ, THEMES

def draw_promotion_menu(screen, state):
    if not state.promotion_menu or not state.promotion_square:
        return

    r, c = state.promotion_square
    color = state.promotion_color
    x = BOARD_X + c * SQ
    y = BOARD_Y + r * SQ

    for i, choice in enumerate(state.promotion_choices):
        rect = pygame.Rect(x, y + i * SQ, SQ, SQ)
        pygame.draw.rect(screen, THEMES[state.theme_name]["panel_light"], rect)

        piece = color + choice
        img = state.piece_images.get(piece)
        if img:
            screen.blit(img, rect.topleft)

def handle_promotion_click(state, pos):
    if not state.promotion_menu or not state.promotion_square:
        return None

    r, c = state.promotion_square
    x0 = BOARD_X + c * SQ
    y0 = BOARD_Y + r * SQ
    mx, my = pos

    if not (x0 <= mx < x0 + SQ):
        return None

    idx = (my - y0) // SQ
    if 0 <= idx < len(state.promotion_choices):
        return state.promotion_choices[idx]

    return None
