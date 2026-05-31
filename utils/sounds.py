import math
from pathlib import Path

import pygame

from core.config import ASSETS_DIR


class SoundManager:
    def __init__(self):
        self.enabled = True
        self.volume = 0.65
        self.sounds = {}

    def load(self):
        """Load all sound effects. Missing files are ignored so the game still runs."""
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
        except pygame.error:
            self.enabled = False
            return

        sound_dir = Path(ASSETS_DIR) / "sounds"

        sound_files = {
            "select": "select.wav",
            "move": "move.wav",
            "capture": "capture.wav",
            "castle": "castle.wav",
            "check": "check.wav",
            "game_over": "game_over.wav",
            "menu": "menu.wav",
        }

        for name, filename in sound_files.items():
            path = sound_dir / filename

            if not path.exists():
                continue

            try:
                sound = pygame.mixer.Sound(str(path))
                sound.set_volume(self.volume)
                self.sounds[name] = sound
            except pygame.error:
                continue

    def play(self, name):
        if not self.enabled:
            return

        sound = self.sounds.get(name)

        if sound:
            sound.play()

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, float(volume)))

        for sound in self.sounds.values():
            sound.set_volume(self.volume)

    def toggle(self):
        self.enabled = not self.enabled
        return self.enabled


sound_manager = SoundManager()
