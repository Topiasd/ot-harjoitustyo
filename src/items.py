class Item:
    all_items = {}
    def __init__(self,name,slot,description,weight,item_type,power,active=None):
        self.name = name
        self.slot = slot
        self.description = description
        self.weight = weight
        self.item_type = item_type
        self.power = power
        self.active = active
        Item.all_items[str(self)]=self
    def activate_item(self):
        if self.power >0:
            self.power -= 1
            return self.active
        return False
    def __str__(self):
        return f"{self.name}: Power[{self.power}] Slot[{self.slot}] Weight[{self.weight}]"

