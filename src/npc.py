from sprites import Sprite
from inventories import Inventory
class NonPlayer:
    npc_id = 0
    npc_list = []
    def __init__(self,name,stats,level,inventory):
        self.id = NonPlayer.npc_id
        npc_id += 1
        NonPlayer.npc_list.append(self.id)
        self.name = name
        self.health = stats[0]
        self.speed = stats[1]
        self.mood = stats[2]
        self.inventory = inventory
        self.level = level
        self.sprite = Sprite(name)
    def remove_npc(self):
        if self.health<=0:
            NonPlayer.npc_list.remove(self.id)
            Inventory.drop_stash(self.inventory)
