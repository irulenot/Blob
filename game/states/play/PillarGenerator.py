import Constants
from states.play.Level import Level
from states.play.Pillar import Pillar


class PillarGenerator(Level):

    level_limit = -1500

    # Initalizes player and pillars in level
    def __init__(self, player):
        Level.__init__(self, player)
        level = self.generatePillars()
        self.pillarLogic(level)


    # Describes where pillars spawn and what they do
    def pillarLogic(self, level):
        for pillar_temp in level:
            pillar = Pillar(pillar_temp[0], pillar_temp[1])
            pillar.rect.x = pillar_temp[2]
            pillar.rect.y = pillar_temp[3]
            pillar.boundary_left = 0
            pillar.boundary_right = 2000
            pillar.change_x = 5
            pillar.player = self.player
            pillar.level = self
            self.pillar_list.add(pillar)


    # Creates 2 pillars
    def generatePillars(self):
        level = []
        for n in range(0, 2):
            level.append([Constants.PILLAR_WIDTH, Constants.PILLAR_HEIGHT, Constants.PILLAR_X_START + n * 500,
                          Constants.PILLAR_Y_START])
        return level
