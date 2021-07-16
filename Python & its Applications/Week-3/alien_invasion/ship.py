import pygame

class Ship():

  def __init__(self, screen):
    """Initialize the ship and set its starting position."""

    self.screen = screen #This refers to the screen object we had created
    
    # Load the ship image and get its rect.
    self.image = pygame.image.load('images/ship.png')
    
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # Start each new ship at the bottom center of the screen.
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    # Movement flag
    self.moving_right = False
    self.moving_left = False

  def update(self):
    """Update the ship's position based on the movement flag."""
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.rect.centerx += 1
    if self.moving_left and self.rect.left > 0:
      self.rect.centerx -= 1

  def blitme(self):
    self.screen.blit(self.image, self.rect)
