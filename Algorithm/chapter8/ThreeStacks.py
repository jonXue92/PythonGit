# -*- coding: utf-8 -*-

# 三个栈交叉，需要用链表的形式连接起来。解法显然适合follow up：假设三个栈不一样大的话？
class ThreeStacks:
    def __init__(self, size):
        self.stackSize = size
        self.stackPointer = [-1, -1, -1]
        self.indexUsed = 0
        self.buffer = [StackNode(-1, -1, -1) for _ in range(size*3)]
        
    def push(self, stackNum, value):
        lastIndex = self.stackPointer[stackNum]
        self.stackPointer[stackNum] = self.indexUsed
        self.indexUsed += 1
        self.buffer = [self.stackPointer[stackNum]] = StackNode(lastIndex, value, -1)
        if lastIndex != -1:
            self.buffer[lastIndex].next = self.stackPointer[stackNum]
            
    def pop(self, stackNum):
        value = self.buffer[self.stackPointer[stackNum]].value
        lastIndex = self.stackPointer[stackNum]
        if lastIndex != self.indexUsed - 1:
            self.swap(lastIndex, self.indexUsed - 1, stackNum)
            
        self.stackPointer[stackNum] = self.buffer[self.stackPointer[stackNum]].prev
        if self.stackPointer[stackNum] != -1:
            self.buffer[self.stackPointer[stackNum]].next = -1
        self.buffer[self.indexUsed - 1] = None
        self.indexUsed -= 1
        return value
    
    def peek(self, stackNum):
        return self.buffer[self.stackPointer[stackNum]].value
    
    def isEmpty(self, stackNum):
        return self.stackPointer[stackNum] == -1
    
    def swap(self, lastIndex, topIndex, stackNum):
        if self.buffer[lastIndex].prev == topIndex:
            self.buffer[lastIndex].value, self.buffer[topIndex].value = self.buffer[topIndex].value, self.buffer[lastIndex].value
            tp = self.buffer[topIndex].prev
            if tp != -1:
                self.buffer[tp].next = lastIndex
            self.buffer[lastIndex].prev = tp
            self.buffer[lastIndex].next = topIndex
            self.buffer[topIndex].prev = lastIndex
            self.buffer[topIndex].next = -1
            self.stackPointer[stackNum] = topIndex
            return
        lp = self.buffer[lastIndex].prev
        if lp != -1:
            self.buffer[lp].next = topIndex
        tp = self.buffer[topIndex].prev
        if tp != -1:
            self.buffer[tp].next = lastIndex
        tn = self.buffer[topIndex].next
        if tn != -1:
            self.buffer[tn].prev = lastIndex
        else:
            for i in range(3):
                if self.stackPointer[i] == topIndex:
                    self.stackPointer[i] = lastIndex
        self.buffer[lastIndex], self.buffer[topIndex] = self.buffer[topIndex], self.buffer[lastIndex]
        self.stackPointer[stackNum] = topIndex
        
class StackNode:
    def __init__(self, p, v, n):
        self.value = v
        self.prev = p
        self.next = n