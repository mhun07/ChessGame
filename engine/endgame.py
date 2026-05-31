from core.game_state import GameStatus
from utils.sounds import sound_manager
from engine.validator import is_in_check, is_checkmate, is_stalemate


def update_game_status(state):
    color = state.turn

    if is_checkmate(state, color):
        state.status = GameStatus.CHECKMATE
        state.game_over = True
        state.winner_text = "Trắng thắng do chiếu hết !!!" if color == "b" else "Đen thắng do chiếu hết !!!"
        return

    if is_stalemate(state, color):
        state.status = GameStatus.STALEMATE
        state.game_over = True
        state.winner_text = "Hòa do hết nước đi !!!"
        return

    state.status = GameStatus.CHECK if is_in_check(state.board, color, state) else GameStatus.PLAYING


def update_timer_status(state):
    if state.white_timer.time_left <= 0:
        state.status = GameStatus.TIMEOUT
        state.game_over = True
        state.winner_text = "Đen thắng do hết giờ !!!"
        sound_manager.play("game_over")

    elif state.black_timer.time_left <= 0:
        state.status = GameStatus.TIMEOUT
        state.game_over = True
        state.winner_text = "Trắng thắng do hết giờ !!!"
        sound_manager.play("game_over")
