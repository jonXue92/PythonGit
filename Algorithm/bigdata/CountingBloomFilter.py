# -*- coding: utf-8 -*-

import sys

class CountingBloomFilter:
    def __init__(self, capacity, hash_functions):
        # capacity is the initial size of the SBF
        # it should be as big as possible to contains all of the keys
        self.capacity = capacity
        self.bitset = [0] * capacity
        
        # k hash functions
        self.hash_functions = hash_functions
        
    def add(self, key):
        for func in self.hash_functions:
            position = func(key) % self.capacity
            self.bitset[position] += 1
            
    def contains(self, key):
        count = sys.maxint
        for func in self.hash_functions:
            position = func(key) % self.capacity
            count = min(count, self.bitset[position])
            
        return count