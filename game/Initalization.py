import pygame

import Constants


# Loads window and specifies title and size
def loadEnvironment():
    pygame.init()
    pygame.display.set_caption("Blob")

    size = [Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    current_state = Constants.MENU_STATE
    return screen, current_state
