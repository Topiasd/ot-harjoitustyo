import os
import pygame
class Sprite:
    def __init__(self,name:str):
        self.name = name
        self.image = pygame.image.load(os.path.join('assets', (name+".png")))
        self.X = 640-self.image.get_width()
        self.Y = 480-self.image.get_height()
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
        if destination[0]<self.X:
            x_direction = -1
        if destination[1]<self.Y:
            y_direction = -1
        x_dis = abs(self.X - destination[0])
        y_dis = abs(self.Y - destination[1])
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
            self.X += self.speed*(x_dis/y_dis)*x_direction
            self.Y += self.speed*y_direction
        else:
            self.Y += self.speed*(y_dis/x_dis)*y_direction
            self.X += self.speed*x_direction
    def check_wall_collision(self):
        self.pos_y_collision = False
        self.pos_x_collision = False
        self.neg_y_collision = False
        self.neg_x_collision = False
        if  self.X < 5:
            self.neg_x_collision = True
        if  self.X > 1275-self.dimensions[0]:
            self.pos_x_collision = True
        if  self.Y < 5:
            self.neg_y_collision = True
        if  self.Y > 955-self.dimensions[1]:
            self.pos_y_collision = True
    def area_change(self,triggers: list):
        if self.X >500 and self.X<650:
            if self.Y >850 and "s" in triggers:
                self.Y =60
                return "s"
            if self.Y <50 and "n" in triggers:
                self.Y=840
                return "n"
        if self.Y >350 and self.Y<500:
            if self.X>1200 and "e" in triggers:
                self.X = 50
                return "e"
            if self.X <40 and "w" in triggers:
                self.X = 1190
                return "w"
        return False