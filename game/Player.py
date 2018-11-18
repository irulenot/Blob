import pygame
import Constants

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(Constants.RED)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0


    # Continually updates movement and gravity on Player
    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x
        self.rect.y += self.change_y


    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= Constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = Constants.SCREEN_HEIGHT - self.rect.height


    def jump(self):
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= Constants.SCREEN_HEIGHT:
            self.change_y = -10


    # Player-controlled movement: left
    def go_left(self):
        self.change_x = -6

    # Player-controlled movement: right
    def go_right(self):
        self.change_x = 6

    # Player-controlled movement: no key pressed.
    def stop(self):
        self.change_x = 0
