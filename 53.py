class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            sub = 0
            for j in range(i, n):
                sub += nums[j]
                res = max(res, sub)
        
        return res