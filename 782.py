class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = {}
        
        for i in jewels:
            c[i] = 0
        res = 0
        for i in stones:
            if i in c:
                res += 1
        
        return res