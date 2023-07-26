#!/usr/bin/python3
""" file storage model """
import json
import os
from datetime import datetime


class FileStorage:
    """class storage """
    __file_name = "file.json"
    __object = {}

    def new(self, obj):
        """serializes newly created Users"""
        key = "{}.{}".format(obj.user_name, obj.password)
        FileStorage.__object[key] = obj

    def all(self):
        """return all objects in __objects"""
        return FileStorage.__object

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in FileStorage.__object.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_name, "w", encoding="utf-8") as f:
                json.dump(obj_dict, f)

    def classes(self):
        from models.base_model import BaseModel
        from models.register import Register
        classes = {
                "BaseModel": BaseModel,
                "Register": Register
                }
        return classes
