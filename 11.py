class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = [[0 for i in height] for j in height]
        
        for i in range(n):
            for j in range(n-1, i, -1):
                area[i][j] = (j-i) *  min(height[j], height[i])
        
        res = 0
        for i in area:
            arr = max(i)
            res = max(arr,res)
        
        return res