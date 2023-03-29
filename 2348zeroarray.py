class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 0
        for r in range(n):
            if nums[r] != 0:
                l = r + 1
            res += (r - l) + 1

        return res

    def zeroFilledSubarray(self, nums):
        count, res = 0, 0
        for i in nums:
            if not i:
                count += 1
            else:
                count = 0
            res += count

        return res