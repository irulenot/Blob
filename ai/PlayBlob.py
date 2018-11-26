import pygame
import Constants

def sendAction(event):
    if (event.type == Constants.GENERATE_PILLAR):
        return { 'event':pygame.KEYDOWN, 'key':pygame.K_UP }
    return None