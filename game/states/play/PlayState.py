from states.play.playStateLogger import *
from states.play.PlayStateHelper import *


def runPlayState(screen):

    # Play State Initalization
    logGameTime()
    player, level_and_pillar = prepareAssets()
    initalizePlayer(player, level_and_pillar)
    player_group = createPlayerGroup(player)
    clock = createLoopUtilities()

    # Play State Main Loop
    out_state = Constants.QUIT_STATE
    done = False
    while (done == False):
        for event in pygame.event.get():
            logEvents(event)
            playerMovementEvents(event, player)
            done, out_state = handleEvents(event, level_and_pillar, done, out_state)

        updateAssets(player_group, level_and_pillar)
        playerBorders(player)
        render(level_and_pillar, player_group, clock, screen)

    # Logs play play_data and new game state
    manageLogs(out_state)
    return out_state