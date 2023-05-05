import pygame
from dino_runner.utils.constants import (JUMPING, JUMPING_SHIELD, JUMPING_HAMMER, RUNNING,RUNNING_SHIELD,RUNNING_HAMMER, DUCKING, DUCKING_SHIELD,DUCKING_HAMMER, DEFAULT_TYPE, SHIELD_TYPE,DINO_DEAD,HAMMER_TYPE)
class Dinosaur:
    X_POS =80
    Y_POS = 310
    Y_POS_DUCK =340
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD,HAMMER_TYPE:RUNNING_HAMMER}
        self.duck_img= {DEFAULT_TYPE: DUCKING,SHIELD_TYPE:DUCKING_SHIELD,HAMMER_TYPE:RUNNING_HAMMER}
        self.jump_img= {DEFAULT_TYPE: JUMPING,SHIELD_TYPE:JUMPING_SHIELD,HAMMER_TYPE:RUNNING_HAMMER}
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.dino_rect= self.image.get_rect()
        self.dino_rect.x= self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index =0
        self.dino_run = True
        self.dino_duck= False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_dead = False
        self.flag_hammer = False
        self.flag_shield = False
        self.shield = False
        self.hammer = False
        self.time_up_power_up = 0
        self.time_to_show_shield = 0
        self.time_to_show_hammer = 0

    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_dead:
            self.dead()

        if user_input[pygame.K_DOWN or pygame.K_s] and not self.dino_jump:
           self.dino_run = False
           self.dino_duck= True
           self.dino_jump = False

        elif  user_input[pygame.K_UP or pygame.K_SPACE or pygame.K_w] and not self.dino_jump:
           self.dino_run = False
           self.dino_duck= False
           self.dino_jump = True 
        elif not self.dino_jump:
           self.dino_run = True
           self.dino_duck= False
           self.dino_jump = False


        if self.step_index >=10:
            self.step_index =0

        if self.hammer:
            self.time_to_show_hammer = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if self.time_to_show_hammer <= 0:
                self.reset()

        if self.shield:
            self.time_to_show_shield = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if self.time_to_show_shield <= 0:
                self.reset()

    def draw(self, screen):
        screen.blit(self.image,self.dino_rect)

    def dead(self):
        if self.dino_duck:
            self.image = DINO_DEAD
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.dino_dead = True
        self.image = DINO_DEAD
        self.dino_dead = True

    def run(self):
        self.image = self.run_img[self.type][0] if self.step_index < 5 else self.run_img[self.type][1]
        self.dino_rect= self.image.get_rect()
        self.dino_rect.x= self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index += 1

    def duck(self):
        self.image= self.duck_img[self.type][0] if self.step_index < 5 else self.duck_img[self.type][1]
        self.dino_rect= self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index +=1

    def jump(self):
        self.image= self.jump_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel *4
            self.jump_vel-=0.8
        if self.jump_vel< -self.JUMP_VEL:
            self.dino_rect.y= self.Y_POS
            self.dino_jump= False
            self.jump_vel = self.JUMP_VEL 

    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.shield = True
            self.time_up_power_up = power_up.time_up
            self.flag_shield = True 
        if power_up.type == HAMMER_TYPE:
            self.type = HAMMER_TYPE
            self.hammer = True
            self.time_up_power_up = power_up.time_up
            self.flag_hammer = True 

    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.game_speed = 20
        self.flag_hammer = False
        self.flag_shield = False
        self.hammer = False
        self.time_up_power_up = 0    
      

    
  


    
    

    
    
    
    
