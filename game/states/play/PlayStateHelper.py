import pygame
import Constants

from states.play.LevelAndPillar import LevelAndPillar
from states.play.Player import Player


""" HELPER FUNCTIONS FOR PLAY STATE """

# Creates player and pillar assets
def prepareAssets():
    player = Player()
    play_state = LevelAndPillar(player)
    return player, play_state


# Define player's properties
def initalizePlayer(player, play_state):
    player.level = play_state
    player.rect.x = 340
    player.rect.y = Constants.SCREEN_HEIGHT - player.rect.height


# Adds player to player group- required object for updates
def createPlayerGroup(player):
    player_group = pygame.sprite.Group()
    player_group.add(player)
    return player_group


# Starts game music and creates the clock
def createGameUtilities():
    playMusic(True)
    clock = pygame.time.Clock()
    return clock


# Plays music and restarts music loop
def playMusic(firstTimePlaying):
    pygame.mixer.music.load(Constants.MUSIC_PATH)
    if (firstTimePlaying == False):
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()


# Handles player movement
def playerMovement(event, player):
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


# Handles exit button or pillar hit and loops music when finished
def updateGameUtilities(event, done):
    if (event.type == pygame.QUIT):
        done = True
    if (event.type == Constants.HIT_PILLAR):
        done = True

    if (event.type == Constants.MUSIC_STOPPED):
        playMusic(False)
    return done


# Updates player and pillars
def updateAssets(player_group, play_state):
    player_group.update()
    play_state.update()


# Shifts world if player goes near left or right
def playerBorders(player, play_state):
    if (player.rect.right >= 500):
        player.go_right()
        diff = player.rect.right - 500
        player.rect.right = 500
    if (player.rect.left <= 120):
        diff = 120 - player.rect.left
        player.rect.left = 120


# Draws assets and pillars and runs at 60fps
def render(play_state, player_group, clock, screen):
    play_state.draw(screen)
    player_group.draw(screen)

    clock.tick(60)
    pygame.display.flip()