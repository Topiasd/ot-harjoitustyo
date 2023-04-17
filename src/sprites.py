import os
import pygame
class Sprite:
    def __init__(self,name:str):
        self.name = name
        self.image = pygame.image.load(os.path.join('sprites', (name+".png")))
        self.x = 640-self.image.get_width()
        self.y = 480-self.image.get_height()
        self.dimensions = (self.image.get_width(),self.image.get_height())
        self.speed = 4
        self.move_live = False
        self.move_last = False
        self.pos_y_collision = False
        self.pos_x_collision = False
        self.neg_y_collision = False
        self.neg_x_collision = False
    def move_sprite(self,destination: tuple):
        self.check_wall_collision()
        x_direction = 1
        y_direction = 1
        if destination[0]<self.x: x_direction = -1
        if destination[1]<self.y: y_direction = -1
        x_dis = abs(self.x - destination[0])
        y_dis = abs(self.y - destination[1])
        if x_dis < 5 and y_dis < 5:
            return
        if x_dis == 0 or self.pos_x_collision and x_direction == 1:
            y_dis += self.speed*y_direction
        elif y_dis == 0 or self.pos_y_collision and y_direction == 1:
            x_dis += self.speed*x_direction
        elif x_dis == 0 or self.neg_x_collision and x_direction == -1:
            y_dis += self.speed*y_direction
        elif y_dis == 0 or self.neg_y_collision and y_direction == -1:
            x_dis += self.speed*x_direction
        elif self.neg_y_collision and y_direction == -1 and self.pos_x_collision and x_direction == 1 or self.neg_y_collision and y_direction == 1 and self.pos_x_collision and x_direction == -1:
            return
        elif self.neg_y_collision and y_direction == 1 and self.pos_x_collision and x_direction == 1 or self.neg_y_collision and y_direction == -1 and self.pos_x_collision and x_direction == -1:
            return
        elif x_dis <= y_dis:
            self.x += self.speed*(x_dis/y_dis)*x_direction
            self.y += self.speed*y_direction
        else:
            self.y += self.speed*(y_dis/x_dis)*y_direction
            self.x += self.speed*x_direction
    def check_wall_collision(self):
        self.pos_y_collision = False
        self.pos_x_collision = False
        self.neg_y_collision = False
        self.neg_x_collision = False
        if  self.x < 5:
            self.neg_x_collision = True
        if  self.x > 1275-self.dimensions[0]:
            self.pos_x_collision = True
        if  self.y < 5:
            self.neg_y_collision = True
        if  self.y > 955-self.dimensions[1]:
            self.pos_y_collision = True
    def area_change(self,triggers: list):
        if self.x >500 and self.x<650:
            if self.y >850 and "s" in triggers:
                self.y =60
                return "s"
            if self.y <50 and "n" in triggers:
                self.y=840
                return "n"
        if self.y >350 and self.y<500:
            if self.x>1200 and "e" in triggers:
                self.x = 50
                return "e"
            if self.x <40 and "w" in triggers:
                self.x = 1190
                return "w"
        return False