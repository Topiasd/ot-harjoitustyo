from npc import NonPlayer
from items import Item
from interactions import Interactions
from inventories import Inventory

class Entities:
    def populate(progress):
        NonPlayer.active_collision = None
        NonPlayer.npc_list = []
        #items
        soul_stone = Item("Soul stone","Active",0,"Quest",0,"Soul travel")
        soul_stone1 = Item("Soul stone","Active",0,"Quest",1,"Soul travel")
        health_potion = Item("Health potion","Consumable",1,"Healing item",50,200)
        #monsters
        chest = NonPlayer("chest","Container",[0,0],progress+2,[300,300],True)
        portal = NonPlayer("portal","Container",[0,0],[],[600,450],True)
        #interactions
        monster = Interactions("monster","'The spooky spectre stares ahead..'",["Attack"])
        monsterloot = Interactions("monsterloot","'Something unshiny'",["Scavenge"])
        chest = Interactions("chest","'Valuables await within this chest'",["Open chest"])
        goblin = Interactions("goblin","'The goblin is green with rage'",["Attack"])
        goblinloot = Interactions("goblinloot","'Dare take a closer look at this goblin's sack?'",["Scavenge"])
        robo = Interactions("robo","'A little bit threatening..'",["Attack"])
        roboloot = Interactions("roboloot","'Power lost'",["Scavenge"])
        portal = Interactions("portal","'The soul portal requires a sacrifice'",["Soul travel"])
        return soul_stone
materials = {"Wood":2,"Stone":3,"Iron":5,"Steel":10,"Silver":20,"Gold":30,"Diamond":45,"Meteorite":70,"Dark matter":100,"Dying star":150}
off_hand_weapons = {"knife":1,"dagger":2,"hammer":3,"hatchet":4,"club":5,"shortsword":6,"axe":7}
main_hand_weapons = {"sword":15,"longsword":25,"spear":30,"longsword":40,"battleaxe":60,"warhammer":80,"flail":35,"halberd":50,"greatsword":70}
armour_types = {"gauntlets":(1,"Arms"),"helmet":(3,"Head"),"greaves":(2,"Feet"),"cuirass":(4,"Body")}
for i in materials:
    for j in off_hand_weapons:
        Item(f"{i} {j}","Off-hand",materials[i]*off_hand_weapons[j]//2,"Weapon",materials[i]*off_hand_weapons[j]*2,(materials[i]*off_hand_weapons[j])**2)
    for j in main_hand_weapons:
        Item(f"{i} {j}","Main-hand",materials[i]*main_hand_weapons[j],"Weapon",materials[i]*main_hand_weapons[j]*2,(materials[i]*main_hand_weapons[j])**2)
    for j in armour_types:
        Item(f"{i} {j}",armour_types[j][1],materials[i]*armour_types[j][0],"Armour",materials[i]*armour_types[j][0]*2,(materials[i]*armour_types[j][0])**3)
food = {"Apple":1,"Pear":2,"Banana":3,"Watermelon":4}
form = {"[rotten]":1,"[raw]":3,"[ripe]":5,"juice":10,"smoothie":20,"pie":30,"cake":40}
for i in food:
    for j in form:
        Item(f"{i}{j}","Consumable",1,"Healing item",food[i]*form[j],food[i]*form[j]**2)
