
import random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH
class Cloud:
    frames_clouds= 0
    clouds =[]
    for index in range(6):
        x_pos_cloud =1200
        y_pos_cloud = random.randint(0,360)
        game_speed = random.randint(1,8)
        list_clouds = [x_pos_cloud, y_pos_cloud, game_speed]
        clouds.append(list_clouds)
   
    def __init__(self):
        self.image = CLOUD
        self.image_width = self.image.get_width()
        self.x_pos_cloud = SCREEN_WIDTH + random.randint(800, 1000)
        self.y_pos_cloud = random.randint(50,100)

    def update(self, game_speed):
        self.x_pos_cloud -=  game_speed
        if self.x_pos_cloud < -self.image_width:
            self.x_pos_cloud = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y_pos_cloud = random.randint(50,100) 

    def draw_ground (self, screen,):
        
        for cloud in self.clouds:
            cloud[0] -= cloud[2]
            if cloud[0] < -200:
                cloud[0] = 1200
                cloud[1] = random.randint(0,360)
                cloud[2] = random.randint(1,8)

            self.frames_clouds += 1
            if self.frames_clouds >= 81:
                self.frames_clouds= 1

            

            if self.frames_clouds < 11 or self.frames_clouds < 31 or self.frames_clouds < 51 or self.frames_clouds <71 or self.frames_clouds <81 :
               for cloud in self.clouds:
                   screen.blit(self.image,(cloud[0], cloud[1]))