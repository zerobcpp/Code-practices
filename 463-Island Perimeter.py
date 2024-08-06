class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        st = []
        seen = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    st.append((i, j))
        
        pos = [0, 1, 0, -1, 0]
        
        while st:
            x, y = st.pop()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            
            side = 4
            for i in range(4):
                dx, dy = x + pos[i], y + pos[i+1]
                if 0 <= dx < n and 0 <= dy < m:
                    if grid[dx][dy] == 1:
                        side -= 1
                        if (dx, dy) not in seen:
                            st.append((dx, dy))
            
            res += side
        
        return res
    
    def islandPerimeter(self, grid):
        res = 0
        n = len(grid)
        m = len(grid[0])
        pos = [0, 1, 0, -1, 0]
        for i in range(n): 
            for j in range(m):
                if grid[i][j] == 1:
                    side = 4
                    for k in range(4):
                        dx, dy = i + pos[k], j + pos[k+1]
                        if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 1:
                            side -= 1
                    res += side
        
        return res
        
        