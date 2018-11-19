import pygame

import Constants

class Button(pygame.sprite.Sprite):
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    def __init__(self, width, height, x_position, y_position, action):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Constants.GREEN)
        self.rect = self.image.get_rect()

        self.action = action
        self.rect.x = x_position
        self.rect.y = y_position


    def update(self):
        pygame.mouse.get_pressed()
        if (pygame.mouse.get_pressed()[0] == True) and (self.rect.collidepoint(pygame.mouse.get_pos())):
            click_event = pygame.event.Event(self.action)
            pygame.event.post(click_event)