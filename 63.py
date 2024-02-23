class Solution:

    
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * (m) for _ in range(n)]

        
        for i in range(m):
            if grid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        
        for i in range(n):
            if grid[i][0] == 0:
                dp[i][0] = 1 
            else:
                break
        
        print(dp)
        
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #print(dp)
        
        return dp[n-1][m-1]
    
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [0] * m
        prev = [0] * m
        prev[0] = 1
        
        for i in range(n):
            dp[0] = prev[0] if grid[i][0] == 0 else 0
            for j in range(1, m):
                if grid[i][j] == 1:
                    dp[j] = 0
                    continue
                dp[j] = prev[j] + dp[j-1]
            #print(prev, dp)
            prev = dp
            
        
        return prev[m-1]
    
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        @cache
        def helper(i, j):
            print(i, j)
            if i == N-1 and j == M-1 and grid[i][j] == 0:
                return 1
            if i >= N or j >= M:
                return 0
            if grid[i][j] == 1: 
                return 0
            
            count = 0
            if i < N:
                count += helper(i+1, j)
            if j < M:
                count += helper(i, j+1)
            
            return count
        
        return helper(0, 0)