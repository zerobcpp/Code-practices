class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        seen = set()
        dirs = [0, 1, 0, -1, 0]
        res = []
        
        for i in range(n):
            for j in range(m):
                
                if land[i][j] == 1 and (i, j) not in seen:
                    st = [(i, j)]
                    seen.add((i, j))
                    r2, c2 = i, j
                    #print(i, j, r2, c2)
                    while st:
                        x, y = st.pop()
                        r2 = max(r2, x)
                        c2 = max(c2, y)
                        
                        for k in range(4):
                            dx, dy = x + dirs[k], y + dirs[k+1]
                            
                            if dx >= 0 and dx < n and dy >= 0 and dy < m and land[dx][dy] == 1 and (dx, dy) not in seen:
                                st.append((dx, dy))
                                seen.add((dx, dy))
                    
                    #print(i, j, r2, c2)
                    res.append([i, j, r2, c2])
        
        return res