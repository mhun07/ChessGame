import pygame
from core.fonts import get_font

class Button:
    def __init__(self, rect, text, callback=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback

    def draw(self, screen, bg=(55, 60, 70), fg=(255, 255, 255)):
        pygame.draw.rect(screen, bg, self.rect, border_radius=10)
        font = get_font(18)
        surf = font.render(self.text, True, fg)
        screen.blit(surf, surf.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False
