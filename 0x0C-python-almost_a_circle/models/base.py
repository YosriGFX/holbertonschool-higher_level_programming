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
        if not list_dictionaries:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''from_json_string Static'''
        if not json_string:
            json_string = '[]'
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        '''save_to_file classic'''
        name = "%s.json" % cls.__name__
        process = open(name, "w")
        if list_objs:
            for en, content in enumerate(list_objs):
                list_objs[en] = cls.to_dictionary(content)
            process.write(cls.to_json_string(list_objs))
        else:
            process.write(cls.to_json_string(None))
        process.close()

    @classmethod
    def create(cls, **dictionary):
        '''create  classic'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
