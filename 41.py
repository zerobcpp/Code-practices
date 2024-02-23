class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        N = len(nums)
        
        for i in range(N+1):
            if i not in nums:
                return i
        
        return -1