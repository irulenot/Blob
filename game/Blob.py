import pygame

import Constants
import Initalization
from states.menu.MenuState import runMenuState
from states.play.PlayState import runPlayState
from states.watch.WatchState import runWatchState

""" MAIN LOOP """
screen, current_state = Initalization.loadEnvironment()

done = False
while (done == False):

    if (current_state == Constants.MENU_STATE):
        current_state = runMenuState(screen)

    if (current_state == Constants.PLAY_STATE):
        current_state = runPlayState(screen)

    if (current_state == Constants.WATCH_STATE):
        current_state = runWatchState(screen)

    if (current_state == Constants.QUIT_STATE):
        done = True

pygame.quit()
