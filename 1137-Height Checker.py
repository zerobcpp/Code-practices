class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c = heights[:]
        c.sort()
        n = len(heights)
        res = 0
        for i in range(n):
            res += 1 if heights[i] != c[i] else 0
        
        return res