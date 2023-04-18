class Creator:
    def __init__(self):
        self.map_list = []
    def create(self,level):
        i=1
        j=1
        level_code = []
        while i < len(level):
            layer = []
            while j < len(level[i]):
                layout = ""
                if level[i][j] == "X":
                    if level[i][j+1]=="X":
                        layout += "e"
                    if level[i-1][j]=="X":
                        layout += "n"
                    if level[i+1][j]=="X":
                        layout += "s"
                    if level[i][j-1]=="X":
                        layout += "w"
                layer.append(layout)
                j += 3
            level_code.append(layer)
            i += 3
            j = 1
        return level_code 
    def stage1(self):
        return  self.create([
            "#########",
            "#XXXXXXX#",
            "#X##X####",
            "#X##X####",
            "#XXXX####",
            "#########"
        ])
