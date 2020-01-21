import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False


def update_screen(ai_settings, screen, ship):
    """Refreshes a screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    """Displaying the last-drawn screen"""
    pygame.display.flip()