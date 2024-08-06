class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        nums.sort()
        res = float('inf')
        
        for i in range(4):
            r = n - 4 + i
            
            res = min(res, nums[r] - nums[i])
        
        return res
            
            
            
'''
-3 mx 0 mn
-2 mx, 1mn
-1 mx, 2mn
0 mx, -3 mn
1 mx, -2mn
2 mx, -1mn
3 mx, -0 mn
'''