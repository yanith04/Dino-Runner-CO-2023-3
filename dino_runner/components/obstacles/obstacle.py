import pygame
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle:
    def __init__(self, image, type):
        self.type = type
        self.image = image
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.destroy = False
        self.destroyed = None

    def update(self, game_speed, player):
        self.rect.x -= game_speed
             
        if self.rect.colliderect(player.dino_rect) and player.hammer:
            self.destroy = True
            self.destroyed = self.type
        if self.rect.colliderect(player.dino_rect):   
            if not player.shield and not player.hammer:
                pygame.time.delay(300)
                player.dead()
        

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
