class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def helper(r, c):        
            if r < 0 or r >= n or c < 0 or c >= m:
                return True


        def dfs(r, c):
            stk = [(r, c)]
            seen.add((r, c))
            oob = False
            while stk:
                x, y = stk.pop()
                for dx, dy in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if helper(dx, dy):
                        oob = True
                    elif (dx, dy) not in seen and grid[dx][dy] == 0:
                        stk.append((dx, dy))
                        seen.add((dx, dy))
            return oob

        n = len(grid)
        m = len(grid[0])
        res = 0          
        seen = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i, j) not in seen and not dfs(i, j):
                    res += 1
                    
        return res

'''
               [1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
'''
