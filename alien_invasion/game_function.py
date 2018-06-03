import sys
from bullet import Bullet
import pygame

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """response of keydown"""
    if event.key == pygame.K_RIGHT:
        # move ship to right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move ship to left
        ship.moving_left = True
        # move ship to up
    elif event.key == pygame.K_UP:
        ship.moving_up = True
        # move ship to down
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    """fire bullets"""
    # creat a bullet then join in group
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """response of keyup"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings,screen,ship,bullets):
    """response events of mouse and keyboard"""
    # monitor the keyboard and mouse event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)





def update_screen(ai_settings,screen,ship,bullets):
    """update the pic on screen and rush to new screen"""
    # redraw screen in each circulation.
    screen.fill(ai_settings.bg_color)

    #redraw all bullets behind ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    # rush screen to make the latest drawed to be seen.
    pygame.display.flip()

def update_bullets(bullets):
    """update location of bullets,then delete the bullet gone"""
    #update location of bullets
    bullets.update()

    # delete bullets that gone
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
