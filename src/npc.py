from sprites import Sprite
class NonPlayer:
    npc_list = []
    def __init__(self,name,level):
        NonPlayer.npc_list.append(self)
        self.name = name
        self.level = level
        self.health = 100
        self.mood = 100
        self.sprite = Sprite(name)
        self.collision = False
    def remove_npc(self):
        if self.health<=0:
            NonPlayer.npc_list.remove(self.id)
    def npc_actions(self,player):
        NonPlayer.collision_player(self,player)
    def collision_player(self,player):
        x_collision = abs(self.sprite.coordinates[0]-player.coordinates[0])<15
        y_collision = abs(self.sprite.coordinates[1]-player.coordinates[1])<15
        if x_collision + y_collision == 2:
            self.collision = True
        else:
            self.collision = False
enemy = NonPlayer("monster",[0,0])
