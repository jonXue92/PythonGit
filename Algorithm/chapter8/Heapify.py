# -*- coding: utf-8 -*-

import sys
import collections

class Heapify:
    def siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            
            k = father
            
    def upHeapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)
            
    def siftdown(self, A, k):
        while 2 * k + 1 < len(A):
            son = 2 * k + 1
            if 2 * k + 2 < len(A) and A[son] > A[2 * k + 2]:
                son = 2 * k + 2
                
            if A[son] >= A[k]:
                break
            
            A[son], A[k] = A[k], A[son]
            k = son
            
    def downHeapify(self, A):
        for i in range(len(A) - 1, -1, -1):
            self.siftdown(A, i)