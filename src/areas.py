import os
import pygame
from random import choice
from npc import NonPlayer
from interactions import Interactions
class Stage:
    """Tason generointi-koodi. Syötteenä tulee antaa 2d ruudukko, joka koostuu 3x3 paloista. X Merkitsee kulkureittiä,
    ja jokaisen X:n joka ei ole keskellä, tulee johtaa seuraavan palan X:ään, jotta peli toimii. Teema tulee antaa myös, joka määrittää textuurit.
    Ilman syötettä, tai kun valmiit palat loppuvat, tasot generoituvat automaattisesti.
    """
    def __init__(self,name="Boss",progress=0,layout=None,theme_choice="meadow",limit=15):
        self.roads = {"e": [], "w": [], "s": [], "n": [], "middle": []}
        self.visited = set([])
        self.max_size = 0
        self.blocks()
        self.asset_dict = {}
        self.level = {}
        if layout:
            self.layout = self.create(layout)
        else:
            self.max_size +=4
            self.layout = [[["middle","n","s","w","e"]]]
        self.progress = progress
        self.theme = self.theme_init(theme_choice)
        self.limit = max(limit,progress*5)
        self.boss = False
        self.name = name
        self.start_generator()
    def start_generator(self):
        counter = [0,0]
        for i in self.layout:
            for j in i:
                self.generator(counter,j,self.theme)
                counter[1]+=1
            counter[1]=0
            counter[0]+=1
    def generator(self,position,compass,assets,random=False):
        background = assets["background"]
        road = assets["road"]
        area = []
        for i in range(100):
            for j in range(100):
                area.append((background,i*13,j*10))
        for i in compass:
            for j in (self.roads[i]):
                area.append((road,j[0]*13,j[1]*10))
        self.level[str(position[0])+"x"+str(position[1])] = (area,compass)
        if not random:
            self.max_size+=1
    def blocks(self):
        for i in range(45):
            for j in range(40,55):
                self.roads["w"].append((i,j))
        for i in range(55,100):
            for j in range(40,55):
                self.roads["e"].append((i,j))
        for i in range(40,55):
            for j in range(45):
                self.roads["n"].append((i,j))
        for i in range(40,55):
            for j in range(55,100):
                self.roads["s"].append((i,j))
        for i in range(40,55):
            for j in range(40,55):
                self.roads["middle"].append((i,j))
    def create(self,level):
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
        return (level_code)
    def theme_init(self,name:str):
        assets = os.path.dirname(os.path.abspath(__file__))
        background = name+"_background.png"
        road = name+"_road.png"
        asset_dict = {}
        asset_dict["background"]=pygame.image.load(os.path.join(assets,'assets',background))
        asset_dict["road"]=pygame.image.load(os.path.join(assets,'assets',road))
        return asset_dict
    def coin_toss(self):
        return choice([True,False])
    def random_generator(self,area):
        y,x = area.split("x")
        e = str(y)+"x"+str(int(x)+1)
        w = str(y)+"x"+str(int(x)-1)
        n = str(int(y)-1)+"x"+str(x)
        s = str(int(y)+1)+"x"+str(x)
        adjacents = {"e":e,"w":w,"n":n,"s":s}
        directions = {"w":"e","e":"w","n":"s","s":"n"}
        new_level = ["middle"]
        lanes = {"n":"Free","s":"Free","e":"Free","w":"Free"}
        for i in adjacents:
            if adjacents[i] in self.level:
                if directions[i] in self.level[adjacents[i]][1]:
                    lanes[directions[i]]=True
                if directions[i] not in self.level[adjacents[i]][1]:
                    lanes[directions[i]]=False
        for i in lanes:
            if lanes[i]==True:
                new_level.append(directions[i])
                continue
            if lanes[i]=="Free" and self.coin_toss():
                lanes[i]==True
                self.max_size+=1
                new_level.append(directions[i])
        while len(new_level)<3 and self.max_size<self.limit:
            for i in lanes:
                if lanes[i]=="Free" and self.coin_toss():
                    lanes[i]==True
                    self.max_size+=1
                    new_level.append(directions[i])
        distance = max(abs(int(y)),abs(int(x)))
        self.generator([int(y),int(x)],new_level,self.theme,True)
        if self.boss == False:
            if len(self.visited)>=self.limit or self.visited==self.max_size:
                self.boss = True
                self.spawn_boss([int(y),int(x)],distance)
                return
        if len(self.visited)>1:
            self.spawn_npc([int(y),int(x)],distance+1)
    def spawn_boss(self,pos,distance):
        species = choice(["monster","robo","goblin"])
        if self.name not in Interactions.interaction_dict:
            boss =Interactions(self.name,"'The soul stone burns in your pocket'",["Attack"])
            boss_corpse =Interactions(self.name+"loot","'A Soul ripe for harvest'",["Scavenge","Absorb soul"])
        NonPlayer(self.name,species,pos,distance*((self.progress+1)*2),False,False,True)
    def spawn_npc(self,pos,distance):
        species = choice(["monster","robo","chest","goblin"])
        container = species=="chest"
        NonPlayer(species,species,pos,distance*(self.progress+1),False,container)
