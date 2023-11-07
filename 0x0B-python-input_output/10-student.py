#!/usr/bin/python3
'''The 9-sudent module'''


class Student:
    '''A student class with only one function'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        x = {}

        if type(attrs) is list:
            for name in attrs:
                if type(name) is not str:
                    return self.__dict__
                else:
                    x[name] = self.__dict__[name]
        else:
            return self.__dict__

        return x
