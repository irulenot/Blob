import pygame
import Constants


# Loads window and specifies title and size
def loadEnvironment():
    pygame.init()
    pygame.display.set_caption("Blob")

    w,h = pygame.display.Info().current_w, pygame.display.Info().current_h
    if (w == 1920 and h == 1080):
        size = [Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)
    else:
        # Fullscreen if not on my monitor as fixes bug for select retina displays.
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)


    current_state = Constants.MENU_STATE
    return screen, current_state
