from level_creator import Creator
class Stage:
    def __init__(self):
        self.roads = {}
        self.roads["e"] = []
        self.roads["w"] = []
        self.roads["s"] = []
        self.roads["n"] = []
        self.roads["middle"] = []
        self.blocks()
        self.asset_dict = {}
        self.level = {}
        stage = Creator()
        stage_code,stage_theme = stage.stage1()[0],stage.stage1()[1]
        counter = [0,0]
        for i in stage_code:
            for j in i:
                self.generator(counter,j,stage_theme)
                counter[1]+=1
            counter[1]=0
            counter[0]+=1
    def generator(self,position,compass,assets):
        background = assets["background"]
        road = assets["road"]
        area = []
        for i in range(100):
            for j in range(100):
                area.append((background,i*13,j*10))
        for i in compass:
            for j in (self.roads[i]):
                area.append((road,j[0]*13,j[1]*10))
        self.level[str(position[0])+"x"+str(position[1])] = (area,compass)
    def blocks(self):
        for i in range(45):
            for j in range(40,55):
                self.roads["w"].append((i,j))
        for i in range(55,100):
            for j in range(40,55):
                self.roads["e"].append((i,j))
        for i in range(40,55):
            for j in range(45):
                self.roads["n"].append((i,j))
        for i in range(40,55):
            for j in range(55,100):
                self.roads["s"].append((i,j))
        for i in range(40,55):
            for j in range(40,55):
                self.roads["middle"].append((i,j))
