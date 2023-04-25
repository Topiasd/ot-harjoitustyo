import os
import pygame

class Sprite:
    def __init__(self,name:str):
        assets = os.path.dirname(os.path.abspath(__file__))
        self.name = name
        self.image = pygame.image.load(os.path.join(assets,'assets',name+".png"))
        self.pos = [640-self.image.get_width(),480-self.image.get_height()]
        self.dimensions = (self.image.get_width(),self.image.get_height())
        self.speed = 4
        self.move = False
        self.target = [0,0]
    def move_sprite(self):
        if self.move is False:
            return
        x_dis,y_dis=abs(self.pos[0]-self.target[0]),abs(self.pos[1]-self.target[1])
        if x_dis < 5 and y_dis < 5:
            self.move = False
        x_dir,y_dir = 1,1
        if self.target[0]<self.pos[0]:
            x_dir = -1
        if self.target[1]<self.pos[1]:
            y_dir = -1
        if x_dir==-1 and self.pos[0]<=0 or x_dir==1 and self.pos[0]>=1235:
            x_dir = 0
        if y_dir==-1 and self.pos[1]<=0 or y_dir==1 and self.pos[1]>=875:
            y_dir = 0
        if x_dis <= y_dis:
            self.pos[0] += self.speed*(x_dis/y_dis)*x_dir
            self.pos[1] += self.speed*y_dir
        else:
            self.pos[1] += self.speed*(y_dis/x_dis)*y_dir
            self.pos[0] += self.speed*x_dir
    def area_change(self,triggers: list):
        if self.pos[0] >500 and self.pos[0]<650:
            if self.pos[1] >850 and "s" in triggers:
                self.pos[1] =60
                return "s"
            if self.pos[1] <50 and "n" in triggers:
                self.pos[1]=840
                return "n"
        if self.pos[1] >350 and self.pos[1]<500:
            if self.pos[0]>1200 and "e" in triggers:
                self.pos[0] = 50
                return "e"
            if self.pos[0] <40 and "w" in triggers:
                self.pos[0] = 1190
                return "w"
        return False
