import Constants
import pygame
from game.states.menu.Button import Button


def loadAssets():
    button = Button(Constants.BUTTON_WIDTH, Constants.BUTTON_HEIGHT,
                    Constants.BUTTON_X_START, Constants.BUTTON_Y_START)
    asset_group = pygame.sprite.Group()
    asset_group.add(button)
    return asset_group


def createLoopUtilities():
    playMusic(True)
    clock = pygame.time.Clock()
    pygame.time.set_timer(Constants.GENERATE_PILLAR, Constants.GENERATE_PILLAR_FREQUENCY)
    return clock


def playMusic(firstTimePlaying):
    pygame.mixer.music.load(Constants.MENU_MUSIC_PATH)
    if (firstTimePlaying == False):
        pygame.mixer.music.set_endevent(Constants.MUSIC_STOPPED)
    pygame.mixer.music.play()


def handleEvents(event, done, out_state):
    if (event.type == pygame.QUIT):
        done = True

    if (event.type == Constants.MUSIC_STOPPED):
        playMusic(False)

    if (event.type == Constants.CLICK_PLAY):
        done = True
        out_state = Constants.PLAY_STATE

    return done, out_state


def render(screen, clock, asset_group):
    screen.fill(Constants.BLUE)

    asset_group.draw(screen)

    font = pygame.font.SysFont('Arial', 29)
    screen.blit(font.render('PLAY', True, Constants.RED), (Constants.BUTTON_X_START, Constants.BUTTON_Y_START))

    clock.tick(60)
    pygame.display.flip()