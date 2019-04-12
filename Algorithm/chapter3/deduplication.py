# -*- coding: utf-8 -*-

class Deduplication:
    def deduplication(self, nums):
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        result = 1
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
        return result
    
    def deduplication2(self, nums):
        d = set()
        result = 0
        for num in nums:
            if num not in d:
                d.add(num)
                nums[result] = num
                result += 1
        return result