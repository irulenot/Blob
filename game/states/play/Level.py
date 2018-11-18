import pygame
import Constants


class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            pillars collide with the player. """
        self.pillar_list = pygame.sprite.Group()
        self.player = player

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000

    # Update pillars on level
    def update(self):
        self.pillar_list.update()


    # Draws background and pillars
    def draw(self, screen):
        screen.fill(Constants.BLUE)
        self.pillar_list.draw(screen)


    # Shifts pillars when player moves left or right
    def shift_world(self, shift_x):
        # Keep track of the shift amount
        self.world_shift += shift_x

        for pillars in self.pillar_list:
            pillars.rect.x += shift_x