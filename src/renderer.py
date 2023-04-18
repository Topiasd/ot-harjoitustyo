import pygame
from areas import Stage
from player import Player
from npc import NonPlayer
from interactions import Interactions
class Render:
    def __init__(self):
        self.map = Stage()
        self.level = [0,0]
        self.triggers = []
        self.display = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Adventure(?)")
    def render(self):
        self.render_map()
        self.render_npc()
        self.render_interaction()
        self.render_player()
        pygame.display.flip()
    def render_map(self):
        area = self.map.level[str(self.level[0])+"x"+str(self.level[1])][0]
        self.triggers = self.map.level[str(self.level[0])+"x"+str(self.level[1])][1]
        for i in area:
                self.display.blit(i[0],(i[1],i[2]))
    def render_npc(self):
        for i in NonPlayer.npc_list:
            if i.level == self.level:
                self.display.blit(i.sprite.image,(i.sprite.X,i.sprite.Y))
    def render_interaction(self):
        for i in NonPlayer.npc_list:
            if i.collision is True:
                for j in Interactions.interaction_dict[i.name]:
                    print (j)
    def render_player(self):
        self.display.blit(Player.player.image,(Player.player.X,Player.player.Y))
