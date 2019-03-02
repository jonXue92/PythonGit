# -*- coding: utf-8 -*-

from collections import deque

class Subsets2:
    def subsets(self, nums):
        result = []
        n = len(nums)
        nums.sort()
        # 1 << n is 2^n
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result
    
    def subsets0(self, nums):
        results = []
        if not nums:
            return results
        nums.sort()
        # BFS
        queue = deque()
        queue.append([])
        while queue:
            subset = queue.popleft()
            results.append(subset)
            for i in range(len(nums)):
                if not subset or subset[-1] < nums[i]:
                    newSubset = list(subset)
                    newSubset.append(nums[i])
                    queue.append(newSubset)
                    
        return results