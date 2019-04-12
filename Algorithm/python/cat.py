# -*- coding: utf-8 -*-

class Cat(object):
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def mew(self):
        print(self.__name.title() + " mews")
        
    def sit(self):
        print(self.__name.title() + " sit")
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
        
    def set_name(self, age):
        self.__age = age