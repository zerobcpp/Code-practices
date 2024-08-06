class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = 1
        mx = 1
        res = -float('inf')
        
        for i in nums:
            
            if i < 0:
                mn, mx = mx, mn
            
            #print(mn, mx, i, '-1')
            mn = min(i, mn * i)
            mx = max(i, mx * i)
            #print(mn, mx, i, '-2')
            #print("___________")
            
            res = max(res, mx, mn)
            
        
        
        return res