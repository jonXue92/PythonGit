# -*- coding: utf-8 -*-
class MatrixMListNode(object):
    def __init__(self,row,col,value):
        self.row=row
        self.col=col
        self.value=value
        self.nextCol=None
        self.nextRow=None

#使用多重链表实现的稀疏矩阵的迭代可分为按行迭代和按列迭代。
class _SparseMatrixIterator(object):
    def __init__(self,rowArray):
        self._rowArray=rowArray
        self._curRow=0#第一个含有非零元素的行
        self._curNode=None#该行内的第一个非零元素
        self._findNextElement()
    
    def __iter__(self):
        return self
    
    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            value=self._curNode.value
            self._curNode=self._curNode.next
            if self._curNode is None:#此时一行遍历结束
                self._findNextElement()#使用辅助方法寻找下一个含非零元素的行。
            return value
        
    #辅助方法，寻找下一个含非零元素的行
    def _findNextElement(self):
        i=self._curRow
        while i < len(self._rowArray) and self._rowArray[i] is None:#寻找下一个含有非零元素的行
            i+=1
        self._curRow=i
        if i < len(self._rowArray):
            self._curNode=self._rowArray[i]
        else:
            self._curNode=None