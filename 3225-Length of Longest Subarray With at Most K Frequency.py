class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = 0
        c = defaultdict(int)
        res = 0
        for i in range(N):
            rk = nums[i]
            c[rk] += 1
            while c[rk] > k:
                lk = nums[l]
                c[lk] -= 1
                l += 1
            
            res = max(res, i - l + 1)
        
        return res