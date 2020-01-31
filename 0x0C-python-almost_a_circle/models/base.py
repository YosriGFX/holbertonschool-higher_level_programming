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
        try:
            func = cls.__name__
            dicto = []
            filo = "%s.json" % func
            proc = open(filo)
            js_dicto = cls.from_json_string(proc.read())
            for ct_dicto in js_dicto:
                dicto.append(cls.create(**ct_dicto))
            return dicto
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv
        Args:
            list
        Returns:
            (list) of Rectangles/Squares in csv
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for r in list_objs:
                    csv_writer.writerow([r.id, r.width, r.height,
                                         r.x, r.y])
            elif cls.__name__ is "Square":
                for s in list_objs:
                    csv_writer.writerow([s.id, s.size, s.x, s.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv
        Args:
            None
        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        obj = cls.create(**{"id": int(args[0]),
                                            "width": int(args[1]),
                                            "height": int(args[2]),
                                            "x": int(args[3]),
                                            "y": int(args[4])})
                    elif cls.__name__ is "Square":
                        obj = cls.create(**{"id": int(args[0]),
                                            "size": int(args[1]),
                                            "x": int(args[2]),
                                            "y": int(args[3])})

                    obj_list.append(obj)
        except Exception:
            return obj_list
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list of Rectangles)
            list_squares (list of squares)
        Returns:
            None
        """
        for i in list_rectangles:
            t = turtle.Turtle()
            t.speed(0.7)
            t.penup()
            t.setpos(i.x, i.y)
            t.pendown()
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
        for i in list_squares:
            t = turtle.Turtle()
            t.speed(0.7)
            t.penup()
            t.setpos(i.x, i.y)
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.forward(i.size)
                t.left(90)
