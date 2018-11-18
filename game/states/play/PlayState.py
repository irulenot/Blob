from states.play.PlayStateHelper import *


""" MAIN LOOP FOR PLAY STATE """
def runPlayState(screen):
    player, play_state = prepareAssets()
    initalizePlayer(player, play_state)
    player_group = createPlayerGroup(player)
    clock = createGameUtilities()

    play_state.generatePillar(0)

    done = False
    while (done == False):
        for event in pygame.event.get():
            playerMovement(event, player)
            done = updateGameUtilities(event, done)

        updateAssets(player_group, play_state)
        playerBorders(player, play_state)
        render(play_state, player_group, clock, screen)