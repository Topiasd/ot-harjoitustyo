from sprites import Sprite
class NonPlayer:
    """Muiden hahmojen toiminnallisuus
    """
    npc_list = []
    active_collision = None
    def __init__(self,name,level,items,pos=False):
        NonPlayer.npc_list.append(self)
        self.name = name
        self.health = 100
        self.mood = 100
        self.sprite = Sprite(name,items,pos,level)
        self.collision = False
        self.lootname = name+"loot"
        self.inventory = self.sprite.inventory
    def remove_npc(self):
        if self.health<=0:
            self.name = self.lootname
            self.sprite = Sprite("lootbag")
    def npc_actions(self,player):
        """Tähän tulee kaikki eri tekoälyn toiminta, tällä hetkellä vain kollision tarkistus
        Args:
            player (pelaaja): pelaajan hahmon tiedot verrataan toiseen hahmoon.
        """
        if self.sprite.level == player.level:
            self.collision_player(player)
            self.remove_npc()
    def collision_player(self,player):
        x_collision = abs(self.sprite.pos[0]-player.pos[0])<30
        y_collision = abs(self.sprite.pos[1]-player.pos[1])<30
        if x_collision + y_collision == 2:
            NonPlayer.active_collision = self
            self.collision = True
        else:
            self.collision = False
