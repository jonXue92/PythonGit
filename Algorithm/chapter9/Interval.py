# -*- coding: utf-8 -*-

class Interval1:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    # 以下为重写的__lt__方法
    def __lt__(self, other):
        # 当两个Interval比较大小时，直接比较它们的left属性
        return self.left < other.left
    
if __name__ == "__main__":
    A = []
    A.append(Interval1(1, 7))
    A.append(Interval1(5, 6))
    A.append(Interval1(3, 4))
    print("Before sort: ")
    for i in A:
        print("({}, {})".format(i.left, i.right))
    # 由于定义了__lt__方法，此处可以直接调用sort方法进行升序比较
    A.sort()
    print("After sort: ")
    for i in A:
        print("({}, {})".format(i.left, i.right))