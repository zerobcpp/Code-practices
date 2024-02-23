class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        r = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            r[i] = nums[nums[i]]
        return r