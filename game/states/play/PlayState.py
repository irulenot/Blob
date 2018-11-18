from states.play.PlayStateHelper import *


def runPlayState(screen):

    # Play State Initalization
    player, level_and_pillar = prepareAssets()
    initalizePlayer(player, level_and_pillar)
    player_group = createPlayerGroup(player)

    # Play State Main Loop
    clock = createLoopUtilities()

    done = False
    while (done == False):
        for event in pygame.event.get():
            playerMovementEvents(event, player)
            done = handleEvents(event, level_and_pillar, done)

        updateAssets(player_group, level_and_pillar)
        playerBorders(player)
        render(level_and_pillar, player_group, clock, screen)