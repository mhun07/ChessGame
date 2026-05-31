class ChessTimer:
    def __init__(self, seconds=600):
        self.total_time = float(seconds)
        self.time_left = float(seconds)

    @property
    def remaining(self):
        return self.time_left

    @remaining.setter
    def remaining(self, value):
        self.time_left = max(0.0, float(value))

    def update(self, dt_ms, active):

        #dt_ms lấy từ pygame clock.tick(FPS),Luôn tính theo milliseconds

        if not active or self.time_left <= 0:
            return self.time_left <= 0

        delta_seconds = dt_ms / 1000.0
        self.time_left = max(0.0, self.time_left - delta_seconds)

        return self.time_left <= 0

    def add_increment(self, seconds):
        self.time_left += float(seconds)

    def reset(self, seconds=None):
        if seconds is not None:
            self.total_time = float(seconds)

        self.time_left = float(self.total_time)

    def text(self):
        minutes = int(self.time_left // 60)
        seconds = int(self.time_left % 60)

        return f"{minutes:02}:{seconds:02}"

    def get_text(self):
        return self.text()