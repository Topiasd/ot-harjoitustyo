import pygame
from savefiles import SaveFiles
class Menu:
    """Luokka, joka määrittelee eri menujen toiminnot
    """
    def __init__(self):
        """Erilaisten menujen status, ja valittu fontti
        """
        self.menus = {}
        self.menu_list = []
        self.line = 0
        self.active_menu = {}
        self.active_menu["blits"] = []
        self.active_menu["buttons"] = []
        self.main_menu = True
        self.inventory = False
        self.battle = False
        self.pause = False
        self.exchange = False
        self.save_selection = False
        self.font = pygame.font.SysFont("Futura", 50)
        self.prompt = "[Type with keyboard]"
        self.give_prompt = False
        self.species_selection = False
        self.add_all()
        self.activate_menu("Main menu")
    def activate_menu(self,i):
        """Jos kyseiselle ruudun tekstipätkälle liittyy toiminto, se aktivoi oikean menun, tai sulkee sen.
        Args:
            i (string): tekstipätkä joka syötetään funktioon kun sitä painetaan ruudulla
        """
        if i in ["Start game","Continue"]:
            self.pause = False
            self.main_menu = False
            return
        if i not in self.menu_list:
            return
        if i == "Main menu":
            self.main_menu = True
        self.pause = True
        self.initialize_menu(self.menus[i])
    def close_menu(self):
        self.pause = False
    def initialize_menu(self,instruction):
        """Määrittää ohjeen mukaan menun eri toiminnot, ja niiden nappuloiden sijainnit
        Args:
            instruction (tuple): lista toiminnoista, ja niiden haluttu sijainti ruudulla
        """
        self.active_menu["blits"] = []
        self.active_menu["buttons"] = []
        self.line = 0
        pos = instruction[1]
        for j in instruction[0]:
            action = self.font.render(j, True, (0, 0, 0))
            width = action.get_width()
            self.active_menu["blits"].append((action, (pos[0]-width/2, pos[1]+(30*self.line))))
            self.active_menu["buttons"].append((j,(pos[0]-width/2,pos[1]+(30*self.line),width,30)))
            self.line += 1
    def add_menu(self,title,options:list,position:tuple):
        self.menus[title]=(options,position)
        if title not in self.menu_list:
            self.menu_list.append(title)
    def add_all(self):
        center = (640,480)
        self.add_menu("Main menu",["New game","Load save","Tutorial","Quit"],center)
        self.add_menu("Tutorial",["Main menu","Point&Click to move your character",
        "Approach other characters or objects to interact"],center)
        self.add_menu("Attack",["Hit the enemy","Retreat"],center)
        self.add_menu("Pause",["Continue","Save game","Tutorial","Main menu"],center)
        self.add_menu("Game over",["Your valiant robot has perished in battle","Main menu"],center)
        self.add_menu("New game",["Main menu","Select species","Select name","","Start game"],center)
        self.add_menu("Select species",["robo","goblin","monster"],center)
        self.add_menu("Select name",[self.prompt,"Confirm"],center)
        self.add_menu("Load save",SaveFiles.save_list(),center)
    def write_prompt(self,letter):
        center = (640,480)
        if letter == "Backspace":
            self.prompt = self.prompt[:-1]
        elif self.prompt == "[Type with keyboard]":
            self.prompt = letter.upper()
        elif self.prompt == "":
            self.prompt = "[Type with keyboard]"
        else:
            self.prompt += letter
        self.add_menu("Select name",[self.prompt,"Confirm"],center)
        self.activate_menu("Select name")