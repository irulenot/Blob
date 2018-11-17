from Level import Level
from MovingPlatform import MovingPlatform
import Constants


class LevelGenerator(Level):

    def __init__(self, player):

        # initalizing player in level
        Level.__init__(self, player)
        self.level_limit = -1500

        # initalizing platforms in level
        level = self.generatePlatforms()
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

    def generatePlatforms(self):
        level = []

        for n in range(0, 2):
            level.append([Constants.BLOCK_WIDTH, Constants.BLOCK_HEIGHT, Constants.BLOCK_X_START + n*500, Constants.BLOCK_Y_START])

        return level