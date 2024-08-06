class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid)
        @cache
        def helper(i, j):
            if i >= N:
                return 0
            
            ways = float('inf')
            for k in range(M):
                if k == j and i != 0:
                    continue
                ways = min(ways, helper(i+1, k) + grid[i][k])
            
            return ways
        
        return helper(0, 0)
                
    
    def minFallingPathSum(self, grid):
        N = len(grid)
        M = len(grid)
        INF = 100 * 10000
        dp = [[INF] * M for _ in range(N)]
        
        for j in range(M):
            dp[0][j] = grid[0][j]
        
        #print(dp)
        for i in range(1, N):
            for j in range(M):
                for k in range(M):
                    if k == j:
                        continue
                    dp[i][j] = min(dp[i-1][k] + grid[i][j], dp[i][j])
            
            #print(dp)
            #print()
        return min(dp[-1])
                    
            
        '''
        [-73,61,43,-48,-36],
        [3,30,27,57,10],
        [96,-76,84,59,-15],
        [5,-49,76,31,-7],
        [97,91,61,-46,67]
        '''