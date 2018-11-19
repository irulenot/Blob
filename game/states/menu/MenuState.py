from game.states.menu.MenuStateHelper import *
import pygame
import Constants

def runMenuState(screen):

    asset_group = loadAssets()
    clock = createLoopUtilities()

    # Menu State Main Loop
    done = False
    while (done == False):
        for event in pygame.event.get():
            done = handleEvents(event, done)

        render(screen, clock, asset_group)

    return Constants.MENU_STATE