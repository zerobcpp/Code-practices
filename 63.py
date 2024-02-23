class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid:
            return res
        n = len(grid)
        m = len(grid[0])
        st = [(0,0)]
        seen = set(st)
        while st:
            x, y = st.pop()
            if x == n - 1 and y == m - 1:
                res += 1
                continue
            seen.add((x, y))
            for dx, dy in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                if 0 <= dx < n and 0 <= dy < m:
                    if (dx, dy) not in seen and grid[dx][dy] != 1:
                        st.append((dx, dy))
                        
            
            #print(st)
        
        return res