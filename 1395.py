class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        N = len(points)
        for i in range(1, N):
            x, y = points[i]
            dx, dy = points[i-1]
            res += max(abs(x-dx), abs(y-dy))
        
        return res
    