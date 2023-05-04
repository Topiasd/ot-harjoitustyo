import os
import json
class SaveFiles:
    def load_save(name):
        saves = os.path.dirname(os.path.abspath(__file__))
        save_file = os.path.join(saves,'save_data',name+".json")
        with open(save_file)as file:
            data = json.load(file)
        return data
    def write_save(char_dict,inv_dict):
        full_dict = char_dict | inv_dict
        print (full_dict)
        saves = os.path.dirname(os.path.abspath(__file__))
        save_file = os.path.join(saves,'save_data',char_dict["name"]+".json")
        with open(save_file,"w")as file:
            json.dump(full_dict, file)
