class Solution:
    def distinctIntegers(self, n: int) -> int:
        seen = set([n])
        res = 1
        while n > 0:
            for i in range(1, n):
                if n % i == 1:
                    seen.add(i)
            
            n -= 1
        return len(seen)