# Global constants

import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 1334
SCREEN_HEIGHT = 750

# Pillar dimensions
PILLAR_WIDTH = 50
PILLAR_HEIGHT = 100
PILLAR_X_START = 700
PILLAR_Y_START = SCREEN_HEIGHT - PILLAR_HEIGHT

# File paths
MUSIC_PATH = '../resources/Platformer2.mp3'

# States
PLAY_STATE = "PLAY"
MENU_STATE = "MENU"
WATCH_STATE = "WATCH"

# Events
MUSIC_STOPPED = pygame.constants.USEREVENT
HIT_PILLAR = pygame.constants.USEREVENT+1