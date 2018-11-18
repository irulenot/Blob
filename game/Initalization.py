import pygame
import Constants

def loadEnvironment():
    pygame.init()
    pygame.display.set_caption("Blob")

    size = [Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    return screen