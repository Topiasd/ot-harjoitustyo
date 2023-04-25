import pygame
class Menu:
    menus = {}
    def __init__(self):
        self.active_menu = {}
        self.pause = False
        self.font = pygame.font.SysFont("Futura", 50)
    def activate_menu(self,i):
        if i in ["Start","Continue"]:
            self.pause = False
        if i not in Menu.menus:
            return
        self.pause = True
        self.initialize_menu(Menu.menus[i])
    def close_menu(self):
        self.pause = False
    def initialize_menu(self,instruction):
        self.active_menu["blits"] = []
        self.active_menu["buttons"] = []
        line = 0
        pos = instruction[1]
        for j in instruction[0]:
            action = self.font.render(j, True, (0, 0, 0))
            width = action.get_width()
            self.active_menu["blits"].append((action, (pos[0]-width/2, pos[1]+(30*line))))
            self.active_menu["buttons"].append((j,(pos[0]-width/2,pos[1]+(30*line),width,30)))
            line += 1
    center = (640,480)
    menus["Main menu"]=(["Start","Tutorial","Quit"],center)
    menus["Tutorial"]=(["Main menu","Point&Click to move your character",
    "Approach other characters or objects to interact"],center)
    menus["Attack"]=(["Not quite ready yet"],center)
    menus["Chat"]=(["Not quite ready yet"],center)
    menus["Pause"]=(["Continue","Tutorial","Main menu"],center)