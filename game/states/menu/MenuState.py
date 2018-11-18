import pygame
import Constants

def runMenuState(screen):

    # Menu State Main Loop
    done = False
    while (done == False):
        for event in pygame.event.get():
            print("Menu events ran")

        done = True

    return Constants.MENU_STATE