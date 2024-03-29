#!/usr/bin/python3
'''
Create Base class
'''
import json


class Base:
    '''
    Create Init
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Convert to json'''
        if list_dictionaries is None:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''Convert to Dict'''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            new_inst = cls(9)
        else:
            new_inst = cls(9, 9)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        return [cls.create(**dict_instance) for dict_instance in list_dicts]
