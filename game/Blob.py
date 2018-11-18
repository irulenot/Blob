import pygame
import Constants
import Initalization
from LevelGenerator import LevelGenerator
from Player import Player


""" Main Program """
screen = Initalization.loadEnvironment()

# Create the player
player = Player()

# Create all the levels
level_list = []
level_list.append(LevelGenerator(player))

# Set the current level
current_level_no = 0
current_level = level_list[current_level_no]

active_sprite_list = pygame.sprite.Group()
player.level = current_level

player.rect.x = 340
player.rect.y = Constants.SCREEN_HEIGHT - player.rect.height
active_sprite_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# MUTED FOR DEVELOPMENT
# Play music
# pygame.mixer.music.load(Constants.MUSIC_PATH)
# pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
# pygame.mixer.music.play()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
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

    # Update the player.
    active_sprite_list.update()

    # Update items in the level
    current_level.update()

    # MUTED FOR DEVELOPMENT
    # Replays song if it ends
    # if event.type == pygame.constants.USEREVENT:
    #     pygame.mixer.music.load('../resources/Platformer2.mp3')
    #     pygame.mixer.music.play()

    # If the player gets near the right side, shift the world left (-x)
    if player.rect.right >= 500:
        diff = player.rect.right - 500
        player.rect.right = 500
        current_level.shift_world(-diff)

    # If the player gets near the left side, shift the world right (+x)
    if player.rect.left <= 120:
        diff = 120 - player.rect.left
        player.rect.left = 120
        current_level.shift_world(diff)

    # If the player gets to the end of the level, go to the next level
    current_position = player.rect.x + current_level.world_shift
    if current_position < current_level.level_limit:
        if current_level_no < len(level_list)-1:
            player.rect.x = 120
            current_level_no += 1
            current_level = level_list[current_level_no]
            player.level = current_level
        else:
            # Out of levels. This just exits the program.
            # You'll want to do something better.
            done = True

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    current_level.draw(screen)
    active_sprite_list.draw(screen)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
