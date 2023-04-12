from items import Item
from renderer import RenderList
class Inventory:
    def __init__(self,size):
        self.contents = []
        self.size = size
        self.total = 0
    def add_item(self,item):
        if item.weight + self.total <= self.size:
            self.contents.append(item)
            self.contents = self.contents.sort()
            return f"Moved {item.name} to inventory"
        return "You are unable to carry more!"
    def remove_item(self,item):
        self.contents.remove(item)
        return f"Removed {item.name} from inventory"
    def exchange(self,inventory,item):
        if inventory.total + item.weight <= inventory.total:
            self.remove_item(item)
            inventory.add_item(item)
            return f"Moved {item.name} between inventories"
        return "Not enough space!"
    def drop_stash(self):
        RenderList.add(self)