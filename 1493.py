# 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        c = defaultdict(int)
        l = 0
        n = len(nums)
        
        for r in range(n):
            idx = nums[r]
            c[idx] = c.get(idx, 0) + 1
            
            while c[0] > 1:
                idx = nums[l]
                c[idx] -= 1
                l += 1
            
            res = max(res, r - l)
        
        return res