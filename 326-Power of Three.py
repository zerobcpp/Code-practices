class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        print(log(45,3)%1)
        return log(n, 3) % 1 == 0 or log(n, 3) <= 1e-9 or log(n, 3) % 1 >= 0.9999999999