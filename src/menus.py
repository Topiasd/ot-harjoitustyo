import pygame
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
        self.battle = False
        self.pause = False
        self.font = pygame.font.SysFont("Futura", 50)
        self.add_all()
        self.activate_menu("Main menu")
    def activate_menu(self,i):
        """Jos kyseiselle ruudun tekstipätkälle liittyy toiminto, se aktivoi oikean menun, tai sulkee sen.
        Args:
            i (string): tekstipätkä joka syötetään funktioon kun sitä painetaan ruudulla
        """
        if i in ["Start","Continue"]:
            self.pause = False
            return
        if i not in self.menu_list:
            return
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
        self.menu_list.append(title)
    def add_all(self):
        print ("asd")
        center = (640,480)
        self.add_menu("Main menu",["Start","Tutorial","Quit"],center)
        self.add_menu("Tutorial",["Main menu","Point&Click to move your character",
        "Approach other characters or objects to interact"],center)
        self.add_menu("Attack",["Hit the enemy","Retreat"],center)
        self.add_menu("Pause",["Continue","Tutorial","Main menu"],center)
        self.add_menu("Game over",["Your valiant robot has perished in battle","Main menu"],center)
        self.add_menu("Chat",["Not quite ready yet"],center)