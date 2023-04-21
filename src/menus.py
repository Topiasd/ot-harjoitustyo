class Menu:
    active_menu = None
    pause = False
    def __init__(self):
        self.placeholder = "placeholder"
    def activate_menu(self,menu):
        Menu.active_menu = menu
        Menu.pause = True
    def close_menu(self):
        Menu.active_menu = None
        Menu.pause = False
