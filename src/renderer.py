import pygame
from areas import Stage
from npc import NonPlayer
from interactions import Interactions
from menus import Menu
class Render:
    def __init__(self):
        self.map = Stage()
        self.level = [0,0]
        self.triggers = []
        self.buttons = []
        self.display = pygame.display.set_mode((1280, 960))
        self.font = pygame.font.SysFont("Futura", 50)
        pygame.display.set_caption("Adventure(?)")
    def render(self,player):
        self.render_map()
        self.render_npc()
        self.render_interaction()
        self.render_player(player)
        self.render_menus()
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
        self.buttons = []
        for i in NonPlayer.npc_list:
            if i.collision is True:
                pygame.draw.rect(self.display,(0,0,0), ((430, 790, 420,200)))
                pygame.draw.rect(self.display,(255,255,255), ((440, 800, 400,150)))
                name = self.font.render(i.name,True,(0,0,0))
                hey = self.font.render(Interactions.interaction_dict[i.name].hey,True,(0,0,0))
                self.display.blit(hey,(440,920))
                self.display.blit(i.sprite.image,(440,800))
                self.display.blit(name, (500, 800))
                line = 0
                for j in Interactions.interaction_dict[i.name].actions:
                    action = self.font.render(j, True, (0, 0, 0))
                    width = action.get_width()
                    self.display.blit(action, (840-width, 800+(30*line)))
                    self.buttons.append((j,(840-width,800+(30*line),width,30)))
                    line += 1
    def render_player(self,player):
        self.display.blit(player.image,(player.coordinates[0],player.coordinates[1]))
    def render_menus(self):
        if Menu.active_menu is not None:
            pass
