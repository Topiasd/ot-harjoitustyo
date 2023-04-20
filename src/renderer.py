import pygame
from areas import Stage
from npc import NonPlayer
from interactions import Interactions
class Render:
    def __init__(self):
        self.map = Stage()
        self.level = [0,0]
        self.triggers = []
        self.display = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Adventure(?)")
    def render(self,player):
        self.render_map()
        self.render_npc()
        self.render_interaction()
        self.render_player(player)
        pygame.display.flip()
    def render_map(self):
        area = self.map.level[str(self.level[0])+"x"+str(self.level[1])][0]
        self.triggers = self.map.level[str(self.level[0])+"x"+str(self.level[1])][1]
        for i in area:
            self.display.blit(i[0],(i[1],i[2]))
    def render_npc(self):
        for i in NonPlayer.npc_list:
            if i.level == self.level:
                self.display.blit(i.sprite.image,(i.sprite.coordinates[0],i.sprite.coordinates[1]))
    def render_interaction(self):
        for i in NonPlayer.npc_list:
            if i.collision is True:
                print (Interactions.interaction_dict[i.name].greeting)
    def render_player(self,player):
        self.display.blit(player.image,(player.coordinates[0],player.coordinates[1]))
