class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
#         N = len(grid)
#         M = len(grid[0])
        
#         def helper(i, j):
#             if i >= N or j >= M:
#                 return 0
            
#             cnt = 0
#             cnt += max(helper(i+1, j-1), helper(i+1, j), helper(i+1, j+1)) + grid[i][j]
            
#             return cnt
        
#         return helper(0, 0)            
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(r, c1, c2):
            if r == m: return 0
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            ans = 0
            for nc1 in range(c1 - 1, c1 + 2):
                for nc2 in range(c2 - 1, c2 + 2):
                    if 0 <= nc1 < n and 0 <= nc2 < n:
                        ans = max(ans, dfs(r + 1, nc1, nc2))
            return ans + cherries

        return dfs(0, 0, n - 1)