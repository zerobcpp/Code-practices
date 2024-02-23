class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in grid:
            for j in i:
                if j < 0:
                    res += 1
        
        return res