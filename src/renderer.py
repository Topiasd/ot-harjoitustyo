import pygame
from areas import Stage
from npc import NonPlayer
from interactions import Interactions
class Render:
    """Kaikki mitä ruudulle ilmestyy, kulkee tämän luokan kautta. Eri tilanteille on erilaiset säännöt.
    """
    def __init__(self,layout,theme,menu):
        self.map = Stage(layout,theme)
        self.menu = menu
        self.level = [0,0]
        self.triggers = []
        self.buttons = []
        self.display = pygame.display.set_mode((1280, 960))
        self.font = pygame.font.SysFont("Futura", 50)
        pygame.display.set_caption("Adventure(?)")
    def render(self,player):
        if self.menu.pause is False:
            self.render_map()
            self.render_npc()
            self.render_interaction()
            self.render_player(player)
        else:
            self.render_menus()
        if self.menu.battle is True:
            self.render_battle(player,NonPlayer.active_collision)
        pygame.display.flip()
    def render_map(self):
        """Nykyisen tason rakennuspalikat renderöidään ensimmäiseksi, ja tason mukana tulee koodi joka kertoo milloin taso
        """
        area = self.map.level[str(self.level[0])+"x"+str(self.level[1])][0]
        self.triggers = self.map.level[str(self.level[0])+"x"+str(self.level[1])][1]
        for i in area:
            self.display.blit(i[0],(i[1],i[2]))
    def render_npc(self):
        for i in NonPlayer.npc_list:
            if i.level == self.level:
                self.display.blit(i.sprite.image,(i.sprite.pos))
    def render_interaction(self):
        self.buttons = []
        for i in NonPlayer.npc_list:
            if i.collision and i.level == self.level:
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
        self.display.blit(player.image,(player.pos))
    def render_menus(self):
        self.display.fill((255,255,255))
        self.buttons = self.menu.active_menu["buttons"]
        for j in self.menu.active_menu["blits"]:
            self.display.blit(j[0],j[1])
    def render_battle(self,player,enemy):
        self.display.blit(player.image,(250,800))
        self.display.blit(enemy.sprite.image,(900,800))
        enemy_name = self.font.render(enemy.name, True, (0, 0, 0))
        enemy_health = self.font.render("Health "+str(enemy.health), True, (0, 0, 0))
        enemy_damage = self.font.render("Damage "+str(enemy.damage), True, (0, 0, 0))
        enemy_armour = self.font.render("Armour "+str(enemy.armour), True, (0, 0, 0))
        enemy_stats = [enemy_name,enemy_health,enemy_damage,enemy_armour]
        player_name = self.font.render(player.name, True, (0, 0, 0))
        player_health = self.font.render("Health "+str(player.health), True, (0, 0, 0))
        player_damage = self.font.render("Damage "+str(player.damage), True, (0, 0, 0))
        player_armour = self.font.render("Armour "+str(player.armour), True, (0, 0, 0))
        player_stats = [player_name,player_health,player_damage,player_armour]
        line = 0
        for i in player_stats:
            width = i.get_width()
            self.display.blit(i, (200-width, 800+(30*line)))
            line += 1
        line = 0
        for i in enemy_stats:
            width = i.get_width()
            self.display.blit(i, (1180-width, 800+(30*line)))
            line += 1
