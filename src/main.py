import pygame
from renderer import Render
from sprites import Sprite
from events import Events
from menus import Menu
from entities import Entities
from savefiles import SaveFiles
class Game:
    """Luokka, joka initialisoi kaikki tarpeelliset luokat, ja loopissa hakee tapahtumat ja antaa renderiin ohjeet
    """
    def __init__(self):
        pygame.init()
        self.player = Sprite("robo","robo",None,[Entities.populate(0)])
        self.clock = pygame.time.Clock()
        self.menu = Menu()
        self.events = Events(self.menu)
        self.map = Render(self.menu)
        self.loop()
    def loop(self):
        while True:
            self.map.render(self.player)
            self.events.event_queue(self.player,self.map)
            self.clock.tick(60)
            if self.events.soul_journey == True:
                self.events.soul_journey = False
                data = SaveFiles.load_save(self.player.name)
                self.player = Sprite(self.player.name,"robo",None,[Entities.populate(self.player.progress)])
                self.player.load_player(data)
                self.player.level = [0,0]
                self.map = Render(self.menu,self.player.progress,self.player.boss)
                self.menu.activate_menu("Start game")
            if self.events.restart == True:
                data = SaveFiles.load_save(self.player.name)
                self.player = Sprite(self.player.name,"robo",None,[Entities.populate(self.player.progress)])
                self.player.load_player(data)
                self.player.level = [0,0]
                self.events = Events(self.menu)
                self.map = Render(self.menu)
if __name__ == "__main__":
    Game()
