import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__() # connect Sprite and Bullet (Python 3 syntax is used)
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        ai_settings.bullet_height) # create rect at (0,0) with dimensions from ai_settings
        # set the bullets's position according to the ship's position
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the colour of the bullet
        self.color = ai_settings.bullet_color

    def update(self):
        """Move the bullet up the screen."""
        self.rect.y -= 3 #Remeber how the coordinates here work

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)