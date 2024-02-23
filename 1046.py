class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        n = len(nums)
        c = {}
        for r in range(n):
            idx = nums[r]
            c[idx] = c.get(idx, 0) + 1
            
            while 0 in c and c[0] > k:
                idx = nums[l]
                c[idx] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
                
            