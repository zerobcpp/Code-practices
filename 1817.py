class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        cycle = 1
        while n > 0:
            for i in range(min(n, 7)):
                res += (i + cycle)
            
            n -= 7
            cycle += 1
        
        return res
    
    def totalMoney(self, n):
        res = 0
        cycle = n // 7
        start = 28
        fix = cycle
        res = 0
        while cycle:
            n -= 7
            cycle -= 1
            res += start
            start += 7
        
        for i in range(1, n+1):
            res += (i + fix)
        
        return res
        
        
        
    def totalMoney(self, n):
        res = 0
        cycle = n // 7
        l = 28
        r = 28 + (cycle-1) * 7
        res = ((l + r) * cycle) // 2
        #print(res)
        for i in range(1, n % 7+1):
            res += i + cycle
        
        return res