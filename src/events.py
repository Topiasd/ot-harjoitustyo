import sys
import pygame
from npc import NonPlayer
class Events:
    """Tapahtumat (hiiren painallukset) ja niistä seuraavat tilannemuutokset löytyvät täältä
    """
    def __init__(self,menu):
        self.menu = menu
    def event_queue(self,player,stage):
        player.move_sprite()
        for i in NonPlayer.npc_list:
            i.npc_actions(player)
        area_change = player.area_change(stage.triggers)
        if area_change is not False:
            if area_change == "s":
                stage.level[0]+=1
            if area_change == "n":
                stage.level[0]-=1
            if area_change == "e":
                stage.level[1]+=1
            if area_change == "w":
                stage.level[1]-=1
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                self.mouse_event(event.pos,stage,player)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu.activate_menu("Pause")
            if event.type == pygame.QUIT:
                sys.exit()
    def activate(self,points,target):
        """Tarkistaa, osuuko hiiren painallus nappulaan

        Args:
            points (nappula): nappulan alue ruudulla
            target (käyttäjän painallus): painalluksen kohde

        Returns:
            bool: jos käyttäjän painallus osuu nappulaan, palautuu True
        """
        horizontal = points[0]-target[0]<=0 and points[0]-target[0]>=-points[2]
        vertical = points[1]-target[1]<=0 and points[1]-target[1]>=-points[3]
        if horizontal and vertical:
            return True
        return False
    def mouse_event(self,pos,stage,player):
        """Tarkistaa käyttäjän painallukset ja niiden seuraamukset

        Args:
            pos (tuple): hiiren painallukset koordinaatit
            stage (kartta-olio): pelikartan antamat tiedot nappuloista
            menus (menu-olio): menujen tilanne,mahdollinen aktivointi ja vaikutus toimintaan
            player (pelaajan hahmo): hahmon tiedot
        """
        for i in stage.buttons:
            if self.activate(i[1],pos):
                if i[0]=="Quit":
                    sys.exit()
                if i[0]=="Attack":
                    self.menu.battle = True
                if i[0]=="Retreat":
                    self.menu.battle = False
                    self.menu.pause = False
                if i[0]=="Inventory":
                    self.menu.inventory = True
                if i[0]=="Close inventory":
                    self.menu.pause = False
                    self.menu.inventory = False
                if i[0]=="Hit the enemy":
                    NonPlayer.active_collision.health -= (player.damage-NonPlayer.active_collision.armour)
                    player.health -= (NonPlayer.active_collision.damage-player.armour)
                    if NonPlayer.active_collision.health<=0:
                        self.menu.battle = False
                        self.menu.pause = False
                    if player.health <= 0:
                        self.menu.activate_menu("Game over")
                self.menu.activate_menu(i[0])
                return
        if not self.menu.pause:
            player.move = True
            player.target = (pos[0]-25,pos[1]-35)
