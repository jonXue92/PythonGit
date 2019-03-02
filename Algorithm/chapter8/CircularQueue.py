# -*- coding: utf-8 -*-

class CircularQueue:
    def __init__(self, n):
        self.circularArray = [0] * n
        self.front = 0
        self.rear = 0
        self.size = 0
        
    def isFull(self):
        return self.size == len(self.circularArray)
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, element):
        if self.isFull():
            raise RuntimeError("Queue is already Full")
        self.rear = (self.front + self.size) % len(self.circularArray)
        self.circularArray[self.rear] = element
        self.size += 1
        
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Queue is already Empty")
        ele = self.circularArray[self.front]
        self.front = (self.front + 1) % len(self.circularArray)
        self.size -= 1
        return ele