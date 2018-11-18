import pygame

import Constants

class Pillar(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    player = None
    level = None

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Constants.GREEN)
        self.rect = self.image.get_rect()


    # Continually updates pillar movement, and logic
    def update(self):

        # Move left/right up/down
        self.rect.x -= self.change_x
        self.rect.y += self.change_y
        cur_pos = self.rect.x - self.level.world_shift

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if (hit == True):
            return True # TODO: We want this to stop the play state

        # Deletes blocks after they leave window
        if cur_pos <= -Constants.BLOCK_WIDTH:
            self.kill()
