class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        rob = [0] * (n+1)
        rob[1] = nums[0]
        
        for i in range(2, n+1):
            rob[i] = max(rob[i-1], rob[i-2] + nums[i-1])
        
        return rob[n]
    
    
    def robcache(self, nums):
        N = len(nums)
        cache = {}
        def helper(i):
            if i >= N:
                return 0
            if i in cache:
                return cache[i]
            skip = helper(i+1)
            take = nums[i] + helper(i+2)
            cache[i] = max(take, skip)
            
            return cache[i]
        
        return helper(0)