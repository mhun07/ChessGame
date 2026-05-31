import pygame
from pathlib import Path
from core.config import ASSETS_DIR, SQ

_image_cache = {}

def load_piece_images(size=SQ):
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
    images = {}

    for piece in pieces:
        key = (piece, size)
        if key in _image_cache:
            images[piece] = _image_cache[key]
            continue

        path = Path(ASSETS_DIR) / f"{piece}.png"
        if not path.exists():
            continue

        img = pygame.image.load(str(path)).convert_alpha()
        img = pygame.transform.smoothscale(img, (size, size))
        _image_cache[key] = img
        images[piece] = img

    return images
