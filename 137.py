class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = dict(dict.fromkeys(nums, 0))
        for i in nums:
            count[i] += 1

        for i, j in count.items():
            if count[i] == 1:
                return i