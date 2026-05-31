import pygame

from core.constants import screen
from core.config import WIDTH, HEIGHT, THEMES
from core.fonts import get_font


TIME_OPTIONS = [
    ("3 phút", 3 * 60),
    ("5 phút", 5 * 60),
    ("10 phút", 10 * 60),
    ("15 phút", 15 * 60),
    ("30 phút", 30 * 60),
]


def run_time_settings():
    theme = THEMES["classic"]
    title_font = get_font(42)
    font = get_font(28)
    small = get_font(20, bold=False)

    selected = 2
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        screen.fill(theme["background"])

        title = title_font.render("Cài đặt thời gian", True, theme["text"])
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 120)))

        note = small.render("Dùng ↑ ↓ để chọn, ENTER để bắt đầu", True, theme["muted"])
        screen.blit(note, note.get_rect(center=(WIDTH // 2, 170)))

        y = 240

        for i, (label, seconds) in enumerate(TIME_OPTIONS):
            color = theme["warning"] if i == selected else theme["text"]
            prefix = "» " if i == selected else "  "

            line = font.render(prefix + label, True, color)
            screen.blit(line, line.get_rect(center=(WIDTH // 2, y)))
            y += 48

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(TIME_OPTIONS)

                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(TIME_OPTIONS)

                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return TIME_OPTIONS[selected][1]
