from items import Item
class Inventory:
    def __init__(self,size):
        self.contents = []
        self.size = size
        self.total = 0
        self.equiped = {}
        self.armour = 0
        self.damage = 0
    def add_item(self,item):
        if item.weight + self.total <= self.size:
            self.contents.append(item)
            self.contents.sort()
            self.total += item.weight
            return f"Moved {item.name} to inventory"
        return "You are unable to carry more!"
    def remove_item(self,item):
        self.contents.remove(item)
        self.total -= item.weight
        return f"Removed {item.name} from inventory"
    def exchange(self,inventory,item):
        if inventory.total + item.weight <= inventory.total:
            self.remove_item(item)
            inventory.add_item(item)
            return f"Moved {item.name} between inventories"
        return "Not enough space!"
    def _damage(self):
        self.damage = 0
        for i in self.equiped:
            if self.equiped[i].item_type == "Weapon":
                self.damage += self.equiped[i].power
    def _armour(self):
        self.armour = 0
        for i in self.equiped:
            if self.equiped[i].item_type == "Armour":
                self.armour += self.equiped[i].power
    def equip(self,item):
        self.equiped[item.slot]=item
        self._damage()
        self._armour()
        return f"Equipped {item.name} on {item.slot}"
    def info(self):
        text_list = []
        text_list.extend([f"Carrying {self.total} out of {self.size}",
                        f"Damage[{self.damage}]",
                        f"Armour[{self.armour}]"])
        text_list.append("Equipped items:")
        for i in self.equiped:
            text_list.append(f"{self.equiped[i].slot}<--{self.equiped[i].name}")
        text_list.append("All items:")
        for i in self.contents:
            text_list.append(f"{str(i)}")
        text_list.append("Close inventory")
        return text_list

iron_dagger = Item("Iron dagger","Left hand","A weak weapon",5,"Weapon",10)
inv = Inventory(100)
inv.add_item(iron_dagger)
inv.equip(iron_dagger)
