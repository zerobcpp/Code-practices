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