# -*- coding: utf-8 -*-

def twoSumDifference(self, nums, target):
        # Write your code here
        nums = [(num, i) for i, num in enumerate(nums)]
        target = abs(target)    
        n, indexs = len(nums), []
    
        nums = sorted(nums, key=lambda x: x[0])

        j = 0
        for i in range(n):
            if i == j:
                j += 1
            while j < n and nums[j][0] - nums[i][0] < target:
                j += 1
            if j < n and nums[j][0] - nums[i][0] == target:
                indexs = [nums[i][1] + 1, nums[j][1] + 1]

        if indexs[0] > indexs[1]:
            indexs[0], indexs[1] = indexs[1], indexs[0]

        return indexs
    
#        nums.sort()
#        target = abs(target)
#        j = 1
#        for i in range(len(nums)):
#            while j < len(nums) and nums[j]-nums[i] < target:
#                j += 1
#            if nums[j]-nums[i] == target:
#                # 找到答案