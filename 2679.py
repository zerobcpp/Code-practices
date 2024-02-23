class Solution:
    def distinctIntegers(self, n: int) -> int:
        res = 1
        r = n
        for i in range(2, n+1):

            if n % i == 1:
                res += 1
            if n % r - i == 1:
                res += 1
                
            n -= 1
            
        return res
            