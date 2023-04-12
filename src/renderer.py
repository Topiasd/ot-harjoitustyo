class RenderList:
    npc_list = []
    inventory_list = []
    def add_npc(npc):
        RenderList.npc_list.append(npc)
    def add_stash(inventory):
        RenderList.inventory_list.append(inventory)