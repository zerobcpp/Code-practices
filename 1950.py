class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n = 1
        for i in nums:
            n *= i
        
        if n == 0:
            return 0
        elif n > 0:
            return 1
        return -1