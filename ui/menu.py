import pygame

from core.constants import screen
from core.config import WIDTH, HEIGHT, THEMES
from core.fonts import get_font


def run_menu():
    theme = THEMES["classic"]
    font = get_font(42)

    waiting = True

    while waiting:
        screen.fill(theme["background"])

        text = font.render(
            "Nhấn SPACE để bắt đầu",
            True,
            theme["text"]
        )

        rect = text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(text, rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
