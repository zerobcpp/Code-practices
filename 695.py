class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        rb = len(grid)
        cb = len(grid[0])
        def expand(r,c):
            if ( (r >= 0 and r < rb) and (c >= 0 and c < cb)) and f'{r},{c}' not in seen and grid[r][c] == 1:
                seen.add(f'{r},{c}')
                return 1 + expand (r+1, c) + expand (r-1, c) + expand (r, c+1) + expand (r, c-1)
            else:
                return 0
        
        
        return max(expand(r,c) for r in range(rb) for c in range(cb))