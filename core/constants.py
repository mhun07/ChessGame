import pygame
from core.config import WIDTH, HEIGHT, APP_NAME

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(APP_NAME)

clock = pygame.time.Clock()
