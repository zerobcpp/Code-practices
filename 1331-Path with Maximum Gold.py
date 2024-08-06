class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        dirs = [0, 1, 0, -1, 0]
        visit = [[0] * M for _ in range(N)]
        LEFT = N * M
        MX = sum(sum(i) for i in grid)
        self.res = 0
        def helper(coin, i, j):
            if grid[i][j] == 0 or i >= N or j >= M or i < 0 or j < 0:
                return
            visit[i][j] = 1
            coin += grid[i][j]

            self.res = max(self.res, coin)
            if coin == MX:
                return MX
            #print(visit, coin)
            for k in range(4):
                dx, dy = i + dirs[k], j + dirs[k+1]
                if 0 <= dx < N and 0 <= dy < M and visit[dx][dy] == 0:
                    helper(coin, dx, dy)
            
            #print(i, j, N, M)
            coin -= grid[i][j]
            visit[i][j] = 0
        
        
        for i in range(N):
            for j in range(M):
                helper(0, i, j)
        
        return self.res
        