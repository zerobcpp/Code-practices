class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        res = []

        for i in range(n):
            temp = [x * spells[i] for x in potions if x * spells[i] >= success]
            res.append(len(temp))
        
        return res