class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return log(n, 3) % 1 == 0 or log(n, 3) <= 1e-9