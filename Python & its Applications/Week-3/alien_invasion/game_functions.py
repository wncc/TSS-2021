import sys
import pygame
from alien import Alien
from time import sleep
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
  """Respond to keypresses and mouse events."""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event,ai_settings, screen, ship, bullets) 

    elif event.type == pygame.KEYUP:
      check_keyup_events(event,ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
  """respond to keypresses"""
  if event.key == pygame.K_RIGHT:  
    ship.moving_right = True 
  elif event.key == pygame.K_LEFT:  
    ship.moving_left = True

  elif event.key == pygame.K_SPACE:
    fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
  """ respond to key releases"""
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):
  """Fire a bullet if limit not reached yet."""
  # Create a new bullet and add it to the bullets group.
  if len(bullets) < ai_settings.bullets_allowed:
      new_bullet = Bullet(ai_settings, screen, ship)
      bullets.add(new_bullet)
  

def update_bullets(ai_settings, screen, ship, aliens, bullets):
  """Update position of bullets and get rid of old bullets."""
  # Update bullet positions.
  bullets.update()
  # Get rid of bullets that have disappeared.
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)

  check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
  """Respond to bullet-alien collisions."""
  # Remove any bullets and aliens that have collided.
  collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

  if len(aliens) == 0:
    # Destroy existing bullets and create new fleet.
    bullets.empty()
    create_fleet(ai_settings, screen, aliens, ship)

def check_fleet_edges(ai_settings, aliens):
  """Respond appropriately if any aliens have reached an edge."""
  for alien in aliens.sprites():
    #iterate through all the aliens and check if any have reached the edge
    if alien.check_edges():
      change_fleet_direction(ai_settings, aliens)
      break

def change_fleet_direction(ai_settings, aliens):
  """Drop the entire fleet and change the fleet's direction."""
  for alien in aliens.sprites():
    alien.rect.y += 10 # make the aliens move down
  ai_settings.fleet_direction *= -1 # change the direction of movement

def check_aliens_bottom(screen,aliens):
  """Check if any aliens have reached the bottom of the screen."""
  screen_rect = screen.get_rect()
  for alien in aliens.sprites():
    if alien.rect.bottom >= screen_rect.bottom:
      return True

def get_number_aliens_x(ai_settings, alien_width):	
  """Determine the number of aliens that fit in a row."""
  available_space_x = ai_settings.screen_width - 2 * alien_width
  number_aliens_x = int(available_space_x / (2 * alien_width))
  return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):	
  """Determine the number of rows of aliens that fit on the screen."""

  available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
  number_rows = int(available_space_y / (2 * alien_height))
  return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
  """Create an alien and place it in the row."""
  alien = Alien(ai_settings, screen)
  alien_width = alien.rect.width
  alien.rect.x = alien_width + 2 * alien_width * alien_number
  alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
  aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
  """Create a full fleet of aliens."""
  # Create an alien and find the number of aliens in a row.
  alien = Alien(ai_settings, screen) #Create an alien object just for calculations
  number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
  number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

  # Create the fleet of aliens.
  for row_number in range(number_rows):
    for alien_number in range(number_aliens_x):
      create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_aliens(ai_settings, screen, aliens, ship):
  """
  Check if the fleet is at an edge,
  and then update the postions of all aliens in the fleet.
  """
  check_fleet_edges(ai_settings, aliens)
  aliens.update()
  # Look for alien-ship collisions.
  if pygame.sprite.spritecollideany(ship, aliens) or check_aliens_bottom(screen,aliens):
    game_over(ai_settings, screen)

def game_over(ai_settings, screen):
  gameover_img = pygame.font.SysFont(None, 48).render("GAME OVER", True, (240,240,240))
  gameover_rect = gameover_img.get_rect()
  gameover_rect.centerx = ai_settings.screen_width/2
  gameover_rect.top = 20
  screen.blit(gameover_img, gameover_rect)

  pygame.display.update()

  sleep(3)
  sys.exit(0)

def update_screen(bg_img, screen, ship, aliens, bullets):
  """Update images on the screen and flip to the new screen."""
  # Redraw the screen during each pass through the loop.
  screen.blit(bg_img,(0,0))

  # Redraw all bullets behind the ship.
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  aliens.draw(screen)
  ship.blitme()

  # Make the most recently drawn screen visible.
  pygame.display.flip()
