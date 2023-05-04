import pygame
#import random
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components import text_utils
class Game: 

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.cloud = Cloud()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points  = 0
        self.death_count =0
            
   

        

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing= True
                self.reset_game()

    def update(self):
        if self.playing:
            self.points += 1
            user_input = pygame.key.get_pressed()
            self.player.update(user_input)
            self.cloud.update(self.game_speed)
            self.obstacle_manager.update(self.game_speed, self.player)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.draw_score() 
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        self.cloud.draw_ground(self.screen)
        
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        score, score_text = text_utils.get_message('Points:'+str(self.points),20,1000,40)
        self.screen.blit(score,score_text)

    def draw_menu(self):
        white_color = (255,255,255)
        self.screen.fill(white_color)
        if self.death_count ==0:
           text,text_rect= text_utils.get_message('Press any Key to START', 30)
           self.screen.blit(text,text_rect)
        else:
            text, text_rect = text_utils.get_message('Press any Key to Restart',30)
            score, score_rect= text_utils.get_message('Your score:' + str(self.points),30 +50)
            self.screen.blit(score,score_rect)

    def reset_game(self):
        self.game_speed = 20
        self.player =Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
