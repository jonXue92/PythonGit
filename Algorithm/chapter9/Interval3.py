# -*- coding: utf-8 -*-

class Interval3:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return "Interval(%d, %d)" % (self.left, self.right)
    
data = [(3, 2),(3, 1),(2, 7),(1, 5),(2, 6),(1, 7)]
intervals = [Interval3(left, right) for left, right in data]

print(sorted(intervals, key = lambda i: (i.left, i.right)))
print(sorted(intervals, key = lambda i: (-i.left, i.right)))
print(sorted(intervals, key = lambda i: (i.right, i.left)))
print(sorted(intervals, key = lambda i: (-i.right, i.left)))