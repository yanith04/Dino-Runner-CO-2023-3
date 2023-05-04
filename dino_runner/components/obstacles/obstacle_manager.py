#import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Birds
#from dino_runner.components.obstacles.dinosaur import Dinosaur

class ObstacleManager:
    def __init__(self):
       
        self.obstacles = []
    
    
    def choice_obstacle(self):
        self.type = random.randint(0, 1)
        self.obstacle = [Cactus(), Birds(),]
        self.obstacles.append(self.obstacle[self.type])

    def update(self, game_speed, player):
        if len(self.obstacles) == 0:
            self.choice_obstacle()

        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
               self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)


            
                
                

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
#class ObstacleManager:
 #   def __init__(self):
  #      self.obstacles = []
        

   # def update(self,game_speed,player):
    #    if len(self.obstacles) == 0:
     #       self.obstacles.append(Cactus())
      #  for obstacle in self.obstacles:
       #     if obstacle.rect.x < -obstacle.rect.width:
        #        self.obstacles.remove(obstacle)
         #   obstacle.update(game_speed, player)
    
    #def draw(self,screen):
     #   for obstacle in self.obstacles:
      #      obstacle.draw(screen)
        






    





