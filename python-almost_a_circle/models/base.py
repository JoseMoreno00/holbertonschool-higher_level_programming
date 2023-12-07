#!/usr/bin/python3
"""
Define a class

{Base}

class Base have:
    a private class atribute {__nb_objects}
    a function init, recive a integer value {id}
        set a public instance id whit the value recived ; Otherwise set
        value to private class atribute {__nb_objects}

"""
import json
from os.path import exists


class Base:
    """Define the func to set a public instance id"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that return the json string
        representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that that writes the JSON string representation
        of list_objs to a file"""
        LaliSta = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            if list_objs is None:
                pass
            else:
                for listi in list_objs:
                    LaliSta.append(listi.to_dictionary())
            file.write(cls.to_json_string(LaliSta))

    @staticmethod
    def from_json_string(json_string):
        """Function that returns the list of the JSON string representation
        json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance
        with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances"""
        file_name = cls.__name__ + ".json"
        if exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                json_string = file.read()
                dictionaryes = cls.from_json_string(json_string)
                return [cls.create(**dictionary)
                        for dictionary in dictionaryes]
        else:
            return []
