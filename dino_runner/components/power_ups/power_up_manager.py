import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
class PowerUpManager:
    def __init__(self):
        self.power_ups = []

    def choice_power_up(self):
        self.type = random.randint(0, 1)
        self.power_up = [Shield(), Hammer()]
        self.power_ups.append(self.power_up[self.type])


    def update(self, game_speed, points, player):
        if len(self.power_ups) == 0 and points % 200 == 0:
            self.choice_power_up()
        for power_up in self.power_ups:
             if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.remove(power_up)
             if power_up.used:
                 player.set_power_up(power_up)
             power_up.update(game_speed, player)

    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen) 