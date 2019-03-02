# -*- coding: utf-8 -*-

def copy(nums):
    arr = [0]*len(nums)  # 相当于Java中的new int[nums.length]
		for i in range(len(nums)):
        arr[i] = nums[i]
    return arr
		
# 用list comprehension实现同样功能
def copy(nums):
    arr = [x for x in nums]
    return arr
		
# 以下相当于Java中的main函数
if __name__ == "__main__":
    nums = [0]*10
    nums[0] = 1
    new_nums = copy(nums)