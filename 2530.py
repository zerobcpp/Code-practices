class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return max(nums)
        pf = 0
        res = 0
        for i in range(n):
            pf += nums[i]
            res = max(res, math.ceil(pf / (i + 1)))

        return res