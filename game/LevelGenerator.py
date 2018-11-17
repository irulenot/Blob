from Level import Level
from Platform import Platform
from MovingPlatform import MovingPlatform
import constants


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

        # height, width, x, and y
        level.append([constants.BLOCK_HEIGHT, constants.BLOCK_WIDTH, constants.BLOCK_X_START, constants.BLOCK_Y_START])
        # level.append([constants.BLOCK_HEIGHT, constants.BLOCK_WIDTH, 800, 400])
        # level.append([constants.BLOCK_HEIGHT, constants.BLOCK_WIDTH, 1000, 500])
        # level.append([constants.BLOCK_HEIGHT, constants.BLOCK_WIDTH, 1120, 280])
        return level