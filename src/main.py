import pygame
from renderer import Render
from sprites import Sprite
from events import Events
from menus import Menu
from entities import Entities
class Game:
    """Luokka, joka initialisoi kaikki tarpeelliset luokat, ja loopissa hakee tapahtumat ja antaa renderiin ohjeet
    """
    layout =[
            "############",
            "#XXXXXXXXXXX",
            "#X##X#####X#",
            "#X##X#",
            "#XXXX#",
            "#X####",
            "#X##X#####X#",
            "#XXXXXXXXXX#",
            "############"
        ]
    theme = "meadow"
    def __init__(self):
        pygame.init()
        self.player = Sprite("robo")
        self.clock = pygame.time.Clock()
        self.menus = Menu()
        self.events = Events(self.menus)
        self.map = Render(Game.layout,Game.theme,self.menus)
        Entities.populate(self.player)
        self.loop()
    def loop(self):
        while True:
            self.map.render(self.player)
            self.events.event_queue(self.player,self.map)
            self.clock.tick(60)
            if self.events.soul_journey == True:
                self.events.soul_journey == False
                self.player.level = [0,0]
                self.map = Render(Game.layout,Game.theme,self.menus)
            if self.events.restart == True:
                self.player = Sprite("robo")
                self.player.level = [0,0]
                self.menus = Menu()
                self.events = Events(self.menus)
                self.map = Render(Game.layout,Game.theme,self.menus)
                Entities.populate(self.player)
if __name__ == "__main__":
    Game()
