class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        gridt = [[] for i in range(n)]
        
        res = 0 
        
        for i in range(n):
            for j in range(n):
                same = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        same = False
                        break
                res += same
        
        return res
                
                
                        