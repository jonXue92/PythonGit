# -*- coding: utf-8 -*-

class Interval2:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
def IntervalKey(interval):
    return interval.left

A = []
A.append(Interval2(1, 7))
A.append(Interval2(5, 6))
A.append(Interval2(3, 4))
print("Before sort: ")
for i in A:
    print("({}, {})".format(i.left, i.right))
A.sort(key = IntervalKey)
print("After sort: ")
for i in A:
    print("({}, {})".format(i.left, i.right))
