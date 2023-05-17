# 1498. Number of Subsequences That Satisfy the Given Sum Condition

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        MOD = 10 ** 9 + 7
        while l <= r:
            if nums[l] + nums[r] <= target:
                res += (2 ** (r - l)) % MOD
                l += 1
            else:
                r -= 1
        
        return res % MOD