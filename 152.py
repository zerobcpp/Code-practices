class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = float('inf')
        mx = -float('inf')
        res = -float('inf')
        
        for i in nums:
            
            if i < 0:
                mn, mx = mx, mn
                
            mn = min(i, mn * i)
            mx = max(i, mx * i)
            res = max(res, mx, mn)
            
        
        
        return res