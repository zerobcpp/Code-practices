class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = set()
        
        def dfs(i, j):
            st = [(i, j)]
            seen.add((i, j))
            count = 0
            oob = False
            while st:
                x, y = st.pop()

                count += 1
                for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if dx < 0 or dx >= n or dy < 0 or dy >= m:
                        oob = True
                    elif grid[dx][dy] == 1 and (dx, dy) not in seen:
                        seen.add((dx, dy))
                        st.append((dx, dy))
            return count if not oob else 0
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in seen:
                    res = max(res, dfs(i, j))
        
        return res
        