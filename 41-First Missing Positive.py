class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        N = len(nums)
        
        for i in range(1, N+2):
            if i not in nums:
                return i
        
        return -1