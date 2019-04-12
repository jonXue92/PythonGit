# -*- coding: utf-8 -*-

class KClosetNumbers:
    def kClosetNumbers(self, A, target, k):
        # 找到A[left] < target, A[right] >= target
        right = self.find_upper_closet(A, target)
        left = right - 1
        results = []
        for _ in range(k):
            if self.is_left_closer(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        return results
    
    def find_upper_closet(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        
        # 找不到的情况下
        return end + 1
    
    def is_left_closer(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target