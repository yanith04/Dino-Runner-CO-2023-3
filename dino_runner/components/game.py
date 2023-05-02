import pygame
import random
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import dinosaur

class Game:
    

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.game_speeds= 25
        #self.cloud= CLOUD
        self.x_pos_cloud = SCREEN_WIDTH + random.randint(800,1000)
        self.y_pos_cloud = random.randint(50,100)
        self.player = dinosaur()
        #self.clouds = []         #self.x_pos_cloud >= 100
        
            
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

       
               

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
       
       # for cloud in range (1,5):
        # self.clouds.append(CLOUD)
       
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        if  self.x_pos_cloud <= -image_width:
            self.x_pos_cloud = SCREEN_WIDTH + random.randint(2500,3000) 
            self.y_pos_cloud = random.randint(50,100)    
        self.x_pos_cloud -= self.game_speeds
        #for i in range (5):
         #self.clouds.append(CLOUD)
           # self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
    #frame_clouds= 0
    #clouds = []
    #for index in range(6):
     #   x_pos_cloud = SCREEN_WIDTH + random.randint(800,1000)
    #  y_pos_cloud = random.randint(50,100)
     #   speed_cloud = random.randint(1,8)
      #  list_clouds = [x_pos_cloud,y_pos_cloud, speed_cloud]
       # clouds.append(list_clouds)

        


        
