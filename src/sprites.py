import os
import pygame
class Sprite:
    def __init__(self,name:str):
        self.name = name
        self.image = pygame.image.load(os.path.join('assets', (name+".png")))
        self.coordinates = [640-self.image.get_width(),480-self.image.get_height()]
        self.dimensions = (self.image.get_width(),self.image.get_height())
        self.speed = 4
        self.move_live = False
        self.move_last = False
    def move_sprite(self,destination: tuple):
        x_dis,y_dis=abs(self.coordinates[0]-destination[0]),abs(self.coordinates[1]-destination[1])
        if x_dis < 5 and y_dis < 5:
            return
        x_dir,y_dir = 1,1
        if destination[0]<self.coordinates[0]:
            x_dir = -1
        if destination[1]<self.coordinates[1]:
            y_dir = -1
        if x_dir==-1 and self.coordinates[0]<=0 or x_dir==1 and self.coordinates[0]>=1235:
            x_dir = 0
        if y_dir==-1 and self.coordinates[1]<=0 or y_dir==1 and self.coordinates[1]>=875:
            y_dir = 0
        if x_dis <= y_dis:
            self.coordinates[0] += self.speed*(x_dis/y_dis)*x_dir
            self.coordinates[1] += self.speed*y_dir
        else:
            self.coordinates[1] += self.speed*(y_dis/x_dis)*y_dir
            self.coordinates[0] += self.speed*x_dir
    def area_change(self,triggers: list):
        if self.coordinates[0] >500 and self.coordinates[0]<650:
            if self.coordinates[1] >850 and "s" in triggers:
                self.coordinates[1] =60
                return "s"
            if self.coordinates[1] <50 and "n" in triggers:
                self.coordinates[1]=840
                return "n"
        if self.coordinates[1] >350 and self.coordinates[1]<500:
            if self.coordinates[0]>1200 and "e" in triggers:
                self.coordinates[0] = 50
                return "e"
            if self.coordinates[0] <40 and "w" in triggers:
                self.coordinates[0] = 1190
                return "w"
        return False
