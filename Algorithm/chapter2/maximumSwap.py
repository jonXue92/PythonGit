# -*- coding: utf-8 -*-

class MaximumSwap:
    def maximumSwap(self, num):
        nums = list(str(num))
        buckets = [0] * 10
        for i in range(len(nums)):
            buckets[int(nums[i])] = i
        for i in range(len(nums)):
            for j in range(9, int(nums[i]), -1):
                if buckets[j] > i:
                    nums[i], nums[buckets[j]] = nums[buckets[j]], nums[i]
                    return int("".join(nums))
        return num