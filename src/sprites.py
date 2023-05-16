import os
import pygame
from inventories import Inventory
from random import randint
class Sprite:
    species_stats = {"robo":[5,10,100],"goblin":[10,5,50],"monster":[30,0,30]}
    """Koodi spriteille. Mahdollistaa liikkumisen ruudulla, ja pelialueiden välillä
    Pelaajan tietojen tallentamisen ja lataamisen
    """
    def __init__(self,name:str,species="chest",pos=False,items=1,level=[0,0],container=False):
        self.assets = os.path.dirname(os.path.abspath(__file__))
        self.name=name
        self.species=species
        if not container:
            self.image = pygame.image.load(os.path.join(self.assets,'assets',species+".png"))
        else:
            self.image = pygame.image.load(os.path.join(self.assets,'assets',name+".png"))
        self.pos = pos
        if not pos:
            self.pos = [randint(100,1000),randint(100,800)]
        self.dimensions = (self.image.get_width(),self.image.get_height())
        self.inventory = Inventory(100,container)
        if items in [i for i in range(1000)]:
            self.inventory.generate(items)
        else:
            for i in items:
                self.inventory.add_item(str(i),True)
        if self.species in Sprite.species_stats:
            self.base_damage = Sprite.species_stats[self.species][0]
            self.base_armour = Sprite.species_stats[self.species][1]
            self.max_health = Sprite.species_stats[self.species][2]
            self.health = Sprite.species_stats[self.species][2]
        else:
            self.base_damage = 1
            self.base_armour = 1
            self.max_health = 1
            self.health = 1
        self.damage = 0
        self.armour = 0
        self.speed = 4
        self.move = False
        self.target = [0,0]
        self.level = level 
        self.progress = 0
        self.boss = "Boss"
        if species != "Container":
            self.update_species(self.species)
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
        if y_dir == 0 and x_dir == 0:
            self.move = False
    def area_change(self,triggers: list):
        if self.pos[0] >500 and self.pos[0]<650:
            if self.pos[1] >850 and "s" in triggers:
                self.pos[1] =60
                self.level[0]+=1
                return "s"
            if self.pos[1] <50 and "n" in triggers:
                self.pos[1]=840
                self.level[0]-=1
                return "n"
        if self.pos[1] >350 and self.pos[1]<500:
            if self.pos[0]>1200 and "e" in triggers:
                self.pos[0] = 50
                self.level[1]+=1
                return "e"
            if self.pos[0] <40 and "w" in triggers:
                self.pos[0] = 1190
                self.level[1]-=1
                return "w"
        return False
    def update_stats(self):
        self.damage = self.inventory.damage + self.base_damage
        self.armour = self.inventory.armour + self.base_armour
    def data(self):
        data = {"name":self.name,
                "max_health":self.max_health,
                "health":self.health,
                "speed":self.speed,
                "base_damage":self.base_damage,
                "base_armour":self.base_armour,
                "species":self.species,
                "progress":self.progress,
                "boss":self.boss}
        return data
    def load_player(self,data):
        self.name = data["name"]
        self.max_health = data["max_health"]
        self.speed = data["speed"]
        self.base_damage = data["base_damage"]
        self.base_armour = data["base_armour"]
        self.species = data["species"]
        self.inventory.load_inventory(data)
        self.update_species(data["species"])
    def update_species(self,species):
        self.species = species
        self.image = pygame.image.load(os.path.join(self.assets,'assets',species+".png"))
        self.dimensions = (self.image.get_width(),self.image.get_height())
