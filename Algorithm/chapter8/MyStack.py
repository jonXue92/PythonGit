# -*- coding: utf-8 -*-

class MyStack:
    def __init__(self):
        self.array = []
        
    def push(self, x):
        self.array.append(x)
        
    def pop(self):
        if not self.isEmpty():
            self.array.pop()
            
    def top(self):
        return self.array[-1]
    
    def isEmpty(self):
        return len(self.array) == 0