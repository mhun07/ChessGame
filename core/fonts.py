import pygame

_font_cache = {}


def get_font(size, bold=True, font_path=None):
    key = (font_path, size, bold)

    if key in _font_cache:
        return _font_cache[key]

    if font_path:
        font = pygame.font.Font(font_path, size)
        font.set_bold(bold)
    else:
        preferred_fonts = ["Segoe UI", "Tahoma", "Verdana", "Arial"]
        font = None

        for name in preferred_fonts:
            try:
                font = pygame.font.SysFont(name, size, bold=bold)
                if font:
                    break
            except Exception:
                continue

        if font is None:
            font = pygame.font.Font(None, size)

    _font_cache[key] = font
    return font
