class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        N = len(points)
        #print(points)
        res = 0
        for i in range(1,N):
            x = points[i-1][0]
            dx = points[i][0]
            
            res = max(res, dx - x)
        
        return res