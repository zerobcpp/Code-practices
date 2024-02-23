class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            
        
        return -1

    def search(self, nums, target):
        l = bisect_left(nums, target)
        if l > len(nums)-1:
            return -1
        if nums[l] == target:
            return l
        return -1