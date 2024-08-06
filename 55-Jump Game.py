class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        N = len(nums) - 1
        
        possible = 0
        while i <= possible:
            possible = max(possible, i + nums[i])
            if i >= N:
                return True
            i += 1
        
        return False