from items import Item

class Interactions:
    interaction_dict = {}
    def item_interaction(items: list):
        items = items.sort()
        if items == ["key","lock"]:
            return ["The lock opens"]
    def char_interaction(character):
        return(character,Interactions.interaction_dict[character.name])



Interactions.interaction_dict["monster"]=["Hello"]


