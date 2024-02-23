class Solution:
    def fairCandySwap(self, alice: List[int], bob: List[int]) -> List[int]:
        a = sum(alice)
        b = sum(bob)
        avg = abs((a - b)) // 2
        setb = set(bob)
        
        for i in alice:
            if i + avg in setb:
                return [i, i + avg]
        
        return None