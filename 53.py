#53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        res = float('-inf')
        temp = 0
        for i in nums:
            temp += i
            res = max(temp, res)
            if temp < 0:
                temp = 0

        return res

    def maxSubArray2(self, nums):
        res = float('-inf')
        cur = 0
        for i in nums:
            cur = max(i, cur + i)
            res = max(cur, res)

        return res

    def maxSubArrayn2(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        for i in range(n):
            sub = 0
            for j in range(i, n):
                sub += nums[j]
                res = max(res, sub)

        return res