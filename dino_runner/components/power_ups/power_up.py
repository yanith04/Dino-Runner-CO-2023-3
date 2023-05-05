import pygame
from dino_runner.utils.constants import SCREEN_WIDTH
#from dino_runner.components.power_ups.heart import HEART_TYPE
#from dino_runner.utils.constants import DEFAULT_TYPE
class PowerUp:
    Y_POS_POWER_UP = 125,300
    POWER_UP_DURATION = 5000

    def __init__(self, image, type):
        
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = self.Y_POS_POWER_UP
#puedes variarlo
        self.star_time = 0
        self.time_up = 0
        self.used = False
        

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            self.star_time = pygame.time.get_ticks()
            self.time_up = self.star_time + self.POWER_UP_DURATION
            self.used = True
        


    def draw(self, screen):
        screen.blit(self.image, self.rect)