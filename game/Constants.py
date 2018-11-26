# Global constants

import pygame
import re

from pathlib import Path


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
game_path = str(Path().absolute())
game_directory = game_path.split("Blob",1)[0]

PLAY_MUSIC_PATH = game_directory + 'Blob/resources/Platformer2.mp3'
MENU_MUSIC_PATH = game_directory + 'Blob/resources/bensound-thelounge.mp3'
WATCH_MUSIC_PATH = game_directory + 'Blob/resources/bensound-allthat.mp3'

PILLAR_LOG_PATH = game_directory + 'Blob/data/play_data/pillar-log.txt'
PILLAR_DATA_PATH = game_directory + 'Blob/data/play_data/pillar-data.txt'
EVENT_LOG_PATH = game_directory + 'Blob/data/play_data/event-log.txt'
EVENT_DATA_PATH = game_directory + 'Blob/data/play_data/event-data.txt'


# States
PLAY_STATE = "PLAY"
MENU_STATE = "MENU"
WATCH_STATE = "WATCH"
QUIT_STATE = "QUIT"


# Events
HIT_PILLAR = pygame.constants.USEREVENT+1
GENERATE_PILLAR = pygame.constants.USEREVENT+2
CLICK_PLAY = pygame.constants.USEREVENT+3
CLICK_WATCH = pygame.constants.USEREVENT+4

# Licenses
# Music: bensound-thelounge.mp3: https://www.bensound.com