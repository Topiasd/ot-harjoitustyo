import sys
import pygame
from npc import NonPlayer
class Events:
    def event_queue(self,player,stage,menus):
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
                self.mouse_event(event.pos,stage,menus,player)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menus.activate_menu("Pause")
            if event.type == pygame.QUIT:
                sys.exit()
    def activate(self,points,target):
        horizontal = points[0]-target[0]<=0 and points[0]-target[0]>=-points[2]
        vertical = points[1]-target[1]<=0 and points[1]-target[1]>=-points[3]
        if horizontal and vertical:
            return True
        return False
    def mouse_event(self,pos,stage,menus,player):
        for i in stage.buttons:
            if self.activate(i[1],pos):
                if i[0]=="Quit":
                    sys.exit()
                menus.activate_menu(i[0])
        if not menus.pause:
            player.move = True
            player.target = (pos[0]-25,pos[1]-35)
