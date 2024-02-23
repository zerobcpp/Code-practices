class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        N = len(nums)
        
        for i in range(1, N-2):
            if nums[i-1] > nums[i]:
                return False
        
        return True