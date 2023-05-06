from items import Item
class Inventory:
    global_items = Item.all_items
    def __init__(self,size):
        self.contents = []
        self.size = size
        self.total = 0
        self.equiped = {"Head":None,"Left hand":None,"Right hand":None,"Feet":None,"Body":None,"Arms":None,"Consumable":None}
        self.armour = 0
        self.damage = 0
    def add_item(self,item_info,take=False):
        item = Inventory.global_items[item_info]
        if item.slot == "Active":
            self.contents.append(item)
            self.contents.sort(key=lambda x: x.name, reverse=True)
            return
        if item.weight + self.total <= self.size:
            self.contents.append(item)
            self.contents.sort(key=lambda x: x.name, reverse=True)
            self.total += item.weight
            if self.equiped[item.slot]==None and item.slot is not "Consumable" and take:
                self.equip(str(item))
            return f"Moved {item.name} to inventory"
        return "You are unable to carry more!"
    def remove_item(self,item_info):
        item = Inventory.global_items[item_info]
        self.contents.remove(item)
        self.total -= item.weight
        return f"Removed {item.name} from inventory"
    def exchange(self,inventory,item_info,take=False):
        item = Inventory.global_items[item_info]
        if inventory.total + item.weight <= inventory.size:
            inventory.add_item(str(item),take)
            self.remove_item(str(item))
            return (f"Moved {item.name} between inventories")
        return "Not enough space!"
    def _damage(self):
        self.damage = 0
        for i in self.equiped:
            if self.equiped[i] == None:
                continue
            if self.equiped[i].item_type == "Weapon":
                self.damage += self.equiped[i].power
    def _armour(self):
        self.armour = 0
        for i in self.equiped:
            if self.equiped[i] == None:
                continue
            if self.equiped[i].item_type == "Armour":
                self.armour += self.equiped[i].power
    def equip(self,item_info):
        if item_info not in Inventory.global_items:
            return 0
        item = Inventory.global_items[item_info]
        if item.slot == "Active":
            return item.activate_item()
        if item.slot == "Consumable":
            self.remove_item(str(item))
            return item.power
        self.equiped[item.slot]=item
        self._damage()
        self._armour()
        return 0
    def info(self):
        if self.contents == []:
            return ["Empty!",(self.gap(72)+"Close inventory")]
        text_list = []
        text_list.append(f"Carrying {self.total} out of {str(self.size)+self.gap(25)}Damage[{self.damage}] Armour[{self.armour}]")
        text_list.append("Equipped items:")
        for i in self.equiped:
            if self.equiped[i] == None:
                continue
            text_list.append(f"{self.equiped[i].slot}<--{self.equiped[i].name}")
        text_list.append("All items:")
        for i in self.contents:
            text_list.append(f"{str(i)}")
        text_list.append(" ")
        text_list.append((self.gap(72)+"Close inventory"))
        return text_list
    def gap(self,width):
        return " "*width
    def data(self):
        data = {"equiped":[],"contents":[],"size":self.size}
        for i in self.equiped:
            data["equiped"].append(str(self.equiped[i]))
        for i in self.contents:
            data["contents"].append(str(i))
        return data
    def load_inventory(self,data:dict):
        self.size = data["size"]
        for i in data["contents"]:
            self.add_item(i)
        for i in data["equiped"]:
            self.equip(i)
