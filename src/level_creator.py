import os
import pygame
class Creator:
    def __init__(self):
        self.map_list = []
    def create(self,level,theme):
        i=1
        j=1
        level_code = []
        while i < len(level):
            layer = []
            while j < len(level[i]):
                layout = ["middle"]
                if level[i][j+1]=="X":
                    layout.append("e")
                if level[i-1][j]=="X":
                    layout.append("n")
                if level[i+1][j]=="X":
                    layout.append("s")
                if level[i][j-1]=="X":
                    layout.append("w")
                layer.append(layout)
                j += 3
            level_code.append(layer)
            i += 3
            j = 1
        return (level_code,theme)
    def stage1(self):
        return  self.create([
            "#########",
            "#XXXXXXX#",
            "#X##X####",
            "#X##X####",
            "#XXXX####",
            "#########"
        ],self.grass())
    def grass(self):
        assets = os.path.dirname(os.path.abspath(__file__))
        asset_dict = {}
        asset_dict["background"]=pygame.image.load(os.path.join(assets,'assets','grass.png'))
        asset_dict["road"]=pygame.image.load(os.path.join(assets,'assets','road.png'))
        return asset_dict
