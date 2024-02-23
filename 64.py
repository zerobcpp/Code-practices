class Solution:
    def minPathSumn2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * (m) for i in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                elif j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif i > 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
        
        print(dp)
        return dp[-1][-1]
    
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        prev = [0] * m
        prev[0] = grid[0][0]

        for i in range(n):
            dp = grid[i]
            for j in range(m):
                if i > 0 and j > 0:
                    dp[j] = grid[i][j] + min(dp[j-1], prev[j])
                elif j > 0:
                    dp[j] += dp[j-1]
                elif i > 0:
                    dp[j] += prev[j]
            
            prev = dp
        
        return prev[-1]