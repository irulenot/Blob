import Constants
from Level import Level
from MovingPlatform import MovingPlatform


class LevelGenerator(Level):

    level_limit = -1500

    # Initalizes player and platforms in level
    def __init__(self, player):
        Level.__init__(self, player)
        level = self.generatePlatforms()
        self.platformLogic(level)


    # Describes where platforms spawn and what they do
    def platformLogic(self, level):
        for platform in level:
            block = MovingPlatform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.boundary_left = 0
            block.boundary_right = 2000
            block.change_x = 5
            block.player = self.player
            block.level = self
            self.platform_list.add(block)


    # Creates 2 platforms
    def generatePlatforms(self):
        level = []
        for n in range(0, 2):
            level.append([Constants.BLOCK_WIDTH, Constants.BLOCK_HEIGHT, Constants.BLOCK_X_START + n * 500,
                          Constants.BLOCK_Y_START])
        return level
