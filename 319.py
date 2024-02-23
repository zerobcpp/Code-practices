class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulb = [False for i in range(n)]
        
        i = 1
        while i <= n:
            for j in range(len(bulb)):
                if j+1 % i == 0:
                    bulb[j] = not bulb[j]
            i += 1
        
        
        res = bulb.count(True)
        
        return res