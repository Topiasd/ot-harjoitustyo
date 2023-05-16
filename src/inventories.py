from random import choice
class Inventory:
    """Esineiden hallintaa mallintava luokka. Esineiden siirtäminen sisään tai ulos, niiden käyttäminen ja niistä muodostuvat hyödyt hahmoille
    """
    global_items={}
    def __init__(self,size,container=False):
        self.contents = []
        self.size = size
        self.total = 0
        self.equiped = {"Head":None,"Off-hand":None,"Main-hand":None,"Feet":None,"Body":None,"Arms":None,"Consumable":None}
        self.armour = 0
        self.damage = 0
        self.threat = 0
        self.value = 0
        self.container = container
        self.cooldown = False
    def add_item(self,item_info,take=False):
        item = Inventory.global_items[item_info]
        if item.slot == "Active"  or self.container:
            self.contents.append(item)
            self.contents.sort(key=lambda x: (x.slot,x.name), reverse=True)
            return
        if item.weight + self.total <= self.size:
            self.contents.append(item)
            self.contents.sort(key=lambda x: x.name, reverse=True)
            self.total += item.weight
            if self.equiped[item.slot]==None and item.slot is not "Consumable" and take:
                self.equip(str(item))
                return
            if item.slot is not "Consumable" and take and self.equiped[item.slot].power<item.power:
                self.equip(str(item))
        return "You are unable to carry more!"
    def remove_item(self,item_info):
        item = Inventory.global_items[item_info]
        if item in self.contents and not self.cooldown:
            self.contents.remove(item)
            self.total -= item.weight
            self.cooldown = True
        if item == self.equiped[item.slot]:
            self.equiped[item.slot]=None
        return 0
    def exchange(self,inventory,item_info,take=False):
        if item_info not in Inventory.global_items:
            return
        item = Inventory.global_items[item_info]
        if item.item_type == "Quest":
            return
        if inventory.total + item.weight <= inventory.size:
            inventory.add_item(str(item),take)
            self.remove_item(str(item))
            self.cooldown = False
            return (f"Moved {item.name} between inventories")
        return "Not enough space!"
    def _damage(self):
        self.damage = 0
        for i in self.equiped:
            if self.equiped[i] == None:
                continue
            if self.equiped[i].item_type == "Weapon":
                self.damage += self.equiped[i].power
        return self.damage
    def _armour(self):
        self.armour = 0
        for i in self.equiped:
            if self.equiped[i] == None:
                continue
            if self.equiped[i].item_type == "Armour":
                self.armour += self.equiped[i].power
        return self.armour
    def equip(self,item_info,charge=0):
        if item_info not in Inventory.global_items:
            return 0
        item = Inventory.global_items[item_info]
        if item.slot == "Active":
            item.power += charge
            if item.power>1:
                item.power = 1
            return item.power
        if item.slot == "Consumable":
            self.remove_item(str(item))
            return item.power
        self.equiped[item.slot]=item
        self._threat()
        return 0
    def info(self,menu): 
        if menu==False:
            return ["Closed"]
        if self.contents == []:
            return ["Empty!","Close inventory"]
        text_list = []
        text_list.append(f"Carrying {self.total} out of {str(self.size)+self.gap(10)}Damage[{self.damage}] Armour[{self.armour}]")
        text_list.append("Equipped items:")
        for i in self.equiped:
            if self.equiped[i] == None:
                continue
            text_list.append(f"{self.equiped[i].slot}<--{self.equiped[i].name} Power[{self.equiped[i].power}]")
        last = None
        quantity = 1
        text_list.append(menu)
        if menu != "All items":
            for i in self.contents:
                if i.item_type==menu:
                    if i.name == "Soul stone":
                        text_list.append(str(i))
                        continue
                    if last==None:
                        last=i
                        continue
                    if i == last:
                        quantity+=1
                        continue
                    text_list.append(f"{str(last)} Quantity[{quantity}]")
                    quantity = 1
                    last = i
            if last != None:
                text_list.append(f"{str(last)} Quantity[{quantity}]")
            elif menu== "Quest":
                pass
            else:
                text_list.append(f"None owned")
        text_list.append(" ")
        for i in ("All items","Weapon","Armour","Healing item","Quest"):
            if i != menu:
                text_list.append(i)
        text_list.append(" ")
        text_list.append("Close inventory")
        return text_list
    def ext_info(self):
        text_list = []
        if self.contents == []:
            return ["Empty!","Close inventory"]
        for i in self.contents:
            text_list.append(str(i))
        text_list.append("Close inventory")
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
            if "Soul stone" in i:
                continue
            self.add_item(i)
        for i in data["equiped"]:
            self.equip(i)
    def generate(self,power_level):
        possible = {}
        for i in ["Healing item","Weapon","Armour"]:
            possible[i]=[]
        value = 0
        for i in Inventory.global_items:
            item = Inventory.global_items[i]
            if item.item_type is not "Quest":
                if item.item_type == "Armour":
                    if item.power<(power_level*20):
                        possible[item.item_type].append(item)
                if item.item_type == "Weapon":
                    if item.power<(power_level*20):
                        possible[item.item_type].append(item)
                if item.item_type == "Healing item":
                    if item.power<(power_level*10):
                        possible[item.item_type].append(item)
        weapons = possible["Weapon"]
        armours = possible["Armour"]
        heals = possible["Healing item"]
        while True:
            if len(self.contents)>4 or value>power_level*200:
                break
            item = choice([choice(weapons),choice(armours),choice(heals)])
            if item in self.contents:
                continue
            if item.value + value < power_level*300:
                if item.item_type == "Healing item":
                    self.add_item(str(item))
                else:
                    self.add_item(str(item),True)
                value += item.value
    def _threat(self):
        self.threat = self._damage()+self._armour()
        return self.threat
    def _value(self):
        self.value = 0
        for i in self.contents:
            if i.slot == "Consumable":
                self.value += i.power
        return self.value
    def all_items(item):
        Inventory.global_items[str(item)]=item
