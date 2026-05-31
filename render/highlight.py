import pygame
from core.config import BOARD_X, BOARD_Y, SQ, THEMES
from engine.validator import find_king, is_in_check

def overlay(screen, rect, color):
    surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    surf.fill(color)
    screen.blit(surf, rect.topleft)

def draw_highlights(screen, state, theme_name="classic"):
    theme = THEMES[theme_name]

    if state.last_move:
        for r, c in state.last_move:
            rect = pygame.Rect(BOARD_X + c * SQ, BOARD_Y + r * SQ, SQ, SQ)
            overlay(screen, rect, theme["last_move"])

    if state.selected:
        r, c = state.selected
        pygame.draw.rect(screen, theme["accent"], pygame.Rect(BOARD_X + c * SQ, BOARD_Y + r * SQ, SQ, SQ), 4)

    for r, c in state.legal_moves:
        rect = pygame.Rect(BOARD_X + c * SQ, BOARD_Y + r * SQ, SQ, SQ)
        if state.board[r][c]:
            overlay(screen, rect, theme["capture"])
        else:
            pygame.draw.circle(screen, theme["legal"][:3], rect.center, 11)

    if is_in_check(state.board, state.turn, state):
        king = find_king(state.board, state.turn)
        if king:
            r, c = king
            rect = pygame.Rect(BOARD_X + c * SQ, BOARD_Y + r * SQ, SQ, SQ)
            overlay(screen, rect, theme["check"])
