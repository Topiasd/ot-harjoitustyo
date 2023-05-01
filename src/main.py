import pygame
from renderer import Render
from sprites import Sprite
from events import Events
from menus import Menu
class Game:
    """Luokka, joka initialisoi kaikki tarpeelliset luokat, ja loopissa hakee tapahtumat ja antaa renderiin ohjeet
    """
    layout =[
            "#########",
            "#XXXXXXX#",
            "#X##X####",
            "#X##X####",
            "#XXXX####",
            "#########"
        ]
    theme = "meadow"
    def __init__(self):
        pygame.init()
        self.player = Sprite("robo")
        self.clock = pygame.time.Clock()
        self.menus = Menu()
        self.events = Events(self.menus)
        self.map = Render(Game.layout,Game.theme,self.menus)
        self.loop()
    def loop(self):
        while True:
            self.map.render(self.player)
            self.events.event_queue(self.player,self.map)
            self.clock.tick(60)
if __name__ == "__main__":
    Game()
