import pygame

import Constants

class Button(pygame.sprite.Sprite):
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    def __init__(self, width, height, x_position, y_position):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Constants.GREEN)
        self.rect = self.image.get_rect()

        self.rect.x = x_position
        self.rect.y = y_position


    def update(self):
        print(click = pygame.mouse.get_pressed())