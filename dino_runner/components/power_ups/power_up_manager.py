
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
#from dino_runner.components.power_ups.heart import HEART_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears =0
        self.power_ups_collected = 0
        self.list_power_up = ["hammer", "shield"]


    def update(self, game_speed, points, player):
        self.list_power_up= random.choice(self.list_power_up)
        if len(self.power_ups) == 0 and points % 200 == 0 and self.list_power_up == "hammer":
            self.power_ups.append(Hammer())
        if len(self.power_ups) == 0 and points % 200 == 0 and self.list_power_up == "shield":
            self.power_ups.append(Shield())
        for power_up in self.power_ups:
             if power_up.used or power_up.rect.x < -power_up.rect.width or power_up.destroye:
                self.power_ups_collected += 1
                self.power_ups.remove(power_up)
             if power_up.used:
                 player.set_power_up(power_up)
             power_up.update(game_speed, player)
    

             

    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

