class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        INF = 100 * 10000
        dp = [[INF] * M for _ in range(N)]
        
        for i in range(M):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, N):
            for j in range(M):
                
                for dx, dy in [(i-1, j-1), (i-1, j), (i-1, j+1)]:
                    if 0 <= dx < N and 0 <= dy < M:
                        dp[i][j] = min(dp[i][j], dp[dx][dy] + matrix[i][j])
        
        #print(dp)
        return min(dp[N-1])