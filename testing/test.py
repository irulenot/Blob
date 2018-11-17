# import pygame
import pygame
import Constants


# initialize game engine
pygame.init()

window_width= Constants.SCREEN_WIDTH
window_height=Constants.SCREEN_HEIGHT

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Hello World")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("../resources/Game_Background_175.png").convert()
background_image = pygame.transform.scale(background_image, Constants.SCREEN_DIMENSIONS)

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)