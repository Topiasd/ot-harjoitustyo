import pygame
from npc import NonPlayer
class Events:
    def init(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.destination_x = 0
        self.destination_y = 0
    def event_queue(self,player,stage,menus):
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
            if event.type == pygame.MOUSEMOTION:
                self.mouse_x = event.pos[0]
                self.mouse_y = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.move_last = False
                self.destination_x = self.mouse_x
                self.destination_y = self.mouse_y
                player.move_live = True
            if event.type == pygame.MOUSEBUTTONUP:
                player.move_live = False
                self.destination_x = self.mouse_x
                self.destination_y = self.mouse_y
                player.move_last = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menus.close_menu()
                    player.move_last = False
                    player.move_live = False
            if event.type == pygame.QUIT:
                exit()
        
        if player.move_live and not menus.pause:
            player.move_sprite((self.mouse_x-25,self.mouse_y-35))
        if player.move_last and not menus.pause:
            player.move_sprite((self.destination_x-25,self.destination_y-35))
        for i in stage.buttons:
            if self.activate(i[1]):
                menus.activate_menu(i[0])
    def activate(self,points):
        horizontal = points[0]-self.destination_x<=0 and points[0]-self.destination_x>=-points[2]
        vertical = points[1]-self.destination_y<=0 and points[1]-self.destination_y>=-points[3]
        if horizontal and vertical:
            return True
        return False
