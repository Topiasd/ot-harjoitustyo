class Interactions:
    interaction_dict = {}
    def __init__(self,name,greeting,actions=None):
        self.interaction_dict = {}
        self.name = name
        self.hey = greeting
        self.actions = actions
        Interactions.interaction_dict[name]=self
