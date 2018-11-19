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

# Pillar properties
PILLAR_WIDTH = 50
PILLAR_HEIGHT = 100
PILLAR_X_START = SCREEN_WIDTH
PILLAR_Y_START = SCREEN_HEIGHT - PILLAR_HEIGHT
GENERATE_PILLAR_FREQUENCY = 2 * 1000                # 1 Pillar every 2 seconds

# Button properties
BUTTON_WIDTH = PILLAR_WIDTH
BUTTON_HEIGHT = PILLAR_HEIGHT
BUTTON_X_START = SCREEN_WIDTH/2 - PILLAR_WIDTH/2
BUTTON_Y_START = SCREEN_HEIGHT/2 - PILLAR_HEIGHT/2


# File paths
PLAY_MUSIC_PATH = '../resources/Platformer2.mp3'
MENU_MUSIC_PATH = '../resources/bensound-thelounge.mp3'


# States
PLAY_STATE = "PLAY"
MENU_STATE = "MENU"
WATCH_STATE = "WATCH"

# Events
MUSIC_STOPPED = pygame.constants.USEREVENT
HIT_PILLAR = pygame.constants.USEREVENT+1
GENERATE_PILLAR = pygame.constants.USEREVENT+2

# Licenses
# Music: https://www.bensound.com