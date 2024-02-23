class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort() 
        N = len(nums)
        res = 0
        
        for i in range(N):
            new = nums[i] + k
            idx = bisect_right(nums, new)
            res = max(res, idx - i)
        
        return res