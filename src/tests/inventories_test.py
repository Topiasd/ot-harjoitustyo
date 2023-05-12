import unittest
from inventories import Inventory
from items import Item

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.consumable = Item("Health potion","Consumable",1,"Healing item",50,200)
        self.active  = Item("Soul stone","Active",0,"Quest",1,"Soul travel")
        self.weapon = Item("Big spoon","Main-hand",60,"Weapon",10)
        self.inventory = Inventory(100)
    def test_use_consumable_effect(self):
        self.inventory.add_item(str(self.consumable))
        heal_amount = self.inventory.equip(str(self.consumable))
        self.assertEqual((heal_amount),self.consumable.power)
    def test_use_consumable_removal(self):
        self.inventory.add_item(str(self.active))
        self.inventory.add_item(str(self.active))
        self.inventory.add_item(str(self.consumable))
        self.inventory.equip(str(self.consumable))
        self.assertEqual((len(self.inventory.contents)),2)
    def test_use_active(self):
        self.inventory.add_item(str(self.active))
        power = self.inventory.equip(str(self.active))
        self.assertEqual((power),self.active.power)
    def test_weight_limit(self):
        self.inventory.add_item(str(self.weapon))
        test = self.inventory.add_item(str(self.weapon))
        self.assertEqual((test),"You are unable to carry more!")
    def test_damage(self):
        self.inventory.add_item(str(self.weapon))
        self.inventory.equip(str(self.weapon))
        self.assertEqual((self.inventory.damage),self.weapon.power)
    def test_remove(self):
        self.inventory.add_item(str(self.weapon))
        self.inventory.remove_item(str(self.weapon))
        self.assertEqual((self.inventory.damage),0)