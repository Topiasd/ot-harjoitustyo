import pygame
from areas import Stage
from npc import NonPlayer
from interactions import Interactions
from textbox import Blits
class Render:
    """Kaikki mitä ruudulle ilmestyy, kulkee tämän luokan kautta. Eri tilanteille on erilaiset säännöt.
    """
    def __init__(self,menu,progress=0,boss="Boss"):
        self.map = Stage(boss,progress)
        self.menu = menu
        self.level = [0,0]
        self.triggers = []
        self.buttons = []
        self.display = pygame.display.set_mode((1280, 960))
        self.font = pygame.font.SysFont("Futura", 50)
        self.inventory_font = pygame.font.SysFont("Futura", 25)
        self.interaction_font = pygame.font.SysFont("Futura", 25)
        pygame.display.set_caption("A Little Soul Searching")
    def render(self,player):
        if self.menu.pause is False:
            self.render_map()
            self.render_npc()
            self.render_interaction(player)
            self.render_ui(player)
            self.render_player(player)
        else:
            self.render_menus()
        if self.menu.inventory is not False:
            self.render_inventory(player,self.menu.inventory)
        if self.menu.battle is True:
            self.render_ui(player)
            self.render_battle(player,NonPlayer.active_collision)
        if self.menu.exchange is True:
            self.render_inventory(player,self.menu.inventory)
            self.render_ext_inventory(NonPlayer.active_collision)
        pygame.display.flip()
    def render_map(self):
        """Nykyisen tason rakennuspalikat renderöidään ensimmäiseksi, ja tason mukana tulee koodi joka kertoo milloin taso
        """
        new_level = str(self.level[0])+"x"+str(self.level[1])
        self.map.visited.add(new_level)
        if new_level not in self.map.level:
            self.map.random_generator(new_level)
        area = self.map.level[new_level][0]  
        self.triggers = self.map.level[new_level][1]
        for i in area:
            self.display.blit(i[0],(i[1],i[2]))
    def render_npc(self):
        for i in NonPlayer.npc_list:
            if i.sprite.level == self.level:
                self.display.blit(i.sprite.image,(i.sprite.pos))
    def render_interaction(self,player):
        self.buttons = []
        for i in NonPlayer.npc_list:
            if i.collision:
                pygame.draw.rect(self.display,(0,0,0), ((430, 790, 420,200)))
                pygame.draw.rect(self.display,(255,255,255), ((440, 800, 400,150)))
                hey = self.interaction_font.render(Interactions.interaction_dict[i.name].hey,True,(0,0,0))
                threat = player.inventory.threat-i.sprite.inventory.threat
                if threat<-10:
                    threat = "High threat!"
                    threat = self.font.render(threat,True,(255,64,64))
                elif threat>10:
                    threat = "Low threat"
                    threat = self.font.render(threat,True,(124,252,0))
                else:
                    threat = "Medium threat"
                    threat = self.font.render(threat,True,(255,255,64))
                self.display.blit(hey,(440,920))
                self.display.blit(i.sprite.image,(450,810))
                if i.inventory.container == False:
                    self.display.blit(threat,(450,810+i.sprite.dimensions[1]))
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
        enemy_health = self.font.render("Health "+str(enemy.sprite.health), True, (0, 0, 0))
        enemy_damage = self.font.render("Damage "+str(enemy.sprite.damage), True, (0, 0, 0))
        enemy_armour = self.font.render("Armour "+str(enemy.sprite.armour), True, (0, 0, 0))
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
    def render_inventory(self,player,menu):
        height = len(player.inventory.info(menu))
        width = 20
        for i in player.inventory.info(menu):
            if len(i) > width:
                width=len(i)
        width *= 9
        pygame.draw.rect(self.display,(0,0,0), ((0, 0, int(width),30*height+10)))
        pygame.draw.rect(self.display,(255,255,255), ((10, 10, int(width)-20,30*height-10)))
        line = 0
        for i in player.inventory.info(menu):
            text = self.inventory_font.render(i, True, (0, 0, 0))
            width = text.get_width()
            self.buttons.append((str(i),(10,10+(30*line),width,30)))
            self.display.blit(text,(10,line*30+10))
            line += 1
    def render_ui(self,player):
        inst = Blits.button_blit("Inventory",(0,0),110,40,25)
        for i in inst["rectangle"]:
            pygame.draw.rect(self.display,i[0],i[1])
        for i in inst["button"]:
            self.buttons.append(i)
        for i in inst["text"]:
            self.display.blit(i[0],i[1])
        self.render_health_bar(player)
    def render_ext_inventory(self,container):
        width = 20
        info = container.inventory.ext_info()
        for i in info:
                if len(i)>width:
                    width=len(i)
        height = len(info)
        corner = 1280-int(width*10)
        pygame.draw.rect(self.display,(0,0,0), ((corner, 0, 1000,30*height+10)))
        pygame.draw.rect(self.display,(255,255,255), ((corner+10, 10, 1260-corner,30*height-10)))
        line = 0
        for i in info:
                text = self.inventory_font.render(i, True, (0, 0, 0))
                width = text.get_width()
                self.buttons.append(("*"+(str(i)),(1270-width,10+(30*line),width,30)))
                self.display.blit(text,(1270-width,line*30+10))
                line += 1
    def render_health_bar(self,player):
        pygame.draw.rect(self.display,(0,0,0), ((0, 940, 180,60)))
        pygame.draw.rect(self.display,(255,255,255), ((10, 945, 160,10)))
        pygame.draw.rect(self.display,(255,64,64), ((10, 945,160*player.health//player.max_health,10)))
