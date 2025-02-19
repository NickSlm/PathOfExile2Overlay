import json
import os 
import sys 

class Config:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        file_path = "config\config.json"
        self.file_name = os.path.join(self.dir_path, file_path)
        with open(self.file_name, "r") as file:
            self.config = json.load(file)
        self.init_config()
    
    def init_config(self):
        database_path = os.path.join(self.dir_path, "data\map_database.json")
        maps_path = os.path.join(self.dir_path, "data\maps.json")
        assets_path = os.path.join(self.dir_path, "assets\icons")
        tesseract_path = os.path.join(self.dir_path, "tesseract.exe")
        new_config = {"database_path": database_path,
                      "maps_path": maps_path,
                      "assets_path": assets_path,
                      "tesseract_path": tesseract_path}
        self.config.update(new_config)
        with open(self.file_name, 'w') as file:
            json.dump(self.config, file, indent=4)
    
    def reload(self):
        with open(self.file_name, 'r') as file:
            self.config = json.load(file)
    
    def get(self, key):
        return self.config[key]
    
    def update(self, new_data):
        with open(self.file_name, 'r') as file:
            config = json.load(file)
        config.update(new_data)
        with open(self.file_name, 'w') as file:
            json.dump(config, file, indent=4)