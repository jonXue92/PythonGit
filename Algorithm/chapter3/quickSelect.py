# -*- coding: utf-8 -*-

class QuickSelect:
    def kthSmallest(self, nums, k):
        if not nums or len(nums) < k:
            return -1
        return self.quickSelect(self, nums, 0, len(nums) - 1, k - 1)
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        mid = (start + end) // 2
        pivot = nums[mid]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if start <= k and k <= right:
            return self.quickSelect(nums, start, right, k)
        elif left <= k and k <= end:
            return self.quickSelect(nums, left, end, k)
        else:
            return nums[k]