import pygame
from areas import Map
from player import Player
from npc import NonPlayer
from interactions import Interactions
class Render:
    def __init__(self):
        self.map = Map()
        self.level = [0,0]
        self.triggers = []
        self.display = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Adventure(?)")
    def add_stash(inventory):
        Render.inventory_list.append(inventory)
    def render(self): #Every different render compiled and ordered
        self.render_map()
        self.render_npc()
        self.render_interaction()
        self.render_player()
        pygame.display.flip()
    def render_map(self): #The background, renderered first
        area = self.map.level[str(self.level[0])+"x"+str(self.level[1])][0]
        self.triggers = self.map.level[str(self.level[0])+"x"+str(self.level[1])][1]
        for i in area:
                self.display.blit(i[0],(i[1],i[2]))
    def render_npc(self): #NPCs rendered second
        for i in NonPlayer.npc_list:
            if i.level == self.level:
                self.display.blit(i.sprite.image,(i.sprite.x,i.sprite.y))
    def render_interaction(self):
        for i in NonPlayer.npc_list:
            if i.collision == True:
                #Here goes a blit for a display box and name
                for j in Interactions.interaction_dict[i.name]:
                    #Here goes a list of different actions that can be taken, to be blit and clickable
                    print (j)
    def render_player(self): #Player rendered last as to remain visible at all times
        self.display.blit(Player.player.image,(Player.player.x,Player.player.y))
    