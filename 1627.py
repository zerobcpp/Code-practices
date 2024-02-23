class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        r = max(right) if right else 0
        l = max(left) if left else 0
        
        return max(r, l)