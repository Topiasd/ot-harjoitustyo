class Item:
    def __init__(self,name,slot,description,weight,item_type,power):
        self.name = name
        self.slot = slot
        self.description = description
        self.weight = weight
        self.item_type = item_type
        self.power = power
    def __str__(self):
        return f"{self.name}: Power[{self.power}] Slot[{self.slot}] Weight[{self.weight}] Type[{self.item_type}]]"
