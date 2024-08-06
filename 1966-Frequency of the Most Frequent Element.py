class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = 0
        res = 0
        N = len(nums)
        l = 0
        
        for r in range(N):
            cur += nums[r]
            while (r - l + 1) * nums[r] - cur > k:
                cur -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res