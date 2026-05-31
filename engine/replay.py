def record_initial_snapshot(state):
    state.replay_snapshots = [state.snapshot()]
    state.replay_index = 0
    state.replay_mode = False


def record_snapshot(state):
    if not state.replay_snapshots:
        state.replay_snapshots = [state.snapshot()]
        state.replay_index = 0
        return

    # Nếu đang replay rồi đi tiếp thì cắt nhánh phía sau.
    state.replay_snapshots = state.replay_snapshots[:state.replay_index + 1]
    state.replay_snapshots.append(state.snapshot())
    state.replay_index = len(state.replay_snapshots) - 1


def start_replay(state):
    if not state.replay_snapshots:
        state.set_message("Chưa có dữ liệu replay")
        return False

    state.replay_mode = True
    state.replay_index = 0
    state.restore_snapshot(state.replay_snapshots[0])
    state.set_message("Đang xem lại ván đấu")
    return True


def replay_next(state):
    if not state.replay_snapshots:
        return False

    state.replay_mode = True
    state.replay_index = min(state.replay_index + 1, len(state.replay_snapshots) - 1)
    state.restore_snapshot(state.replay_snapshots[state.replay_index])
    return True


def replay_prev(state):
    if not state.replay_snapshots:
        return False

    state.replay_mode = True
    state.replay_index = max(state.replay_index - 1, 0)
    state.restore_snapshot(state.replay_snapshots[state.replay_index])
    return True


def stop_replay(state):
    if not state.replay_snapshots:
        return False

    state.restore_snapshot(state.replay_snapshots[-1])
    state.replay_index = len(state.replay_snapshots) - 1
    state.replay_mode = False
    state.set_message("Đã thoát replay")
    return True
