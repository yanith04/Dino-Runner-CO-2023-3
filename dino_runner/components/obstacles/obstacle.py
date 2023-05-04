
import pygame
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import DINO_DEAD


class Obstacle:
    def __init__(self, image, type):
        self.type = type
        self.image = image
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if not player.shield:
               player.hammer
               pygame.time.delay(100)
               player.dino_dead = True  

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
