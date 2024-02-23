class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        r = 0   
        l = max(left) if left else 0
        for i in right:
            r = max(n - i, r)
        
        return max(r, l)