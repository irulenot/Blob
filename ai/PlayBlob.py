import pygame
import Constants
import Logger
import re


# AI thinks about what to do in this instance and returns an action
def think_cycle():

    action = evaluation()

    # Clears the log as no longer relevant
    Logger.clearLog()

    if(action == "JUMP"):
        return { 'event':pygame.KEYDOWN, 'key':pygame.K_UP }

    return None


# AI looks at pillars then returns an action
def evaluation():
    log_file = open(Constants.LOG_PATH, "r")
    log_data = log_file.read()

    log_parse = re.split('rect[(]|, 650, 50', log_data)
    if(len(log_parse) > 1):
        closest_pillar = int(log_parse[1])

        if (closest_pillar > 380) and (closest_pillar < 450):
            return "JUMP"

    return None