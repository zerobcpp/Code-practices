class Solution:
    def successfulPairsn2(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        res = []

        for i in range(n):
            temp = [x * spells[i] for x in potions if x * spells[i] >= success]
            res.append(len(temp))
        
        return res
        # n ^ 2
        # O(2n
 
    def successfulPairs(self, sp, pot, target):
        m = len(pot)
        pot.sort()
        res = []
        
        for i in sp:
            mid = ceil(target / i)
            idx = bisect_left(pot, mid)
            #print(mid, idx)
            if idx < 0:
                res.append(0)
            else:
                res.append(m - idx)
        
        return res
