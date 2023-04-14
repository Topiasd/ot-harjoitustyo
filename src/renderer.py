import pygame
from areas import Map
from player import Player
class Render:
    def __init__(self):
        self.render_list = []
        self.map = Map()
        self.level = [0,0]
        self.triggers = []
        self.display = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Adventure(?)")
    def add_npc(npc):
        Render.npc_list.append(npc)
    def add_stash(inventory):
        Render.inventory_list.append(inventory)
    def render(self):
        area = self.map.level[str(self.level[0])+"x"+str(self.level[1])][0]
        self.triggers = self.map.level[str(self.level[0])+"x"+str(self.level[1])][1]
        for i in area:
                self.display.blit(i[0],(i[1],i[2]))
        for i in self.render_list:
            if i.level == self.level:
                self.display.blit(i.sprite.image,(i.sprite.x,i.sprite.y))
        self.display.blit(Player.player.image,(Player.player.x,Player.player.y))
        pygame.display.flip()
