import re

import pygame

import Constants


# AI's evaluation acted on
def decision():
    action = evaluation()

    if (action == "JUMP"):
        return {'event': pygame.KEYDOWN, 'key': pygame.K_UP}

    return None


# TO BE REPLACED
def evaluation():
    log_file = open(Constants.LOG_PATH, "r")
    log_data = log_file.read()

    log_parse = re.split('rect[(]|, 650, 50', log_data)
    if (len(log_parse) > 1):
        closest_pillar = int(log_parse[1])

        if (closest_pillar > 380) and (closest_pillar < 450):
            return "JUMP"

    return None
