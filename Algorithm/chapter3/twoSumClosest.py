# -*- coding: utf-8 -*-
import sys

class TwoSumClosest:
    def twoSumClosest(self, nums, target):
        nums.sort()
        i, j = 0, len(nums) - 1
        
        diff = sys.maxsize
        while i < j:
            if nums[i] + nums[j] < target:
                diff = min(diff, target - nums[i] - nums[j])
                i += 1            
            else:
                diff = min(diff, nums[i] + nums[j] - target)
                j -= 1
                
        return diff
                