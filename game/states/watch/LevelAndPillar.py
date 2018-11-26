import Constants
from states.watch.Level import Level
from states.watch.Pillar import Pillar


# Creates the level, puts the player in it, and generates the pillars and their properties
class LevelAndPillar(Level):

    level_limit = -1500

    # Initalizes player and pillars in level
    def __init__(self, player):
        Level.__init__(self, player)


    # Creates 2 pillars
    def generatePillar(self):

        pillar = Pillar(Constants.PILLAR_WIDTH, Constants.PILLAR_HEIGHT)
        pillar.rect.x = Constants.PILLAR_X_START
        pillar.rect.y = Constants.PILLAR_Y_START
        pillar.boundary_left = 0
        pillar.boundary_right = 2000
        pillar.change_x = 5
        pillar.player = self.player
        pillar.level = self
        self.pillar_list.add(pillar)