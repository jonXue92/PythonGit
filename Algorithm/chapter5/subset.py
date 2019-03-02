# -*- coding: utf-8 -*-

#subset.add(nums[i])
#subsetsHelper(result, subset, nums, i + 1)
#subset.remove(len(size) - 1)
class Subsets:
    
    def subsets(self, nums):
        nums = sorted(nums)
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations
    
    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))
        for i in range(index,len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()
            
    def subsets0(self, nums):
        results = []
        self.search(sorted(nums), 0, [], results)
        return results
    
    def search(self, nums, index, S, results):
        if index == len(nums):
            results.append(list(S))
            return
        self.search(nums, index + 1, S, results)
        S.append(nums[index])
        self.search(nums, index + 1, S, results)
        S.pop()
        
    def subsets1(self, nums):
        results = []
        self.search1(sorted(nums), 0, [], results)
        return results
    
    def search1(self, nums, index, S, results):
        if index == len(nums):
            results.append(S)
            return
        self.search1(nums, index + 1, S + [nums[index]], results)
        self.search1(nums, index + 1, S, results)