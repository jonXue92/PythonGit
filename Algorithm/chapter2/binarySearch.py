class BinarySearch
    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1
            
        start, end = 0, len(nums) - 1
        # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环，在
        # first position of target 的情况下不会出现死循环，但是在
        # last position of target 的情况下会出现死循环。样例：nums=[1,1] target = 1
        # 为了统一模板，我们就都采用start + 1 < end，就保证不会出现死循环
        while start + 1 < end:
            # python 没有 overflow 的问题，直接//2就可以了
            mid = (start + end) // 2
            # >,=,< 的逻辑先分开写，然后再看看 = 的情况是否能合并到其他分支里
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid
        
        # 如果是找 first position of target 就先看 start, 否则就先看 end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
            
        return -1