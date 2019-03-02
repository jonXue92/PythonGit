# -*- coding: utf-8 -*-

class Permute2:
    def permute(self, nums):
        nums.sort()
        result = []
        if nums == None:
            return result
        hasNext = True
        while hasNext:
            current = list(nums)
            result.append(current)
            hasNext = self.nextPermutation(nums)
            
        return result
    
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return False
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            return False
        j = n - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[j], nums[i - 1] = nums[i - 1], nums[j]
        self.swapList(nums, i, n - 1)
        return True
    
    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1