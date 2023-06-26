#!/usr/bin/python3
"Task 0"
import json


class Base():
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        "Instantiation"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        "Returns the JSON representation of list_dictionaries"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        "Writes the JSON str repr of list_objs to a file"
        file_to_write = f"{cls.__name__}.json"
        to_dict_list = []
        if not list_objs:
            pass
        else:
            for x in range(len(list_objs)):
                to_dict_list.append(list_objs[x].to_dictionary())

        to_write = cls.to_json_string(to_dict_list)

        with open(file_to_write, 'w') as file:
            file.write(to_write)

    @staticmethod
    def from_json_string(json_string):
        "Returns the list of JSON str repr"
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        "Returns an instance with all attrs already set"
        if cls.__name__ == "Rectangle":
            newby = cls(5, 5)
        else:
            newby = cls(5)
        for k, v in dictionary.items():
            setattr(newby, k, v)
        return newby
