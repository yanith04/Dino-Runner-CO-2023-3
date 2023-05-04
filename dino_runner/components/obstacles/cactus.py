import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle

CACTUS = [LARGE_CACTUS,SMALL_CACTUS]


class Cactus(Obstacle):
    Y_POS_CACTUS = [315,320,325]

    def __init__(self):
        self.image = CACTUS[random.randint(0,1)]
        super().__init__(self.image, 0 )
        self.rect.y = random.choice (self.Y_POS_CACTUS)








        #image, cactus_pos = self.CACTUS[random.randint(0, 1)]
        #self.type = random.randint(0, 2)
        #super().__init__(image, self.type)
        #self.rect.y = cactus_pos

    #
    #CACTUS = [SMALL_CACTUS, LARGE_CACTUS]
    #def __init__(self):
     #   self.image = CACTUS()
      #  super().__init__(self.image)
     #   self.rect.y = self.Y_POS_CACTUS