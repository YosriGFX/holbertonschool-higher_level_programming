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
            list_dictionaries  = []
            return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''from_json_string Static'''
        if not json_string:
            return []
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        '''save_to_file classic'''
        fname = "%s.json" % cls.__name__
        js_objs = []
        if list_objs:
            for _ in list_objs:
                js_objs.append(_.to_dictionary())
        process = open(fname, "w")
        process.write(cls.to_json_string(js_objs))
        process.close()

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
        func = cls.__name__
        dicto = []
        filo = "%s.json" % func
        try:
            proc = open(filo)
            js_dicto = cls.from_json_string(proc.read())
            for ct_dicto in js_dicto:
                dicto.append(cls.create(**ct_dicto))
            return dicto
        except:
            return dicto
        finally:
            proc.close()
