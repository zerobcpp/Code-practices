class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[i] for i in nums]
        
        N = len(nums)
        
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i].append(nums[j])
        
        print(dp)
        return max(dp, key = len)