import pygame
from sprites import Sprite
from areas import Map
class Game:
    def __init__(self):
        self.sprites = []
        self.mouse_x=0
        self.mouse_y=0
        self.destination_x = 0
        self.destination_y = 0
        self.level = [0,0]
        self.triggers = []
        pygame.init()
        self.display = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Adventure(?)")
        self.clock = pygame.time.Clock()
        self.player = Sprite("robo")
        self.sprites.append(self.player)
        self.map = Map()
        self.loop()
    def loop(self):
        while True:
            self.render()
            self.events()
            self.clock.tick(60)
    def render(self):
        area = self.map.level[str(self.level[0])+"x"+str(self.level[1])][0]
        self.triggers = self.map.level[str(self.level[0])+"x"+str(self.level[1])][1]
        for i in area:
                self.display.blit(i[0],(i[1],i[2]))
        for i in self.sprites:
            self.display.blit(i.image,(i.x,i.y))
        pygame.display.flip()
    def events(self):
        area_change = self.player.area_change(self.triggers)
        if area_change != False:
            if area_change == "s":
                self.level[0]+=1
            if area_change == "n":
                self.level[0]-=1
            if area_change == "e":
                self.level[1]+=1
            if area_change == "w":
                self.level[1]-=1
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                self.mouse_x = event.pos[0]
                self.mouse_y = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.move_player_last = False
                self.destination_x = self.mouse_x
                self.destination_y = self.mouse_y
                self.player.move_player_live = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.player.move_player_live = False
                self.destination_x = self.mouse_x
                self.destination_y = self.mouse_y
                self.player.move_player_last = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.move_player_last = False
                    self.player.move_player_live = False
            if event.type == pygame.QUIT:
                exit()
        if self.player.move_player_live:
            self.player.move_sprite((self.mouse_x-25,self.mouse_y-35))
        if self.player.move_player_last:
            self.player.move_sprite((self.destination_x-25,self.destination_y-35))
if __name__ == "__main__":
    Game()
