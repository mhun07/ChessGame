import pygame
from core.config import SIDEBAR_X, SIDEBAR_WIDTH, HEIGHT, THEMES
from core.fonts import get_font


def draw_sidebar(screen, state, theme_name="classic"):
    theme = THEMES[theme_name]

    panel = pygame.Rect(SIDEBAR_X, 50, SIDEBAR_WIDTH, HEIGHT - 100)
    pygame.draw.rect(screen, theme["panel"], panel, border_radius=16)

    title_font = get_font(25)
    font = get_font(20)
    small = get_font(16, bold=False)
    result_font = get_font(18)

    screen.blit(
        title_font.render("Chess game của Minh Hưng !", True, theme["text"]),
        (SIDEBAR_X + 20, 70)
    )

    turn = "Trắng" if state.turn == "w" else "Đen"

    screen.blit(
        font.render(f"Lượt: {turn}", True, theme["text"]),
        (SIDEBAR_X + 20, 125)
    )

    screen.blit(
        font.render(f"Trắng: {state.white_timer.text()}", True, theme["text"]),
        (SIDEBAR_X + 20, 170)
    )

    screen.blit(
        font.render(f"Đen: {state.black_timer.text()}", True, theme["text"]),
        (SIDEBAR_X + 20, 205)
    )

    if state.replay_mode:
        replay_text = f"Replay: {state.replay_index}/{max(0, len(state.replay_snapshots) - 1)}"
        screen.blit(
            small.render(replay_text, True, theme["warning"]),
            (SIDEBAR_X + 20, 235)
        )

    draw_move_table(
        screen,
        state,
        SIDEBAR_X + 20,
        260,
        theme,
        max_rows=12
    )

    if state.ui_message:
        msg_box = pygame.Rect(
            SIDEBAR_X + 15,
            HEIGHT - 230,
            SIDEBAR_WIDTH - 30,
            55
        )

        pygame.draw.rect(screen, theme["panel_light"], msg_box, border_radius=12)

        screen.blit(
            small.render(state.ui_message, True, theme["warning"]),
            (SIDEBAR_X + 28, HEIGHT - 212)
        )

    if state.game_over:
        box = pygame.Rect(
            SIDEBAR_X + 15,
            HEIGHT - 145,
            SIDEBAR_WIDTH - 30,
            80
        )

        pygame.draw.rect(
            screen,
            theme["danger"],
            box,
            border_radius=14
        )

        screen.blit(
            result_font.render(state.winner_text, True, (255, 255, 255)),
            (SIDEBAR_X + 30, HEIGHT - 115)
        )


def draw_move_table(screen, state, x, y, theme, max_rows=12):
    title_font = get_font(20)
    font = get_font(17, bold=False)

    screen.blit(
        title_font.render("Nước đi", True, theme["text"]),
        (x, y)
    )

    y += 35

    screen.blit(font.render("#", True, theme["warning"]), (x, y))
    screen.blit(font.render("Trắng", True, theme["text"]), (x + 50, y))
    screen.blit(font.render("Đen", True, theme["text"]), (x + 175, y))

    y += 30

    rows = []

    for i in range(0, len(state.move_history), 2):
        white = state.move_history[i].get("san", "")
        black = state.move_history[i + 1].get("san", "") if i + 1 < len(state.move_history) else ""
        rows.append((i // 2 + 1, white, black))

    total = len(rows)
    max_scroll = max(0, total - max_rows)

    state.move_scroll = max(0, min(state.move_scroll, max_scroll))

    visible_rows = rows[state.move_scroll:state.move_scroll + max_rows]
    table_start_y = y
    row_height = 25

    for row_num, white_move, black_move in visible_rows:
        screen.blit(font.render(str(row_num), True, theme["muted"]), (x, y))
        screen.blit(font.render(white_move, True, theme["text"]), (x + 50, y))
        screen.blit(font.render(black_move, True, theme["text"]), (x + 175, y))
        y += row_height

    if total > max_rows:
        bar_x = x + 315
        bar_y = table_start_y
        bar_h = max_rows * row_height

        pygame.draw.rect(
            screen,
            theme["panel_light"],
            (bar_x, bar_y, 6, bar_h),
            border_radius=3
        )

        thumb_h = max(28, int(bar_h * max_rows / total))
        thumb_y = bar_y + int((bar_h - thumb_h) * state.move_scroll / max_scroll) if max_scroll else bar_y

        pygame.draw.rect(
            screen,
            theme["accent"],
            (bar_x, thumb_y, 6, thumb_h),
            border_radius=3
        )
