import pygame
from renderer import Render
from sprites import Sprite
from events import Events
from menus import Menu
class Game:
    def __init__(self):
        pygame.init()
        self.player = Sprite("robo")
        self.clock = pygame.time.Clock()
        self.map = Render()
        self.events = Events()
        self.menus = Menu()
        self.loop()
    def loop(self):
        while True:
            Render.render(self.map,self.player)
            self.events.event_queue(self.player,self.map,self.menus)
            self.clock.tick(60)
if __name__ == "__main__":
    Game()
