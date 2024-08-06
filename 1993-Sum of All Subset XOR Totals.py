class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        res = []
        arr = [] 
        
        def helper(start, end):
            if len(arr) == end:
                res.append(arr[:])
            
            for i in range(start, N):
                arr.append(nums[i])
                helper(i+1, end)
                arr.pop()
        
        for i in range(1, N+1):
            helper(0, i)
        
        sol = 0
        for i in res:
            temp = 0
            for j in i:
                temp ^= j
            
            sol += temp
        
        return sol
    
    def subsetXORSum(self, nums):
        N = len(nums)
        res = 0
        for i in nums:
            res |= i
        
        return res << (N-1)
            
        
                