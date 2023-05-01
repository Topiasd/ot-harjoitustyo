from sprites import Sprite
class NonPlayer:
    """Muiden hahmojen toiminnallisuus
    """
    npc_list = []
    active_collision = None
    def __init__(self,name,level):
        NonPlayer.npc_list.append(self)
        self.name = name
        self.level = level
        self.health = 100
        self.mood = 100
        self.damage = 10
        self.armour = 5
        self.sprite = Sprite(name)
        self.collision = False
    def remove_npc(self):
        if self.health<=0:
            NonPlayer.npc_list.remove(self)
    def npc_actions(self,player):
        """Tähän tulee kaikki eri tekoälyn toiminta, tällä hetkellä vain kollision tarkistus
        Args:
            player (pelaaja): pelaajan hahmon tiedot verrataan toiseen hahmoon.
        """
        NonPlayer.collision_player(self,player)
        self.remove_npc()
    def collision_player(self,player):
        x_collision = abs(self.sprite.pos[0]-player.pos[0])<15
        y_collision = abs(self.sprite.pos[1]-player.pos[1])<15
        if x_collision + y_collision == 2:
            NonPlayer.active_collision = self
            self.collision = True
        else:
            self.collision = False
enemy = NonPlayer("monster",[1,0])
