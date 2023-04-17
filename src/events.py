import pygame
from renderer import Render
from player import Player
from npc import NonPlayer
class Events:
    mouse_x = 0
    mouse_y = 0
    destination_x = 0
    destination_y = 0
    def event_queue(player,map):
        NonPlayer.npc_actions(player)
        area_change = player.player.area_change(map.triggers)
        if area_change != False:
            if area_change == "s":
                map.level[0]+=1
            if area_change == "n":
                map.level[0]-=1
            if area_change == "e":
                map.level[1]+=1
            if area_change == "w":
                map.level[1]-=1
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                Events.mouse_x = event.pos[0]
                Events.mouse_y = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.player.move_last = False
                Events.destination_x = Events.mouse_x
                Events.destination_y = Events.mouse_y
                player.player.move_live = True
            if event.type == pygame.MOUSEBUTTONUP:
                player.player.move_live = False
                Events.destination_x = Events.mouse_x
                Events.destination_y = Events.mouse_y
                player.player.move_last = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.player.move_last = False
                    player.player.move_live = False
            if event.type == pygame.QUIT:
                exit()
        if player.player.move_live:
            player.player.move_sprite((Events.mouse_x-25,Events.mouse_y-35))
        if player.player.move_last:
            player.player.move_sprite((Events.destination_x-25,Events.destination_y-35))
        