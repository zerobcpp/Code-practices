class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = log(n, 2)
        return True if c % 1 == 0 else False