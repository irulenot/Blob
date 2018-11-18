import Constants
from Level import Level
from Pillar import Pillar


class LevelGenerator(Level):

    level_limit = -1500

    # Initalizes player and pillars in level
    def __init__(self, player):
        Level.__init__(self, player)
        level = self.generatePillars()
        self.pillarLogic(level)


    # Describes where pillars spawn and what they do
    def pillarLogic(self, level):
        for pillar in level:
            block = Pillar(pillar[0], pillar[1])
            block.rect.x = pillar[2]
            block.rect.y = pillar[3]
            block.boundary_left = 0
            block.boundary_right = 2000
            block.change_x = 5
            block.player = self.player
            block.level = self
            self.pillar_list.add(block)


    # Creates 2 pillars
    def generatePillars(self):
        level = []
        for n in range(0, 2):
            level.append([Constants.BLOCK_WIDTH, Constants.BLOCK_HEIGHT, Constants.BLOCK_X_START + n * 500,
                          Constants.BLOCK_Y_START])
        return level
