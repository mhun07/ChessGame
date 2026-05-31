class MoveAnimation:

    #File này được giữ lại để tránh lỗi import cũ

    def __init__(self):
        self.active = False

    def start(self, *args, **kwargs):
        self.active = False

    def update(self, dt):
        self.active = False

    def draw(self, screen):
        return None


move_animation = MoveAnimation()


def start_animation(*args, **kwargs):
    move_animation.start(*args, **kwargs)


def update_animation(dt):
    move_animation.update(dt)


def draw_animation(screen):
    move_animation.draw(screen)
