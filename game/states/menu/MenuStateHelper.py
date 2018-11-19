import Constants
import pygame
from game.states.menu.Button import Button


# Creates button asset and assigns it to a group
def loadAssets():
    button = Button(Constants.BUTTON_WIDTH, Constants.BUTTON_HEIGHT,
                    Constants.BUTTON_X_START, Constants.BUTTON_Y_START)
    asset_group = pygame.sprite.Group()
    asset_group.add(button)
    return asset_group


# Starts music loop and initalizes clock
def createLoopUtilities():
    pygame.mixer.music.load(Constants.MENU_MUSIC_PATH)
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    return clock


# Listens for pygame events, such as exit and clicking on button
def handleEvents(event, done, out_state):
    if (event.type == pygame.QUIT):
        done = True

    if (event.type == Constants.CLICK_PLAY):
        done = True
        out_state = Constants.PLAY_STATE

    return done, out_state


# Draws everything on screen such a background, assets, and words. In 60fps
def render(screen, clock, asset_group):
    screen.fill(Constants.BLUE)

    asset_group.draw(screen)

    font = pygame.font.SysFont('Arial', 29)
    screen.blit(font.render('PLAY', True, Constants.RED), (Constants.BUTTON_X_START, Constants.BUTTON_Y_START))

    clock.tick(60)
    pygame.display.flip()