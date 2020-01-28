#!/usr/bin/python3
'''base file'''
import json


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Base __init__'''
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''to_json_string Static'''
        if list_dictionaries:
            return (json.dumps(list_dictionaries))
        else:
            return (json.dumps([]))

    @staticmethod
    def from_json_string(json_string):
        '''from_json_string Static'''
        if not json_string:
            return []
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        '''save_to_file classic'''
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            for i in list_objs:
                json_list.append(i.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @classmethod
    def create(cls, **dictionary):
        '''create  classic'''
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''load_from_file function'''
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_list = cls.from_json_string(file.read())
                obj_list = []
                for i in json_list:
                    obj_list.append(cls.create(**i))
                return obj_list
        except:
            return []
