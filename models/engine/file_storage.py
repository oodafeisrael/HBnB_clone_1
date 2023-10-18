#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import city
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """A storage engine for AirBnB project
    Class Methods:
        all: Returns object
        new: updates dictionary id
        save: converts python objects into JSON strings
        reload: converts JSON strings into python objects
    Class attributes:
        __file_path: file name to save objects to
        __objects: instantiated objects dictionary
        class_dic: all classes dictionary
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Return the dictionary __objects.'''
        return FileStorage.__objects

    def new(self, obj):

        if obj:
            key = "{}.{}".format(obj.__class__.____name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        '''new __objs to the JSON file.'''

        new_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(new_objs, file)

    def reload(self):

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    cls_name, obj_id = key.split('.')
                    obj_cls = models.class_map[cls_name]
                    obj = obj_cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
