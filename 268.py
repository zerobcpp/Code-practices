class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]+1
        else:
            for i in range(len(nums)):
                if i not in nums:
                    return i