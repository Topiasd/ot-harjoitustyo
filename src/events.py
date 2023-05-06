import sys
import pygame
from npc import NonPlayer
from savefiles import SaveFiles
from string import ascii_letters
class Events:
    """Tapahtumat (hiiren painallukset) ja niistä seuraavat tilannemuutokset löytyvät täältä
    """
    def __init__(self,menu):
        self.menu = menu
        self.restart = False
        self.soul_journey = False
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
                self.key_event(player,event)
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
    def key_event(self,player,key):
        if key.scancode == 41 and self.menu.main_menu == False:
            self.menu.activate_menu("Pause")
            return
        if key.scancode == 28 and self.menu.give_prompt == True:
            player.name = self.menu.prompt
            self.menu.prompt = "[Type with keyboard]"
            self.menu.give_prompt = False
            self.menu.activate_menu("New game")
        if key.scancode == 42 and len(self.menu.prompt)>0:
            self.menu.write_prompt("Backspace")
        if str(key.unicode) in ascii_letters:
            self.menu.write_prompt(str(key.unicode))
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
                if self.menu.save_selection==True:
                    if i[0] != "Main menu":
                        data = SaveFiles.load_save(i[0])
                        player.load_player(data)
                        self.menu.main_menu = False
                    self.menu.save_selection=False
                    self.menu.activate_menu("Start game")
                if self.menu.inventory:
                    if "Close inventory" in i[0]:
                        self.menu.pause = False
                        self.menu.inventory = False
                        return
                    if player.inventory.equip(i[0]) == "Soul journey":
                        print ("asd")
                        SaveFiles.write_save(player.data(),player.inventory.data())
                        self.soul_journey = True
                    player.health += player.inventory.equip(i[0])
                    if player.health > player.max_health:
                        player.health = player.max_health
                if self.menu.exchange:
                    if "Close inventory" in i[0] or "Scavenge" in i[0] or "Open chest" in i[0]:
                        self.menu.pause = False
                        self.menu.exchange = False
                        return
                    if "*" in i[0]:
                        i = i[0].replace("*","")
                        NonPlayer.active_collision.inventory.exchange(player.inventory,i,True)
                        return
                    player.inventory.exchange(NonPlayer.active_collision.inventory,i[0])
                if i[0]=="Scavenge" or i[0]=="Open chest":
                    self.menu.exchange = True
                if i[0]=="Select name":
                    self.menu.prompt = "[Type with keyboard]"
                    self.menu.give_prompt = True
                if i[0]=="Quit":
                    sys.exit()
                if i[0]=="Attack":
                    player.update_stats()
                    NonPlayer.active_collision.sprite.update_stats()
                    self.menu.battle = True
                if i[0]=="Retreat":
                    self.menu.battle = False
                    self.menu.pause = False
                if i[0]=="Inventory":
                    self.menu.inventory = True
                if i[0]=="Save game":
                    SaveFiles.write_save(player.data(),player.inventory.data())
                if i[0]=="Load save":
                    self.menu.save_selection=True
                if self.menu.species_selection == True:
                    player.update_image(i[0])
                    self.menu.species_selection = False
                    self.menu.activate_menu("New game")
                if i[0]=="Select species":
                    self.menu.species_selection = True
                if self.menu.give_prompt == True:
                    if i[0]=="Confirm" and self.menu.prompt is not "[Type with keyboard]":
                        player.name = self.menu.prompt
                        self.menu.prompt = "[Type with keyboard]"
                        self.menu.give_prompt = False
                        self.menu.activate_menu("New game")
                if i[0]=="Hit the enemy":
                    if player.damage > NonPlayer.active_collision.sprite.armour:
                        NonPlayer.active_collision.health -= (player.damage-NonPlayer.active_collision.sprite.armour)
                    if player.armour < NonPlayer.active_collision.sprite.damage:
                        player.health -= (NonPlayer.active_collision.sprite.damage-player.armour)
                    if NonPlayer.active_collision.health<=0:
                        self.menu.battle = False
                        self.menu.pause = False
                    if player.health <= 0:
                        self.restart = True
                self.menu.activate_menu(i[0])
                return
        if not self.menu.pause:
            player.move = True
            player.target = (pos[0]-25,pos[1]-35)
