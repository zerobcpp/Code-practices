class Solution:
    def longestAlternatingSubarray(self, nums: List[int], t: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] <= t and nums[0] % 2 == 0:
                return 1
            else:
                return 0
        res = 0
        r = 0
        
        while r < n:
            
            if nums[r] % 2 == 0 and nums[r] <= t:
                l = r
                while r < n - 1 and nums[r] % 2 != nums[r+1] % 2 and nums[r+1] <= t:
                    r += 1
                res = max(res, r - l + 1)
            r += 1
        
        return res
            
                        