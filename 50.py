class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = abs(n)
            x = 1 / x
            
        ans = 1
        mul = x
        i = n
        
        while i > 0:
            if i % 2 == 1:
                ans *= mul
            mul *= mul
            i //= 2
            #print(i, mul, ans)
        return ans