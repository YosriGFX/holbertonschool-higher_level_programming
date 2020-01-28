#!/usr/bin/python3
''' test_base file '''

import unittest
import pep8
import inspect
import json

from models.base import Base


class TestBasePepDocs(unittest.TestCase):
    '''Tests to check docs and style of Base class'''
    @classmethod
    def setUpClass(cls):
        '''Set up for the doc tests'''
        cls.funcs = inspect.getmembers(Base, inspect.isfunction)


    def test_module_docstring(self):
        '''Tests for the module docstring'''
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        '''Tests for the Base class docstring'''
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        '''Tests for the docstrings in all functions'''
        for func in self.funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    '''Tests to check functionality of Base class'''


    def test_no_id(self):
        '''Tests id as None'''
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_set(self):
        '''Tests id as not None'''
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_no_id_after_set(self):
        '''Tests id as None after not None'''
        base2 = Base()
        self.assertEqual(base2.id, 2)



    def test_to_json_string_empty(self):
        '''Check for passing empty list'''
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_to_json_String_None(self):
        '''Tests to_json_string Empty'''
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string_empty(self):
        '''Tests from_json_string with an empty string'''
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_None(self):
        '''Tests from_json_string with an empty string'''
        self.assertEqual([], Base.from_json_string(None))
