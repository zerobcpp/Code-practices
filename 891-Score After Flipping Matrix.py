class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0
        
        for i in range(1, m):
            zero = one = 0
            for j in range(n):
                if grid[j][i] == 1:
                    one += 1
                else:
                    zero += 1
            
            if zero > one:
                for j in range(n):
                    grid[j][i] = 1 if grid[j][i] == 0 else 0
        
        
        res = 0
        for i in range(n):
            for j in range(m):
                columnScore = grid[i][j] << (m - j - 1)
                res += columnScore
        
        
        return res