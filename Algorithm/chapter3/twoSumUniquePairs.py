# -*- coding: utf-8 -*-

class TwoSumUniquePairs:
    def twoSumUniquePairs(self, nums, target):
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        count = 0
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                count += 1
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
        return count