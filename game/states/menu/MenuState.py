from states.menu.MenuStateHelper import *
import pygame
import Constants

def runMenuState(screen):

    asset_group = loadAssets()
    clock = createLoopUtilities()

    # Menu State Main Loop
    out_state = Constants.QUIT_STATE
    done = False
    while (done == False):
        for event in pygame.event.get():
            done, out_state = handleEvents(event, done, out_state)

        asset_group.update()
        render(screen, clock, asset_group)

    return out_state