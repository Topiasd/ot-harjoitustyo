import pygame
from renderer import Render
from player import Player
from events import Events
class Game:
    def __init__(self):
        pygame.init()
        self.player = Player()
        self.clock = pygame.time.Clock()
        self.map = Render()
        self.loop()
    def loop(self):
        while True:
            Render.render(self.map)
            Events.event_queue(self.player,self.map)
            self.clock.tick(60)
if __name__ == "__main__":
    Game()
