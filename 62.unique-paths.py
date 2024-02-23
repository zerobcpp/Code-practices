# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
    
    def uniquePaths(self, m, n):
        return comb(n-1 + m-1, n-1)
    
    def uniquePaths(self, m, n):
        prev = [1] * n
        dp = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + prev[j]
            
            dp, prev = prev, dp
        
        return prev[-1]
        
    
    def uniquePaths(self, m, n):
        
        #@cache
        cache = {}
        def helper(i, j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if (i, j) in cache:
                return cache[i, j]
            
            cache[i, j] = helper(i+1, j) + helper(i, j+1)
            return cache[i, j]
        
        return helper(0, 0)
