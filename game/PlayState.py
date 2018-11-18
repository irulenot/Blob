import pygame

import Constants
from LevelGenerator import LevelGenerator
from Player import Player


""" PLAY STATE HELPERS"""

# Creates player and platform assets
def prepareAssets():
    player = Player()
    play_state = LevelGenerator(player)
    return player, play_state


# Plays music and restarts music loop
def playMusic(firstTimePlaying):
    pygame.mixer.music.load(Constants.MUSIC_PATH)
    if firstTimePlaying is False:
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()


# Handles player movements and exit game
def gameLogic(event, player, done):
    if event.type == pygame.QUIT:
        done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.go_left()
        if event.key == pygame.K_RIGHT:
            player.go_right()
        if event.key == pygame.K_UP:
            player.jump()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT and player.change_x < 0:
            player.stop()
        if event.key == pygame.K_RIGHT and player.change_x > 0:
            player.stop()

    return done


# Updates player and platforms
def updateAssets(player_group, play_state):
    player_group.update()
    play_state.update()


""" MAIN LOOP FOR PLAY STATE """
def runPlayState(screen):
    player, play_state = prepareAssets()

    # Set the current level
    current_level_no = 0

    player_group = pygame.sprite.Group()
    player.level = play_state

    player.rect.x = 340
    player.rect.y = Constants.SCREEN_HEIGHT - player.rect.height
    player_group.add(player)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    playMusic(True)

    done = False

    while not done:

        for event in pygame.event.get():
            done = gameLogic(event, player, done)

        updateAssets(player_group, play_state)

        # Replays song if it ends
        if event.type == pygame.constants.USEREVENT:
            playMusic(False)

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            play_state.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            play_state.shift_world(diff)

        play_state.draw(screen)
        player_group.draw(screen)

        # 60 fps
        clock.tick(60)

        # Updates screen with drawings
        pygame.display.flip()
