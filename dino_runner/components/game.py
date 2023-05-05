import pygame
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
            if event.type == (pygame.KEYDOWN) and not self.playing:
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
            self.draw_power_up() 
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
        else:
            self.draw_menu()
        self.player.draw(self.screen)
        self.draw_bg_menu()
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

    def draw_bg_menu(self):
        if self.playing == False:
            image_width = BG.get_width()
            self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

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
           # game_over, game_over_rect = text_utils.get_message("GAME OVER", 30, height= SCREEN_HEIGHT//2)
            text, text_rect = text_utils.get_message("Press any key to Restart", 30)
            score, score_rect = text_utils.get_message("Your score: "+ str(self.points), 30 )#, height= SCREEN_HEIGHT//2 + 50)
            collect_power_up, collect_power_up_rect = text_utils.get_message("Your collected power ups: "+ str(self.power_up_manager.power_ups_collected), 30, height= SCREEN_HEIGHT//2 + 90)
            overcome_obstacle, overcome_obstacle_rect = text_utils.get_message("Your obstacles overcome: "+ str(self.obstacle_manager.obstacles_overcome), 30, height= SCREEN_HEIGHT//2 + 130)
            death, death_rect =text_utils.get_message("Deaths: " + str(self.death_count), 20, 1000, 40) 
            self.screen.blit(death,death_rect)
            #self.screen.blit(game_over, game_over_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect) 
            self.screen.blit(collect_power_up, collect_power_up_rect)
            self.screen.blit(overcome_obstacle, overcome_obstacle_rect)
    
    def draw_power_up(self):

        if self.player.flag_shield:
              text, text_rect = text_utils.get_message("Time left of shield: "+ str(self.player.time_to_show_shield), 20, 980, 80)
              self.screen.blit(text, text_rect)

        if self.player.flag_hammer:
              text, text_rect = text_utils.get_message("Time left of hammer: "+ str(self.player.time_to_show_hammer), 20, 970, 100)
              self.screen.blit(text, text_rect)


    def reset_game(self):
        self.game_speed = 20
        self.player =Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0