import pygame
import Constants

from states.play.LevelAndPillar import LevelAndPillar
from states.play.Player import Player


def logNewGame():
    p = open(Constants.PILLAR_LOG_PATH, "a")
    p.write('\nNEWGAME\n')
    f = open(Constants.EVENT_LOG_PATH, "a")
    f.write('\nNEWGAME\n')


# Creates player and pillar assets
def prepareAssets():
    player = Player()
    level_and_pillar = LevelAndPillar(player)
    return player, level_and_pillar


# Define player's properties
def initalizePlayer(player, level_and_pillar):
    player.level = level_and_pillar
    player.rect.x = 340
    player.rect.y = Constants.SCREEN_HEIGHT - player.rect.height


# Adds player to player group- required object for updates
def createPlayerGroup(player):
    player_group = pygame.sprite.Group()
    player_group.add(player)
    return player_group


# Starts game music, creates the clock, and creates pillar generation timer
def createLoopUtilities():
    pygame.mixer.music.load(Constants.PLAY_MUSIC_PATH)
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    pygame.time.set_timer(Constants.GENERATE_PILLAR, Constants.GENERATE_PILLAR_FREQUENCY)
    return clock


def logEvents(event):
    f = open(Constants.EVENT_LOG_PATH, "a")
    f.write(str(event))
    f.write('\n')


# Handles player movement
def playerMovementEvents(event, player):
    if (event.type == pygame.KEYDOWN):
        if (event.key == pygame.K_LEFT):
            player.go_left()
        if (event.key == pygame.K_RIGHT):
            player.go_right()
        if (event.key == pygame.K_UP):
            player.jump()
    if (event.type == pygame.KEYUP):
        if (event.key == pygame.K_LEFT) and (player.change_x < 0):
            player.stop()
        if (event.key == pygame.K_RIGHT) and (player.change_x > 0):
            player.stop()


# Handles exit button and loops music when finished
# Handles pillar hit and pillar generation
def handleEvents(event, level_and_pillar, done, out_state):
    if (event.type == Constants.HIT_PILLAR):
        out_state = Constants.MENU_STATE
        done = True

    if (event.type == Constants.GENERATE_PILLAR):
        level_and_pillar.generatePillar()

    # Quit conditions
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            done = True

    if (event.type == pygame.QUIT):
        done = True

    return done, out_state


# Updates player and pillars
def updateAssets(player_group, level_and_pillar):
    player_group.update()
    level_and_pillar.update()


# Keeps player within borders
def playerBorders(player):
    if (player.rect.right >= 500):
        player.rect.right = 500
    if (player.rect.left <= 120):
        player.rect.left = 120


# Draws assets and pillars and runs at 60fps
def render(level_and_pillar, player_group, clock, screen):
    level_and_pillar.draw(screen)
    player_group.draw(screen)

    clock.tick(60)
    pygame.display.flip()


# Writes to data files if data is valid
def manageLogs(out_state):

    if(out_state == Constants.MENU_STATE):
        event_log = open(Constants.EVENT_LOG_PATH, "r")
        event_data = open(Constants.EVENT_DATA_PATH, "a")
        event_data.write(event_log.read())

        pillar_log = open(Constants.PILLAR_LOG_PATH, "r")
        pillar_data = open(Constants.PILLAR_DATA_PATH, "a")
        pillar_data.write(pillar_log.read())

    open(Constants.EVENT_LOG_PATH, 'w').close()
    open(Constants.PILLAR_LOG_PATH, 'w').close()
