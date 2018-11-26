import pygame

import Constants


class Level(object):

    def __init__(self, player):
        self.pillar_list = pygame.sprite.Group()
        self.player = player

        # How far the player can move left/right
        self.level_limit = -500

    # Update pillars on level
    def update(self):
        self.pillar_list.update()

    # Draws background and pillars
    def draw(self, screen):
        screen.fill(Constants.BLUE)
        self.pillar_list.draw(screen)
