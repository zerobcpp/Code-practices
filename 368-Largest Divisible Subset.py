class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[i] for i in nums]
        
        N = len(nums)
        
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
            
        
        return max(dp, key = len)
#         res = []
        
#         for i in dp:
#             if len(res) < len(i):
#                 res = i
        
#         return res
        