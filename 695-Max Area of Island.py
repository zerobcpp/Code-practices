class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        stack = []
        rb = len(grid)
        cb = len(grid[0])
        res = 0
        
        for i in range(rb):
            for j in range(cb):
                if (i, j) not in seen and grid[i][j]:
                    seen.add((i, j))
                    stack.append((i,j))
                    inC = 0
                    while stack:
                        r, c = stack.pop()
                        inC += 1
                        for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= x < rb) and (0<= y < cb) and grid[x][y] == 1 and (x,y) not in seen:
                                stack.append((x, y))
                                seen.add((x, y))
                    res = max(res, inC)
        return res