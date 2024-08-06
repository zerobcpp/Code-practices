class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        n = len(grid)
        m = len(grid[0])
        
        pos = [0, -1, 0, 1, 0]
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    if (i, j) not in seen:
                        res += 1
                        st = [(i, j)]
                        seen.add((i, j))
                        while st:
                            x, y = st.pop()
                            
                            for k in range(4):
                                dx, dy = x + pos[k], y + pos[k+1]
                                if 0 <= dx < n and 0 <= dy < m:
                                    if grid[dx][dy] == '1' and (dx, dy) not in seen:
                                        st.append((dx, dy))
                                        seen.add((dx, dy))
        
        return res
                        