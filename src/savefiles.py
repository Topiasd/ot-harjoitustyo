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
        saves = os.path.dirname(os.path.abspath(__file__))
        save_file = os.path.join(saves,'save_data',char_dict["name"]+".json")
        SaveFiles.update(char_dict["name"])
        with open(save_file,"w")as file:
            json.dump(full_dict, file)
    def update(name):
        saves = os.path.dirname(os.path.abspath(__file__))
        save_collection = os.path.join(saves,'save_data',"save_list.json")
        with open(save_collection)as file:
            data = json.load(file)
            print (data)
        if name in data:
            data.remove(name)
        data.remove("Main menu")
        updated_data = data
        updated_data.append(name)
        updated_data.append("Main menu")
        with open(save_collection,"w")as file:
            json.dump(updated_data, file)