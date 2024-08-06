class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        prod = 1
        res = 0
        for i in range(n):
            prod *= nums[i]
            
            while l < n and prod >= k:
                prod /= nums[l]
                l += 1
            if i >= l:
                res += (i - l + 1)
        
        return res
                