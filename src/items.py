from inventories import Inventory
class Item:
    """Esineet ja niiden ominaisuudet
    """
    item_list = {}
    def __init__(self,name,slot,weight,item_type,power,value=0):
        self.name = name
        self.slot = slot
        self.weight = weight
        self.item_type = item_type
        self.power = power
        self.value = value
        Inventory.all_items(self)
    def __str__(self):
        if self.slot == "Active":
            if self.power == 1:
                return f"{self.name} [CHARGED]"
            return f"{self.name} [DORMANT]"
        return f"{self.name}: Power[{self.power}] Slot[{self.slot}] Weight[{self.weight}]"
