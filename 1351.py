# 1351. Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in grid:
            for j in i:
                if j < 0:
                    res += 1
        
        return res
    
    def countNegatives(self, grid):
        res = 0 
        for i in grid:
            n = len(i)
            for j in range(n):
                if i[j] < 0:
                    res += (n - j)
                    break
        
        return res