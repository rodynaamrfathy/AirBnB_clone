#!/usr/bin/python3
"""convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "storage_file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
         """Sets in __objects the obj with key <obj class name>.id."""
        classname = type(obj).__name__
        FileStorage.__objects ["{}.{}".format(classname, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        for obj in FileStorage.__objects.values():
            obj_dic = obj.to_dict()
            with open(FileStorage.__file_path, 'w') as json_file:
                json.dumps(obj_dic, json_file)


    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        try:
            with open(FileStorage.__file_path) as json_file:
                objects_dict = json.load(json_file)
                for obj in objects_dict:
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(**obj)
        except FileNotFoundError:
            return
