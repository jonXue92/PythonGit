# -*- coding: utf-8 -*-

class FindMedianSortedArrays:
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, n // 2 + 1)
        else:
            smaller = self.findKth(A, B, n // 2)
            bigger = self.findKth(A, B, n // 2 + 1)
            return (smaller + bigger) / 2
        
    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        a = A[k // 2 - 1] if len(A) >= k // 2 else None
        b = B[k // 2 - 1] if len(B) >= k // 2 else None
        if b is None or (a is not None and a < b):
            return self.findKth(A[k // 2:], B, k - k // 2)
        return self.findKth(A, B[k // 2:], k - k // 2)
    
    def findMedianSortedArrays0(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth0(A, B, n // 2 + 1)
        else:
            smaller = self.findKth0(A, B, n // 2)
            bigger = self.findKth0(A, B, n // 2 + 1)
            return (smaller + bigger) / 2
    
    def findKth0(self, A, B, k):
        if len(A) == 0:
            left, right = B[0], B[-1]
        elif len(B) == 0:
            left, right = A[0], A[-1]
        else:
            left, right = min(A[0], B[0]), max(A[-1], B[-1])
        while left + 1 < right:
            mid = (left + right) // 2
            count1 = self.helper(A, mid)
            count2 = self.helper(B, mid)
            if count1 + count2 < k:
                left = mid
            else:
                right = mid
        count1 = self.helper(A, left)
        count2 = self.helper(B, left)
        if count1 + count2 >= k:
            return left
        else:
            return right
        
    def helper(self, array, flag):
        if len(array) == 0:
            return 0
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] <= flag:
                left = mid
            else:
                right = mid
        if array[right] <= flag:
            return right + 1
        if array[left] <= flag:
            return left + 1
        return 0