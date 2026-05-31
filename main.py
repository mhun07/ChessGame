import pygame

from core.constants import screen, clock
from core.config import FPS, THEMES
import core.game_state as gs

from utils.loaders import load_piece_images
from utils.helpers import screen_to_square
from utils.sounds import sound_manager

from render.draw import draw_game
from ui.promotion import draw_promotion_menu, handle_promotion_click
from ui.settings import run_time_settings

from engine.logic import select_square, try_move, promote
from engine.endgame import update_timer_status
from engine.save_load import save_game, load_game, last_error
from engine.pgn import save_pgn
from engine.replay import record_initial_snapshot, start_replay, replay_next, replay_prev, stop_replay


MAX_MOVE_ROWS = 12


def handle_board_click(state, mouse_pos):
    if state.replay_mode:
        state.set_message("Thoát replay để tiếp tục chơi")
        return

    sq = screen_to_square(*mouse_pos)

    if not sq:
        state.clear_selection()
        return

    r, c = sq
    piece = state.board[r][c]

    if piece and piece[0] == state.turn:
        select_square(state, sq)
        return

    if state.selected:
        result = try_move(state, state.selected, sq)

        if result != "promotion":
            state.clear_selection()


def main():
    sound_manager.load()
    time_seconds = run_time_settings()

    state = gs.state
    state.time_control_seconds = time_seconds
    state.white_timer.reset(time_seconds)
    state.black_timer.reset(time_seconds)
    state.piece_images = load_piece_images()
    record_initial_snapshot(state)

    theme_names = list(THEMES.keys())
    theme_index = theme_names.index(state.theme_name) if state.theme_name in theme_names else 0

    running = True

    while running:
        dt = clock.tick(FPS)

        if state.ui_message_timer > 0:
            state.ui_message_timer -= dt / 1000.0

            if state.ui_message_timer <= 0:
                state.ui_message = ""

        if not state.game_over and not state.promotion_menu and not state.replay_mode:
            state.white_timer.update(dt, state.turn == "w")
            state.black_timer.update(dt, state.turn == "b")
            update_timer_status(state)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    sound_manager.play("menu")
                    state.reset()
                    state.piece_images = load_piece_images()
                    record_initial_snapshot(state)

                elif event.key == pygame.K_s:
                    sound_manager.play("menu")
                    save_game(state)

                elif event.key == pygame.K_l:
                    sound_manager.play("menu")
                    loaded = load_game()

                    if loaded is not None:
                        loaded.piece_images = load_piece_images()
                        gs.state = loaded
                        state = gs.state

                    else:
                        state.set_message(last_error or "Không tải được ván đấu")

                elif event.key == pygame.K_p:
                    sound_manager.play("menu")
                    path = save_pgn(state)
                    state.set_message(f"Đã xuất PGN: {path.name}")

                elif event.key == pygame.K_v:
                    sound_manager.play("menu")
                    start_replay(state)

                elif event.key == pygame.K_RIGHT:
                    replay_next(state)

                elif event.key == pygame.K_LEFT:
                    replay_prev(state)

                elif event.key == pygame.K_END:
                    stop_replay(state)

                elif event.key == pygame.K_t:
                    sound_manager.play("menu")
                    theme_index = (theme_index + 1) % len(theme_names)
                    state.theme_name = theme_names[theme_index]

                elif event.key == pygame.K_ESCAPE:
                    if state.replay_mode:
                        stop_replay(state)
                    else:
                        state.clear_selection()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state.promotion_menu:
                    choice = handle_promotion_click(state, event.pos)

                    if choice:
                        sound_manager.play("menu")
                        promote(state, choice)
                        state.clear_selection()

                    continue

                handle_board_click(state, event.pos)

            elif event.type == pygame.MOUSEWHEEL:
                total_rows = (len(state.move_history) + 1) // 2
                max_scroll = max(0, total_rows - MAX_MOVE_ROWS)

                state.move_scroll -= event.y
                state.move_scroll = max(0, min(state.move_scroll, max_scroll))

        draw_game(screen, state)
        draw_promotion_menu(screen, state)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
