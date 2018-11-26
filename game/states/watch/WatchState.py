import Constants
import sys
sys.path.append(Constants.game_directory + "Blob/")
import ai.PlayBlob as ai

import Logger
from states.watch.WatchStateHelper import *


def runWatchState(screen):
    # Play State Initalization
    player, level_and_pillar = prepareAssets()
    initalizePlayer(player, level_and_pillar)
    player_group = createPlayerGroup(player)
    clock = createLoopUtilities()

    # Play State Main Loop
    out_state = Constants.QUIT_STATE
    done = False
    while (done == False):

        ai_action = ai.decision()
        if (ai_action != None):
            playerMovementEvents(player, ai_action)

        # Clears the log as decided on
        Logger.clearLog()

        for event in pygame.event.get():
            done, out_state = handleEvents(event, level_and_pillar, done, out_state)

        updateAssets(player_group, level_and_pillar)
        playerBorders(player)
        render(level_and_pillar, player_group, clock, screen)

    return out_state
