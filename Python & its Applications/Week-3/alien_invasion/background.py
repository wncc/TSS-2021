import pygame
class Background():
    def __init__(self, ai_settings, screen):
        self.screen = screen

        self.bg_img = pygame.image.load('images/bg.jpg')
        