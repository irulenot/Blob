import pygame

import Initalization
from PlayState import runPlayState

""" Main Program """
screen = Initalization.loadEnvironment()

# -------- Main Program Loop -----------
runPlayState(screen)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
