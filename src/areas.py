import os
import pygame
class Map:
    def __init__(self):
        self.asset_list = ["grass","road"]
        self.asset_dict = {}
        for i in self.asset_list:
            self.asset_dict[i]=pygame.image.load(os.path.join('assets', (i+".png")))
        self.level = {}
        self.ens((0,0))
        self.ew((0,1))
        self.ens((1,0))
    def ew(self,position: tuple):
        triggers = ["e","w"]
        area = []
        for i in range(100):
            for j in range(100):
                if i > 40 and i<55:
                    area.append((self.asset_dict["road"],j*13,i*10))
                    continue
                area.append((self.asset_dict["grass"],j*13,i*10))
        self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
    def ensw(self,position: tuple):
        triggers = ["e","n","s","w"]
        area = []
        for i in range(100):
            for j in range(100):
                if i > 40 and i<55 or j>40 and j<55:
                    area.append((self.asset_dict["road"],j*13,i*10))
                    continue
                area.append((self.asset_dict["grass"],j*13,i*10))
        self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
    def ns(self,position: tuple):
        triggers = ["n","s"]
        area = []
        for i in range(100):
            for j in range(100):
                if j>40 and j<55:
                    area.append((self.asset_dict["road"],j*13,i*10))
                    continue
                area.append((self.asset_dict["grass"],j*13,i*10))
        self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
    def nsw(self,position: tuple):
        triggers = ["w","n","s"]
        area = []
        for i in range(100):
            for j in range(100):
                if j>40 and j<55 or i>40 and i<55 and j<55:
                    area.append((self.asset_dict["road"],j*13,i*10))
                    continue
                area.append((self.asset_dict["grass"],j*13,i*10))
        self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
    def ens(self,position: tuple):
        triggers = ["e","n","s"]
        area = []
        for i in range(100):
            for j in range(100):
                if j>40 and j<55 or i>40 and i<55 and j>50:
                    area.append((self.asset_dict["road"],j*13,i*10))
                    continue
                area.append((self.asset_dict["grass"],j*13,i*10))
        self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
    
