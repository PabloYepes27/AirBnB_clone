#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances
"""
import os
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    Summary: Definning the class to store the data and make it persistant:
        __file_path -> Private class attribute
        __objects -> Private class attribute
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="UTF8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="UTF8") as file:
                json_dict = json.load(file)
            for key, value in json_dict.items():
                class_name = key.split(".")
                FileStorage.__objects[key] = globals()[class_name[0]](**value)

        except Exception:
            pass
