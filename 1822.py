# 1822. Sign of the Product of an Array

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
    
    def arraySign(self, nums):
        n = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                n += 1
        
        return 1 if n % 2 == 0 else -1