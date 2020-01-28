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

    @classmethod
    def save_to_file(cls, list_objs):
        '''save_to_file classic'''
        doc = []
        name = "%s.json" % cls.__name__
        process = open(name, "w")
        if list_objs:
            for content in list_objs:
                doc.append(cls.to_dictionary(content))
            process.write(cls.to_json_string(doc))
        else:
            process.write(doc)
        process.close()
