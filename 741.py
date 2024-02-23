class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        
        dirs = [0, 1, 0, -1, 0]
        st = [(0,0,grid[0][0])]
        seen = {(0, 0)}
        
        cnt = 0
        while st:
            x, y, p = st.pop()
            cnt = max(cnt, p)
            
            for i in range(4):
                dx = x + dirs[i]
                dy = y + dirs[i+1]
                if 0 <= dx < N and 0 <= dy < M:
                    if (dx, dy) not in seen and grid[dx][dy] != -1:
                        cnt = max(cnt, grid[dx][dy] + cnt)
                        st.append((dx, dy, cnt))
                        seen.add((dx, dy))
        
        
        return cnt if ((N-1),(M-1)) in seen else 0
                    