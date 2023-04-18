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
    def npc_actions(player):
        for i in NonPlayer.npc_list:
            NonPlayer.collision_player(i,player)
    def collision_player(self,player):
        if abs(self.sprite.X-player.player.X)<15 and abs(self.sprite.Y-player.player.Y)<15:
            self.collision = True
        else:
            self.collision = False
enemy = NonPlayer("monster",[0,0])
