from core.config import INCREMENT_SECONDS, AUTO_QUEEN
from utils.helpers import opposite
from utils.sounds import sound_manager
from engine.validator import legal_moves_for_piece, is_in_check, is_checkmate
from engine.special_moves import apply_special_move, update_castling_rights, update_en_passant, is_promotion
from engine.notation import simple_san
from engine.endgame import update_game_status
from engine.replay import record_snapshot


def select_square(state, pos):
    if state.replay_mode:
        return False

    r, c = pos
    piece = state.board[r][c]

    if piece and piece[0] == state.turn:
        state.selected = pos
        state.legal_moves = legal_moves_for_piece(state, pos)
        sound_manager.play("select")
        return True

    state.selected = None
    state.legal_moves.clear()
    return False


def try_move(state, src, dst, promotion=None):
    if state.game_over or state.replay_mode:
        return False

    sr, sc = src
    dr, dc = dst
    piece = state.board[sr][sc]

    if not piece or piece[0] != state.turn:
        return False

    if dst not in legal_moves_for_piece(state, src):
        return False

    if is_promotion(piece, dst) and promotion is None and not AUTO_QUEEN:
        state.promotion_menu = True
        state.promotion_from = src
        state.promotion_square = dst
        state.promotion_color = piece[0]
        return "promotion"

    if is_promotion(piece, dst) and promotion is None:
        promotion = "Q"

    captured_before = state.board[dr][dc]
    captured = apply_special_move(state, src, dst, piece)

    state.board[sr][sc] = ""

    placed_piece = piece[0] + promotion if is_promotion(piece, dst) else piece
    state.board[dr][dc] = placed_piece

    if captured:
        if captured[0] == "w":
            state.captured_white.append(captured)
        else:
            state.captured_black.append(captured)

    castle = piece[1] == "K" and abs(dc - sc) == 2
    was_capture = bool(captured)

    update_castling_rights(state, src, dst, piece, captured_before or captured)
    update_en_passant(state, src, dst, piece)

    state.last_move = (src, dst)
    state.halfmove_clock = 0 if piece[1] == "P" or captured else state.halfmove_clock + 1

    moving_color = state.turn
    next_color = opposite(state.turn)

    if state.turn == "b":
        state.fullmove_number += 1

    if state.turn == "w":
        state.white_timer.add_increment(INCREMENT_SECONDS)
    else:
        state.black_timer.add_increment(INCREMENT_SECONDS)

    # Kiểm tra check/mate sau nước đi để ghi SAN tốt hơn.
    check = is_in_check(state.board, next_color, state)
    mate = is_checkmate(state, next_color) if check else False

    move_record = {
        "piece": piece,
        "from": src,
        "to": dst,
        "captured": captured,
        "promotion": promotion,
        "castle": castle,
        "san": simple_san(piece, src, dst, captured, promotion, castle, check, mate),
    }

    state.move_history.append(move_record)

    state.turn = next_color
    state.selected = None
    state.legal_moves.clear()
    state.promotion_menu = False

    update_game_status(state)

    if state.game_over:
        sound_manager.play("game_over")
    elif check:
        sound_manager.play("check")
    elif castle:
        sound_manager.play("castle")
    elif was_capture:
        sound_manager.play("capture")
    else:
        sound_manager.play("move")

    record_snapshot(state)

    return True


def promote(state, choice):
    if not state.promotion_menu:
        return False

    src = state.promotion_from
    dst = state.promotion_square

    state.promotion_menu = False
    state.promotion_from = None
    state.promotion_square = None

    return try_move(state, src, dst, choice)
