import os
import pygame
from level_creator import Creator
class Stage:
    def __init__(self):
        self.asset_list = ["grass","road"]
        self.asset_dict = {}
        for i in self.asset_list:
            self.asset_dict[i]=pygame.image.load(os.path.join('assets', (i+".png")))
        self.level = {}
        stage = Creator()
        stage_code = stage.stage1()
        for i in range(len(stage_code)):
            for j in range(len(stage_code[i])):
                self.generator((i,j),stage_code[i][j])
    def generator(self,position: tuple,compass: str):
        if compass == "ew":
            triggers = ["e","w"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y > 40 and y<55:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "ensw":
            triggers = ["e","n","s","w"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y > 40 and y<55 or x>40 and x<55:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "ns":
            triggers = ["n","s"]
            area = []
            for y in range(100):
                for x in range(100):
                    if x>40 and x<55:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "nsw":
            triggers = ["w","n","s"]
            area = []
            for y in range(100):
                for x in range(100):
                    if x>40 and x<55 or y>40 and y<55 and x<55:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "ens":
            triggers = ["e","n","s"]
            area = []
            for y in range(100):
                for x in range(100):
                    if x>40 and x<55 or y>40 and y<55 and x>50:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "e":
            triggers = ["e"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y>40 and y<55 and x>45:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "w":
            triggers = ["w"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y>40 and y<55 and x<60:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "n":
            triggers = ["n"]
            area = []
            for y in range(100):
                for x in range(100):
                    if x>40 and x<55 and y<60:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "s":
            triggers = ["s"]
            area = []
            for y in range(100):
                for x in range(100):
                    if x>40 and x<55 and y>40:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "enw":
            triggers = ["e","n","w"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y>40 and y<55 or  x>40 and x<55 and y<55:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "esw":
            triggers = ["e","s","w"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y>40 and y<55 or  x>40 and x<55 and y>40:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "en":
            triggers = ["e","n"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y>40 and y<55 and x>40 or  x>40 and x<55 and y<55:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "nw":
            triggers = ["n","w"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y>40 and y<55 and x<55 or  x>40 and x<55 and y<55:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "sw":
            triggers = ["s","w"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y>40 and y<55 and x<55 or  x>40 and x<55 and y>40:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
        if compass == "es":
            triggers = ["e","s"]
            area = []
            for y in range(100):
                for x in range(100):
                    if y>40 and y<55 and x>40 or  x>40 and x<55 and y>40:
                        area.append((self.asset_dict["road"],x*13,y*10))
                        continue
                    area.append((self.asset_dict["grass"],x*13,y*10))
            self.level[str(position[0])+"x"+str(position[1])] = (area,triggers)
