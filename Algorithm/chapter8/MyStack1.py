# -*- coding: utf-8 -*-

class ThreeStacks1:
    def __init__(self, size):
        self.stackSize = size
        self.threeStack = [None] * (size * 3)
        self.stackPointer = [0, size, 2 * size]
        
    def push(self, stackNum, value):
        self.threeStack[self.stackPointer[stackNum]] = value
        self.stackPointer[stackNum] += 1
        
    def pop(self, stackNum):
        popItem = self.threeStack[self.stackPointer[stackNum] - 1]
        self.stackPointer[stackNum] -= 1
        return popItem
    
    def peek(self, stackNum):
        return self.threeStack[self.stackPointer[stackNum] - 1]
    
    def isEmpty(self, stackNum):
        return self.stackPointer[stackNum] == self.stackSize * stackNum