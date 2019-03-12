# -*- coding: utf-8 -*-

class StandardBloomFilter:
    def __init__(self, capacity, hash_functions):
        # capacity is the initial size of the SBF
        # it should be as big as possible to contains all of the keys
        self.capacity = capacity
        self.bitset = [False] * capacity
        
        # k hash functions
        self.hash_functions = hash_functions
    
    def add(self, key):
        for func in self.hash_functions:
            position = func(key) % self.capacity
            self.bitset[position] = True
            
    def contains(self, key):
        for func in self.hash_functions:
            position = func(key) % self.capacity
            if self.bitset[position] is False:
                return False
        return True
        