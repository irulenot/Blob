import pygame
import Initalization
import Constants

from states.play.PlayState import runPlayState
from states.menu.MenuState import runMenuState


""" MAIN LOOP """
screen, current_state = Initalization.loadEnvironment()

done = False
while (done == False):

    if (current_state == Constants.MENU_STATE):
        current_state = runMenuState(screen)

    if (current_state == Constants.PLAY_STATE):
        current_state = runPlayState(screen)

    done = True

pygame.quit()
