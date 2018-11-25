from states.watch.WatchStateHelper import *


def runWatchState(screen):

    # Play State Initalization
    player, level_and_pillar = prepareAssets()
    initalizePlayer(player, level_and_pillar)
    player_group = createPlayerGroup(player)
    clock = createLoopUtilities()

    # Play State Main Loop
    out_state = Constants.MENU_STATE
    done = False
    while (done == False):


        for event in pygame.event.get():
            playerMovementEvents(event, player)
            done, out_state = handleEvents(event, level_and_pillar, done, out_state)

        updateAssets(player_group, level_and_pillar)
        playerBorders(player)
        render(level_and_pillar, player_group, clock, screen)

    return out_state