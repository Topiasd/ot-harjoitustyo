from npc import NonPlayer
from items import Item
from interactions import Interactions
#items
iron_dagger = Item("Iron dagger","Left hand","A weak weapon",5,"Weapon",20)
iron_sword = Item("Iron sword","Right hand","A meager weapon",5,"Weapon",30)
wood_bucket = Item("Wooden bucket","Head","Unfashionable",10,"Armour",2)
health_potion = Item("Health potion","Consumable","Feels better than it tastes",1,"Healing item",50)
#monsters
monster = NonPlayer("monster",[1,0],[iron_sword])
chest = NonPlayer("chest",[0,0],[iron_dagger,health_potion],[300,300])
goblin = NonPlayer("goblin",[0,2],[wood_bucket])
#interactions
monster = Interactions("monster","'The spooky specter stares ahead..'",["Attack"])
monsterloot = Interactions("monsterloot","'Something unshiny'",["Scavenge"])
chest = Interactions("chest","'Valuables await within this chest'",["Open chest"])
goblin = Interactions("goblin","'The goblin is green with rage'",["Attack"])
goblinloot = Interactions("goblinloot","'Dare take a closer look at this goblin's sack?'",["Scavenge"])